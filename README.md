# backend

### Installation

```bash 
poetry shell
poetry install
```

### Run

```bash
make dev
```
or
```bash
make run
```
### Migrations

Create:
```bash
make create-migration msg='Some message'
```

Migrate:
```bash
make migrate
```

### Format code with Ruff

```bash
make format
```

### To-do
- [X] Customize migration formatting for alembic via ruff