## Modificação de planilhas do Google Sheets usando Python

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | Planilhas com Python
| :label: Tecnologias | Python


![Design sem nome](https://github.com/Bullsyeswild/Planilha_sheets/assets/127852691/72a5644d-794c-4322-a692-891a70bf15e7)


## Detalhes do projeto

Realizei modificações de planilhas do Google Sheets usando Python e através da biblioteca 'gspread'. Ainda me aprofundei em conhecimentos do Google Cloud como criações de credenciais e chaves. Feliz demais pelos objetivos alcançados até aqui!

OBS: Como a 'credencial.json' é particular e não deve ser divulgada, deixo o passo a passo para obterem as respectivas.

### Preparando o ambiente:

- É necessário ter instalado o Python 3 e o gerenciador de pacotes pip, caso não tenha realize a instalação antes de continuar.
- Para instalar o pip no VS Code, basta abrir o terminal do seu 'projeto.py' e digitar: *pip install gspread oauth2client*

### Criando credenciais:

- Acesse o endereço <a href="https://console.developers.google.com/project"> Google Cloud</a> e clique em 'Criar Projeto', preencha com o nome do projeto e clique em criar.
- Clique em cima do nome do projeto, em seguida no canto superior esquerdo clique no menu de navegação -> 'API's e serviços' -> 'Credenciais
- Em 'Criar credenciais' clique em 'Conta de serviço'
- Preencha o campo 'Nome da conta de serviço' e em seguida o papel para aquela conta, eu selecionei 'Projeto -> Proprietário'
- Criado a conta, clique nela e vá para a aba 'Chaves'
- Clique em 'Adicionar Chave' -> 'Criar nova Chave' selecione o formato JSON e confirme (aparecerá um arquivo em download que deve ser colocado na pasta junto com o 'arquivo.py')
## 🚨 Esse arquivo contém as credenciais para acessar o projeto, guarde em segredo.🚨

- No canto esquerdo clique em "Biblioteca" e no campo de busca digite "sheets", em seguida clique em 'Google Sheets API' e após isso em 'Ativar'.

### Criando planilha:

- Crie uma nova planilha no endereço <a href="https://docs.google.com/spreadsheets/u/0/"> aqui </a> e de um titulo qualquer
- Em seguida clique em 'Compartilhar' e coloque o e-mail que foi gerado como 'Conta de Serviço'

### No código:

- Na parte 'credentials.json' coloque o nome do arquivo que foi gerado ao 'Criar nova Chave'
- O ID da planilha é a parte do link da planilha demonstrado como exemplo a seguir:
- "docs.google.com/spreadsheets/d/ ->ID ESTARÁ AQUI <- /edit#gid=0"
