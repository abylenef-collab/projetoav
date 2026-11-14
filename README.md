1. Título do projeto
   
UBS - WEB — Sistema Web de Gestão e Agendamento de Atendimentos em Unidades Básicas de Saúde. 

2. Descrição 

O UBS - WEB é uma plataforma web desenvolvida com o propósito de facilitar a comunicação entre os pacientes e as Unidades Básicas de Saúde (UBS), digitalizando processos como agendamento de consultas, envio de pedidos de exames e acompanhamento de solicitações. O projeto busca solucionar problemas relacionados às filas presenciais, à burocracia administrativa e à falta de comunicação entre os pacientes e a unidade de saúde, proporcionando mais praticidade, organização, transparência e acessibilidade aos serviços públicos de saúde. 

3. Objetivos 

O principal objetivo é desenvolver uma plataforma web funcional e acessível para otimizar a gestão de atendimentos em uma Unidade Básica de Saúde. Objetivos específicos: 

* Implementar um sistema de agendamento online para reduzir filas presenciais.
* Criar um canal digital seguro para o envio de documentos e pedidos de exames. 
* Desenvolver um painel de acompanhamento das solicitações, apresentando datas, horários, profissionais e especialidades. 
* Facilitar a comunicação entre pacientes e funcionários da UBS. 
* Garantir a integridade e a privacidade dos dados dos usuários, seguindo as diretrizes da Lei Geral de Proteção de Dados (LGPD).
  
4. Funcionalidades As funcionalidades a seguir estão descritas como requisitos e recursos previstos na documentação do projeto. 

  4.1. Autenticação de usuários 
  * Login do paciente utilizando CPF e senha. 
  * Cadastro de novos usuários. 
  * Acesso restrito ao painel administrativo da UBS.
   
  4.2. Agendamento de consultas 
  * Consulta de especialidades médicas disponíveis.
  * Visualização de datas e horários com vagas disponíveis.
  * Realização de agendamentos online. 
  * Confirmação ou cancelamento de consultas pela secretaria. 
  
  4.3. Secretaria Digital  Envio de fotos e documentos contendo pedidos de exames. 
  - Pré-visualização dos arquivos enviados. 
  - Campo para observações do paciente. 
  - Análise dos documentos pela equipe administrativa. 
  * Possibilidade de aprovar, rejeitar ou solicitar o reenvio dos documentos. 
  
  4.4. Acompanhamento e notificações 
  - Consulta ao histórico de solicitações. 
  - Acompanhamento dos status dos agendamentos (pendente, confirmado ou cancelado). 
  - Visualização do profissional e da especialidade do atendimento.
  - Recebimento de notificações sobre confirmações, pendências e rejeições. 
  
  Observação: o documento de referência apresenta essas funcionalidades como requisitos e recursos previstos, mas não comprova que todas estejam implementadas e disponíveis para utilização.
  
5. Tecnologias utilizadas

De acordo com a documentação, foram previstas e utilizadas as seguintes tecnologias e ferramentas:

- HTML: estruturação das páginas e elementos da interface.  
- CSS: estilização e organização visual das telas. 
- JavaScript: implementação de interatividade e comportamentos da interface. 
- Banco de Dados Relacional: armazenamento e gerenciamento das informações do sistema. 
- Visual Studio Code (VS Code): ambiente de desenvolvimento utilizado para a programação. 

Arquitetura: MVC (Model-View-Controller), utilizada para organizar a estrutura do sistema. 

Metodologia: versão adaptada do Scrum, com reuniões semanais e desenvolvimento incremental. 

6. Pré-requisitos 

Para o desenvolvimento e a possível execução do projeto, são considerados necessários: 
- Computador com acesso à internet. 
- Navegador web atualizado (Google Chrome, Mozilla Firefox ou Microsoft Edge). 
- Visual Studio Code ou outro editor de código. 
- Banco de dados relacional configurado. 
- Suporte a HTML, CSS e JavaScript. 
- Observação: o documento não especifica o banco de dados escolhido, suas versões ou outros requisitos técnicos de instalação.

7. Instalação e execução

O projeto tem como objetivo desenvolver um software voltado ao gerenciamento e cadastro de máquinas e suas manutenções no LAMAC (Laboratório de Manutenção de Computadores) no IFRN Campus SGA, proporcionando maior organização, agilidade e segurança no armazenamento das informações relacionadas aos equipamentos no local.

Para a execução do projeto, é necessário seguir os  seguintespassos:

**1. Clonar o repositório**

    git clone https://github.com/abylenef-collab/projetoav.git

**2. Criar o ambiente virtual**

    python -m venv ./venv
  
  Ative o ambiente:
  
  No Windows:  
  
    venv\Scripts\activate
  
  No Linux ou Mac: 
  
    source venv/bin/activate

**3. Instalar as dependências**

    pip install -r requirements.txt
  
  (Isso instala o Django e o python-dotenv de uma só vez)

**4. Criar o arquivo .env**
  
  Copie o arquivo modelo e renomeie para .env:
  
    cp .env.example .env
  
  No Windows, se o comando cp não funcionar:
  
    copy .env.example .env
  
  Abra o .env. Ele contém:
    SECRET_KEY=
    DEBUG=True 

**5. Gerar uma SECRET_KEY**

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

  O terminal imprimirá uma chave aleatória, como:
  
    django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6

**6. Colar a chave no .env**

Copie a chave impressa e cole no arquivo (sem aspas e sem espaços):

  SECRET_KEY=django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
  DEBUG=True

**7. criar o banco de dados**

    python manage.py migrate

**8. Rodar o projeto**

    python manage.py runserver

  Acesse http://localhost:8000/ no navegador.

9. Equipe 

- Abylene Freitas de França 
- Ana Karolline Carneiro Souza 
