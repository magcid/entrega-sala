# Instruções para Envio ao GitHub

## Pré-requisitos
- Conta no GitHub configurada
- Git instalado e configurado
- Acesso ao repositório remoto

## Passos para Enviar ao GitHub

### 1. Criar Repositório no GitHub
1. Acesse o GitHub e crie um novo repositório chamado `entrega-sala`
2. Não inicialize com README, .gitignore ou license

### 2. Configurar o Remote
```bash
# Substitua SEU_USUARIO pelo seu nome de usuário do GitHub
git remote add origin https://github.com/SEU_USUARIO/entrega-sala.git
```

### 3. Fazer Push para o GitHub
```bash
# Enviar a branch master
git push -u origin master

# Ou se estiver usando SSH
git push -u origin master
```

## Comandos Adicionais Úteis

### Verificar conexão com o remote
```bash
git remote -v
```

### Verificar status do repositório
```bash
git status
```

### Ver histórico de commits
```bash
git log --oneline
```

## Notas Importantes

- O repositório local já está configurado e com a versão inicial commitada
- Todos os arquivos necessários para o funcionamento do sistema estão incluídos
- Certifique-se de ter permissão para escrever no repositório remoto
- O projeto foi testado e está pronto para uso no laboratório

## Estrutura do Projeto após envio
```
entrega-sala/
├── PLANEJAMENTO.md          # Documentação do planejamento
├── README.md                # Documentação de uso
├── provas/                  # Pasta para provas (com arquivo de exemplo)
│   └── prova.pdf            # Arquivo de prova (exemplo)
├── respostas/               # Pasta para respostas dos alunos
├── requirements.txt         # Dependências Python
├── run.sh                   # Script para iniciar o servidor
├── server.py                # Servidor Flask principal
├── static/                  # Arquivos estáticos (CSS, JS)
│   ├── style.css            # Estilos CSS
│   └── script.js            # JavaScript
└── templates/               # Templates HTML
    └── index.html           # Página principal
```