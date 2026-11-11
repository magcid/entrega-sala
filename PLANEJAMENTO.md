# Planejamento Detalhado - Sistema de Entrega de Provas para Laboratório

## Visão Geral
Vamos criar um sistema web local para entrega de provas em laboratório de informática, onde o professor executa o servidor e os alunos acessam via rede local.

## Arquitetura do Sistema

### Componentes Principais
1. **Servidor Web** - Executado na máquina do professor
2. **Interface Web** - Acessada pelos alunos via navegador
3. **Sistema de Upload/Download** - Para provas e respostas

### Funcionalidades
- Download da prova (formato PDF)
- Envio de respostas em arquivo ZIP
- Controle de acesso baseado em rede local
- Armazenamento de respostas organizadas por aluno

## Estrutura do Projeto

### Diretórios
```
entrega-sala/
├── server.py              # Servidor web (Python)
├── requirements.txt       # Dependências Python
├── provas/                # Pasta para armazenar provas
│   └── prova.pdf          # Arquivo da prova (exemplo)
├── respostas/             # Pasta para armazenar respostas
├── templates/             # Templates HTML
│   └── index.html         # Página principal
├── static/                # Arquivos estáticos
│   ├── style.css          # Estilos CSS
│   └── script.js          # JavaScript
└── README.md              # Documentação
```

## Detalhamento das Funcionalidades

### 1. Servidor Web (server.py)
- Usar Flask (Python) para criar servidor HTTP
- Servir arquivos estáticos e páginas HTML
- Gerenciar download da prova
- Processar upload de arquivos ZIP
- Armazenar informações sobre alunos e respostas

### 2. Interface Web
- Página principal com:
  - Link para download da prova
  - Formulário para envio de resposta (seleção de arquivo ZIP)
  - Campo para nome do aluno
- Design responsivo para funcionar em diferentes dispositivos

### 3. Sistema de Upload/Download
- Download da prova: `/prova` - serve o arquivo PDF
- Upload de respostas: `/upload` - recebe arquivo ZIP, salva com nome baseado no aluno
- Validação de tipo de arquivo (apenas ZIP)
- Armazenamento organizado por aluno

## Dependências Necessárias (requirements.txt)

```
Flask==2.3.3
Werkzeug==2.3.7
```

## Configuração de Rede Local

### Acesso
- O servidor será acessível apenas na rede local do laboratório
- Endereço IP fixo ou DHCP com reserva de IP
- Porta padrão 5000 (ou outra porta disponível)
- Acesso restrito apenas aos alunos da rede local

## Segurança e Restrições

### Limitações do Sistema
1. Funciona apenas em rede local (sem internet)
2. Sem autenticação (acesso baseado em rede)
3. Controle de acesso limitado ao ambiente local
4. Arquivos ZIP enviados são armazenados localmente no servidor

## Fluxo de Uso

### Para o Professor:
1. Preparar a prova em PDF na pasta `provas/`
2. Iniciar o servidor: `python server.py`
3. Comunicar o IP do servidor aos alunos
4. Verificar respostas na pasta `respostas/`

### Para os Alunos:
1. Acessar página no navegador: `http://IP_DO_SERVIDOR:5000`
2. Baixar a prova
3. Resolver a prova e compactar em ZIP
4. Enviar o arquivo ZIP com suas respostas

## Considerações Técnicas

### Protocolo de Comunicação
- HTTP/HTTPS (apenas local)
- Formatos: PDF para provas, ZIP para respostas
- Codificação: UTF-8

### Armazenamento
- Arquivos salvos localmente na máquina do professor
- Estrutura organizada por aluno
- Nomeação automática dos arquivos com timestamp

## Requisitos Mínimos do Sistema

### Hardware:
- Máquina do professor (servidor)
- Dispositivos dos alunos (computadores ou tablets)

### Software:
- Python 3.7+
- Flask (framework web)
- Navegador web moderno para alunos

### Rede:
- Rede local funcional
- IPs estáticos ou reservados para o servidor
- Acesso restrito ao laboratório

## Implementação Futura (opcional)

### Funcionalidades Adicionais:
1. Controle de horário de início/fim da prova
2. Validação de conteúdo do arquivo ZIP
3. Sistema de notificação para professor
4. Backup automático das respostas
5. Interface de administração para gerenciar provas

Este planejamento cria um sistema robusto e simples que atende às necessidades específicas do laboratório de informática, funcionando exclusivamente com a rede local disponível.