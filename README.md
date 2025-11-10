[![CI](https://github.com/LucasF087/gerenciador-tarefas-agil/actions/workflows/python-app.yml/badge.svg)](https://github.com/LucasF087/gerenciador-tarefas-agil/actions/workflows/python-app.yml)

# Gerenciador de Tarefas Ágil

**Repositório:** https://github.com/LucasF087/gerenciador-tarefas-agil

## Resumo
Sistema educativo para gerenciamento de tarefas (CRUD) desenvolvido em Python. Implementa:
- API REST JSON (Flask) e interface web simples (Bootstrap)
- CLI para uso via terminal
- Persistência em JSON (`/data/tasks.json`)
- Testes automatizados com Pytest
- Pipeline CI com GitHub Actions
- Diagramas UML (Mermaid + imagens PNG/SVG)

## Estrutura do projeto
```
/src
  ├── tasks.py        # Lógica de domínio (dataclass + CRUD)
  ├── cli.py          # CLI de linha de comando
  └── app.py          # Servidor Flask (API + interface web)
/templates            # HTML para a interface web
/tests
/docs                 # Diagramas mermaid + imagens (PNG/SVG)
/data/tasks.json
README.md
.github/workflows/python-app.yml
.gitignore
LICENSE
git-prepare.sh        # Script opcional para simular histórico de commits
```

## Como executar (local)

### 1) Ambiente (recomendado Python 3.11+)
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate    # Windows (PowerShell)
pip install --upgrade pip
pip install -r requirements.txt || pip install flask pytest
```

### 2) Rodar o servidor web (Flask)
```bash
python -m src.app
# Abra http://127.0.0.1:5000/ no navegador
```

### 3) CLI (opcional)
```bash
python -m src.cli list
python -m src.cli create "Minha tarefa" --description "detalhes"
```

### 4) Testes
```bash
pip install pytest
pytest -q
```

## Rotas principais (API)
- `GET /api/tasks` — lista tarefas
- `POST /api/tasks` — cria tarefa (JSON: { "title": "...", "description": "..." })
- `GET /api/tasks/<id>` — obtém tarefa
- `PUT /api/tasks/<id>` — atualiza (JSON)
- `DELETE /api/tasks/<id>` — remove tarefa

## Modelo de Kanban (sugestão de cards)
- Inicializar repositório e README
- Implementar tasks.py (domínio)
- Implementar CLI básico
- Implementar API Flask (GET/POST)
- Interface web (listar/criar)
- Testes unitários (Pytest)
- CI: GitHub Actions
- Diagramas UML e documentação
- Simular mudança de escopo (adicionar campo `priority`)
- Preparar vídeo pitch
- Ajustes finais e correções

## Modelo de commits semânticos (exemplos)
- `feat(tasks): add create_task and persistence`
- `fix(cli): handle missing arguments`
- `test: add pytest for task creation`
- `chore(ci): add github actions workflow`
- `docs: add UML diagrams`

## Mudança de escopo (exemplo aplicado)
Adicionado o campo `priority` nas tarefas (valores: `low`, `medium`, `high`) para permitir priorização simples no Kanban. Documentado no README.

## Observações
- Coloque os arquivos de diagrama (PNG/SVG) em `/docs` antes de subir para o GitHub.
- O arquivo `git-prepare.sh` é opcional e serve para gerar um histórico local de commits (use com cuidado).

---
Gerado por assistente — pronto para entrega.
