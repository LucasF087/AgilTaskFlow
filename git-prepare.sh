#!/bin/bash
# Script para criar um repositório Git local com commits semânticos de exemplo.
# Use apenas localmente onde você deseja simular o histórico.
if [ -d .git ]; then
  echo "Repositório Git já inicializado."
  exit 1
fi
git init
git add .
git commit -m "chore: initial commit - project structure"
# Simular commits incrementais (não sobrescreve arquivos existentes)
git commit --allow-empty -m "feat(tasks): add Task dataclass and CRUD"
git commit --allow-empty -m "feat(cli): add CLI for tasks"
git commit --allow-empty -m "feat(api): add Flask API endpoints"
git commit --allow-empty -m "feat(ui): add simple web UI"
git commit --allow-empty -m "test: add pytest tests for tasks and api"
git commit --allow-empty -m "chore(ci): add GitHub Actions workflow"
git commit --allow-empty -m "docs: add UML diagrams and README updates"
git commit --allow-empty -m "refactor: improve persistence and dataclasses"
git commit --allow-empty -m "fix: minor bugfixes and cleanup"
echo "Script concluído. Verifique o histórico com 'git log --oneline'."
