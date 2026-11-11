# Sistema de Entrega de Provas para Laboratório de Informática

Sistema para entrega de provas em laboratório de informática, funcionando apenas com rede local.

## 📋 Visão Geral

Este sistema permite a entrega de provas em laboratórios de informática utilizando uma rede local. Os alunos podem baixar as provas e enviar suas respostas através de um interface web simples e responsiva, sem necessidade de conexão com a internet.

## ✨ Funcionalidades

- 📥 Download da prova pelo aluno
- 📤 Envio de respostas em arquivo ZIP
- 💻 Interface web simples e responsiva
- 🔐 Funciona exclusivamente com rede local (sem internet)
- 🗂️ Organização automática das respostas por aluno e timestamp

## ⚙️ Configuração

### Requisitos

- Python 3.7+
- Flask

### Instalação

```bash
pip install -r requirements.txt
```

### Execução

```bash
python server.py
```

O servidor será iniciado em `http://localhost:5000` e poderá ser acessado pelos alunos via rede local.

## 🗂️ Estrutura do Projeto

```
.
├── server.py           # Servidor Flask principal
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html      # Página principal
├── static/
│   ├── css/            # Arquivos CSS
│   └── js/             # Arquivos JavaScript
├── provas/             # Diretório para armazenar as provas
└── respostas/          # Diretório para armazenar as respostas enviadas pelos alunos
```

## 🚀 Uso

1. Coloque a prova em formato PDF na pasta `provas/` com o nome `prova.pdf`
2. Inicie o servidor: `python server.py`
3. Alunos acessam via navegador local em `http://IP_DO_SERVIDOR:5000`
4. Alunos baixam a prova e enviam suas respostas em arquivo ZIP

## 🛡️ Notas Importantes

- O sistema funciona apenas com rede local
- Não há autenticação, pois o acesso é restrito à rede local
- As respostas são salvas na pasta `respostas/` com nomes baseados no nome do aluno e timestamp

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuidores

Este projeto existe graças às pessoas que contribuem com o código e feedback.

## 🙏 Agradecimentos

- Agradeço ao laboratório de informática pela oportunidade de desenvolver este sistema