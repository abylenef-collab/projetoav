// Aplica o tema salvo antes da página aparecer
(function () {
    const salvo = localStorage.getItem('tema');
    document.documentElement.setAttribute('data-bs-theme', salvo || 'light');
})();

// Faz o botão funcionar
document.addEventListener('DOMContentLoaded', function () {
    const botao = document.getElementById('btn-tema');
    if (!botao) return;

    botao.addEventListener('click', function () {
        const atual = document.documentElement.getAttribute('data-bs-theme');
        const novo = atual === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-bs-theme', novo);
        localStorage.setItem('tema', novo);
    });
});

// ===== Transição suave ao trocar de tela =====
document.addEventListener('click', function (e) {
    const link = e.target.closest('a');
    if (!link) return;

    // Ignora links que não devem ter transição
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#')) return;
    if (link.target === '_blank') return;
    if (link.origin !== window.location.origin) return;
    if (e.ctrlKey || e.metaKey || e.shiftKey) return;

    e.preventDefault();
    document.body.classList.add('saindo');

    // Espera o fade terminar e só então troca de página
    setTimeout(function () {
        window.location.href = link.href;
    }, 250);
});

// Se voltar pela seta do navegador, tira o efeito de "saindo"
window.addEventListener('pageshow', function (e) {
    if (e.persisted) {
        document.body.classList.remove('saindo');
    }
});