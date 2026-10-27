# CRUD Users — Flet + SQLite3

Aplicação desktop de CRUD (Create, Read, Update, Delete) construída com **Python** e **[Flet](https://flet.dev)**, utilizando **SQLite3** como banco de dados local para persistência dos usuários.

## Funcionalidades

- **Criar** — formulário no topo da tela para registrar um novo usuário (nome com mínimo de 4 caracteres).
- **Listar** — exibe todos os usuários cadastrados, com numeração e rolagem automática.
- **Editar** — botão de edição abre um modal (`AlertDialog`) com o nome atual; ao salvar, a linha é atualizada na interface sem recarregar a lista.
- **Excluir** — botão de exclusão abre um modal de confirmação; ao confirmar, a linha é removida da interface.
- **Feedback visual** — `SnackBar` informando o sucesso ou a falha de cada operação.
- **Persistência** — os dados ficam salvos em `database/app.db` mesmo após fechar o aplicativo.

## Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.12+ | Linguagem |
| Flet 1.0 | Interface gráfica desktop |
| SQLite3 | Banco de dados local (biblioteca nativa do Python) |

## Requisitos

- Python 3.12 ou superior
- Flet 1.0

## Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/maryosilva/flet-crud-sqlite3.git
cd flet-crud-sqlite3

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python main.py
```

> O banco de dados (`database/app.db`) e a tabela `usuarios` são criados automaticamente na primeira execução.

## Estrutura do projeto

```text
flet-crud-sqlite3/
│
├── main.py                  # Ponto de entrada: monta a página e conecta os componentes
│
├── database/
│   ├── __init__.py          # Exporta conexão e inicializa o banco (init_db)
│   ├── connection.py        # Conexão com SQLite (context manager) e criação da tabela
│   └── app.db               # Arquivo do banco de dados (gerado automaticamente)
│
├── models/
│   ├── __init__.py
│   └── user.py              # Modelo User (id, name) com from_row / to_dict
│
├── services/
│   ├── __init__.py
│   └── user_service.py      # Operações CRUD: create, get_all, get_by_id, update, delete
│
├── components/
│   ├── __init__.py
│   ├── user_form.py         # Formulário de cadastro (CREATE)
│   ├── user_list.py         # Listagem de usuários (READ)
│   ├── user_update.py       # Modal de edição (UPDATE)
│   └── user_delete.py       # Modal de exclusão (DELETE)
│
├── requirements.txt
├── pyrightconfig.json
└── README.md
```

### Arquitetura em camadas

```text
┌─────────────────────────────────────────────┐
│  components/   →  UI Flet (formulário,      │
│                   lista, modais, SnackBars) │
└──────────────────────┬──────────────────────┘
                       │ chama
┌──────────────────────▼──────────────────────┐
│  services/     →  regras de negócio e        │
│                   operações CRUD            │
└──────────────────────┬──────────────────────┘
                       │ usa
┌──────────────────────▼──────────────────────┐
│  database/     →  conexão SQLite            │
│  models/       →  estrutura de dados        │
└─────────────────────────────────────────────┘
```

- **`main.py`** — cria a página, instancia o formulário e a lista, e propaga os callbacks de criação/atualização/exclusão para a interface.
- **`database/connection.py`** — `get_db_connection()` é um *context manager* que abre/fecha a conexão; `init_db()` cria a tabela `usuarios` se não existir (executado automaticamente ao importar `database`).
- **`services/user_service.py`** — funções puras de CRUD com validação (nome com pelo menos 4 caracteres), usando transações com `commit`/`rollback`.
- **`models/user.py`** — classe `User` com `from_row()` para conversão direta de `sqlite3.Row`.
- **`components/`** — cada operação da UI isolada em seu próprio módulo, comunicando-se por callbacks (`on_user_created`, `on_updated`, `on_deleted`).

## Esquema do banco de dados

```sql
CREATE TABLE usuarios (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

## Validações

- O nome é sempre limpo com `strip()` antes de salvar.
- Nomes com menos de 4 caracteres lançam `ValueError`, exibida ao usuário via `SnackBar`.
- Operações no banco usam `try/except` com `rollback` em caso de erro.

## Licença

Este é um projeto de estudo. Sinta-se livre para usá-lo como referência.
