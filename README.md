# Flet CRUD Tasks

Aplicação de gerenciamento de tarefas desenvolvida com [Flet](https://flet.dev/), permitindo operações CRUD (Create, Read, Update, Delete) com persistência local em arquivo JSON.

## Funcionalidades

- Adicionar novas tarefas
- Visualizar lista de tarefas
- Editar tarefas existentes
- Marcar tarefas como concluídas
- Excluir tarefas
- Contador de tarefas
- Persistência automática em arquivo JSON

## Pré-requisitos

- Python 3.10 ou superior
- pip

## Instalação

1. Clone o repositório ou baixe os arquivos
2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install flet
```

## Execução

```bash
python main.py
```

A aplicação será aberta automaticamente no navegador.

## Estrutura do Projeto

```
flet/
├── main.py      # Código principal da aplicação
├── db.json      # Banco de dados local (tarefas)
└── .venv/       # Ambiente virtual Python
```

## Formato dos Dados

As tarefas são armazenadas em `db.json` com a seguinte estrutura:

```json
[
    {
        "id": 1,
        "description": "Descrição da tarefa",
        "isCompleted": false
    }
]
```

## Tecnologias

- Python
- Flet (UI Framework)
- JSON (Armazenamento local)