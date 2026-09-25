/* ============================================
   Sistema de Gerenciamento de Tarefas
   script.js - Funcionalidades JavaScript
   Complementa o Bootstrap 5
   ============================================ */

// ---------- Filtrar Tarefas na Tabela ----------
function filtrarTarefas() {
    const input = document.getElementById('buscaTarefa');
    const filtro = input.value.toLowerCase();
    const tabela = document.getElementById('tabelaTarefas');
    const linhas = tabela.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    const semResultados = document.getElementById('semResultados');
    let encontrou = false;

    for (let i = 0; i < linhas.length; i++) {
        const colunaTitulo = linhas[i].getElementsByTagName('td')[1];
        if (colunaTitulo) {
            const texto = colunaTitulo.textContent || colunaTitulo.innerText;
            if (texto.toLowerCase().indexOf(filtro) > -1) {
                linhas[i].style.display = '';
                encontrou = true;
            } else {
                linhas[i].style.display = 'none';
            }
        }
    }

    if (!encontrou) {
        tabela.style.display = 'none';
        semResultados.classList.remove('d-none');
    } else {
        tabela.style.display = '';
        semResultados.classList.add('d-none');
    }
}

// ---------- Confirmar Exclusao de Tarefa ----------
function confirmarExclusao(id, titulo) {
    const modal = new bootstrap.Modal(document.getElementById('modalConfirmarExclusao'));
    const corpo = document.getElementById('corpoModalExclusao');
    const btnConfirmar = document.getElementById('btnConfirmarExclusao');

    corpo.innerHTML = `
        <p>Tem certeza que deseja excluir a tarefa:</p>
        <p class="fw-bold text-danger"><i class="bi bi-exclamation-triangle"></i> ${titulo}</p>
        <p class="text-muted small">Esta acao nao pode ser desfeita.</p>
    `;

    btnConfirmar.href = `/tarefas/${id}/excluir/`;
    modal.show();
}

// ---------- Atualizar Contadores dos Cards ----------
function atualizarContadores() {
    const tabela = document.getElementById('tabelaTarefas');
    if (!tabela) return;

    const linhas = tabela.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    let total = 0;
    let pendentes = 0;
    let andamento = 0;
    let concluidas = 0;

    for (let i = 0; i < linhas.length; i++) {
        if (linhas[i].style.display === 'none') continue;

        const colunaStatus = linhas[i].getElementsByTagName('td')[4];
        if (colunaStatus) {
            const badge = colunaStatus.querySelector('.badge');
            if (badge) {
                const classe = badge.className;
                total++;

                if (classe.includes('bg-warning')) {
                    pendentes++;
                } else if (classe.includes('bg-info')) {
                    andamento++;
                } else if (classe.includes('bg-success')) {
                    concluidas++;
                }
            }
        }
    }

    document.getElementById('contador-total').textContent = total;
    document.getElementById('contador-pendentes').textContent = pendentes;
    document.getElementById('contador-andamento').textContent = andamento;
    document.getElementById('contador-concluidas').textContent = concluidas;
}

// ---------- Destacar Tarefa com Prazo Proximo ----------
function destacarPrazos() {
    const hoje = new Date();
    const tresDias = new Date();
    tresDias.setDate(hoje.getDate() + 3);

    const linhas = document.querySelectorAll('#tabelaTarefas tbody tr');

    linhas.forEach(function (linha) {
        const colunaPrazo = linha.getElementsByTagName('td')[3];
        if (!colunaPrazo) return;

        const textoPrazo = colunaPrazo.textContent.trim();
        if (!textoPrazo) return;

        const partes = textoPrazo.split('/');
        if (partes.length !== 3) return;

        const prazo = new Date(partes[2], partes[1] - 1, partes[0]);
        const badge = linha.getElementsByTagName('td')[4].querySelector('.badge');

        if (badge && !badge.classList.contains('bg-success')) {
            if (prazo < hoje) {
                colunaPrazo.classList.add('text-danger', 'fw-bold');
                colunaPrazo.innerHTML += ' <i class="bi bi-exclamation-circle text-danger"></i>';
            } else if (prazo <= tresDias) {
                colunaPrazo.classList.add('text-warning', 'fw-bold');
                colunaPrazo.innerHTML += ' <i class="bi bi-clock-fill text-warning"></i>';
            }
        }
    });
}

// ---------- Alternar Status da Tarefa ----------
function alternarStatus(id, statusAtual) {
    const novosStatus = {
        'pendente': 'em_andamento',
        'em_andamento': 'concluida',
        'concluida': 'pendente'
    };

    const novoStatus = novosStatus[statusAtual] || 'pendente';
    window.location.href = `/tarefas/${id}/alterar-status/?novo_status=${novoStatus}`;
}

// ---------- Limpar Busca ----------
function limparBusca() {
    const input = document.getElementById('buscaTarefa');
    input.value = '';
    filtrarTarefas();
    input.focus();
}

// ---------- Mostrar/Ocultar Botao de Limpar Busca ----------
function toggleBotaoLimpar() {
    const input = document.getElementById('buscaTarefa');
    const btnLimpar = document.getElementById('btnLimparBusca');

    if (input && btnLimpar) {
        if (input.value.length > 0) {
            btnLimpar.classList.remove('d-none');
        } else {
            btnLimpar.classList.add('d-none');
        }
    }
}

// ---------- Atalho de Teclado: "/" para focar na busca ----------
document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        const input = document.getElementById('buscaTarefa');
        if (input) input.focus();
    }

    if (e.key === 'Escape') {
        const input = document.getElementById('buscaTarefa');
        if (input && document.activeElement === input && input.value.length > 0) {
            limparBusca();
        }
    }
});

// ---------- Inicializacao ----------
document.addEventListener('DOMContentLoaded', function () {
    // Atualiza contadores ao carregar
    atualizarContadores();

    // Destaca prazos proximos ou vencidos
    destacarPrazos();

    // Listener no campo de busca
    const inputBusca = document.getElementById('buscaTarefa');
    if (inputBusca) {
        inputBusca.addEventListener('input', function () {
            filtrarTarefas();
            atualizarContadores();
            toggleBotaoLimpar();
        });
    }
});