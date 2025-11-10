[![CI](https://github.com/LucasF087/gerenciador-tarefas-agil/actions/workflows/python-app.yml/badge.svg)](https://github.com/LucasF087/gerenciador-tarefas-agil/actions/workflows/python-app.yml)

---

# 🧠 **AgilTaskFlow — Sistema de Gerenciamento de Tarefas Ágil**

---

## 🔗 **Repositório oficial:** [github.com/LucasF087/AgilTaskFlow](https://github.com/LucasF087/AgilTaskFlow)

---

O **AgilTaskFlow** é um sistema desenvolvido em **Python** com o objetivo de aplicar, na prática, os conceitos de **Engenharia de Software** e **Metodologias Ágeis**.

O projeto permite o gerenciamento completo de tarefas por meio de um **sistema CRUD** (criar, listar, atualizar e excluir), incorporando boas práticas de desenvolvimento, testes automatizados e integração contínua via **GitHub Actions**.

---

## 🎯 **Objetivo do Projeto**

O projeto foi criado para demonstrar a aplicação de práticas ágeis e ferramentas de apoio ao ciclo de desenvolvimento de software, abordando desde a modelagem até a automação de testes e versionamento.

A proposta central é desenvolver uma solução simples e funcional que simule um ambiente real de trabalho com metodologias ágeis — integrando **Kanban**, **controle de versão (Git/GitHub)** e **integração contínua (CI)**.

---

## 📋 **Escopo Funcional**

O **AgilTaskFlow** oferece as seguintes funcionalidades principais:

- ✅ Criar, listar, editar e excluir tarefas (CRUD completo);  
- 🗂️ Armazenamento local em formato **JSON**;  
- 🚦 Campo adicional de **prioridade** (*feature implementada durante a mudança de escopo*);  
- 🔍 Filtragem e manipulação de tarefas em linha de comando (CLI);  
- 🧪 Testes automatizados com **PyTest** para validação do sistema;  
- 🔄 Execução automática de testes com **GitHub Actions** a cada *push*.

---

## 🧩 **Metodologia Ágil Utilizada (Kanban)**

Durante o desenvolvimento, foi utilizada a metodologia **Kanban**, organizada no **GitHub Projects**, com as colunas:

- 📝 **To Do (A Fazer)**  
- 🚧 **In Progress (Em Progresso)**  
- ✅ **Done (Concluído)**  

Cada card representou uma etapa ou tarefa do projeto, acompanhando o progresso ao longo do ciclo de desenvolvimento.

---

## 🔄 **Mudança de Escopo**

Durante o desenvolvimento do projeto foi simulada uma **mudança de escopo**, conforme exigido nos requisitos da entrega.  
A alteração escolhida foi a implementação do campo **priority** dentro das tarefas, permitindo que o usuário atribua níveis de prioridade para cada *Task*, aumentando o controle de foco, planejamento e impacto sobre o fluxo de trabalho.

### 🧠 **Justificativa**
No contexto real de engenharia de software, mudanças de requisitos são constantes e ciclos iterativos são necessários para adaptar o produto ao contexto de negócio.  
A inclusão da prioridade atendeu uma necessidade de melhor organização e alinhamento com práticas ágeis (como **Kanban**, **Scrum** ou **Scrumban**), permitindo que o sistema diferencie tarefas importantes de tarefas triviais.

### ⚙️ **Alteração Realizada**
- Nova propriedade `priority` adicionada na classe `Task`;
- Persistência atualizada no arquivo JSON;
- Endpoints da API atualizados para receber e retornar prioridades;
- Testes ajustados para cobrir o funcionamento da nova feature.

### 📎 **Evidências**
- Novo card criado no Kanban representando a mudança de escopo (print presente em `/docs/prints/kanban_new_card_scope.png`);
- Commit correspondente à mudança: *hash do commit que implementou esta feature* (exemplo: `a88c775`);
- README atualizado incluindo esta explicação.

Essa mudança reflete uma adaptação real de requisitos dentro de um ciclo ágil, com controle via **Kanban** e versionamento via **GitHub**.

---

## ⚙️ **Estrutura do Projeto**

AgilTaskFlow/

├── .github/
│ └── workflows/
│ └── python-app.yml # CI/CD configurado com PyTest
│
├── data/
│ └── tasks.json # Base de dados local (JSON)
│
├── docs/
│ ├── theory.md # Parte teórica, conceitos e diagramas UML
│ ├── video_pitch_script.md # Roteiro para o vídeo pitch do projeto
│ └── prints/ # Evidências (Kanban, testes, execução etc.)
│
├── src/
│ ├── app.py # Arquivo principal do sistema (Flask)
│ └── tasks.py # Lógica de manipulação das tarefas (CRUD)
│
├── tests/
│ ├── test_app.py # Testes unitários do app principal
│ ├── test_tasks.py # Testes unitários das funções principais
│ └── test_tasks_extra.py # Testes complementares
│
├── pytest.ini # Configuração do PyTest
├── requirements.txt # Dependências do projeto
└── README.md # Documentação geral

---

## 🚀 **Instalação e Execução (Windows — PowerShell)**

💡 *Estes passos funcionam no Windows PowerShell. Em Linux/macOS, use `python3` e `source venv/bin/activate`.*

### 1️⃣ Criar e ativar o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

---

### 2️⃣ Instalar dependências:

pip install -r requirements.txt

---

### 3️⃣ Travar versões (opcional, mas recomendado):

pip freeze > requirements.txt

---

### 4️⃣ Executar a aplicação:

Se a sua aplicação for um Flask simples (como este projeto):

- Exemplo 1: Executar diretamente

python src/app.py

- Exemplo 2: Usando FLASK_APP

$env:FLASK_APP = "src.app"

```
flask run

---

**O servidor será iniciado em:**

🔗 **http://127.0.0.1:5000**

---

## 🧪 **Testes Automatizados**

Rodar os testes localmente:

pytest -q

---

Resultado esperado:

...                                                                 [100%]

3 passed in 0.20s

---

## 🌐 **Exemplos de Chamada à API (via CMD)**

⚠️ No Windows PowerShell, use curl.exe em vez de curl. Os exemplos abaixo funcionam perfeitamente no Prompt de Comando (CMD):

🔹 **Criar uma tarefa (POST)**

curl -X POST http://127.0.0.1:5000/api/tasks -H "Content-Type: application/json" -d "{\"title\":\"Revisar backlog\",\"description\":\"Organizar entregas da sprint\"}"

🔹 **Listar tarefas (GET)**

curl http://127.0.0.1:5000/api/tasks

🔹 **Atualizar tarefa (PUT)**

curl -X PUT http://127.0.0.1:5000/api/tasks/1 -H "Content-Type: application/json" -d "{\"title\":\"Organizar backlog semanal (atualizado)\",\"description\":\"Adicionado novo item de revisão\",\"completed\":true}"

🔹 **Excluir tarefa (DELETE)**

curl -X DELETE http://127.0.0.1:5000/api/tasks/1

---

## 🧭 **Diagramas UML e Documentação**

Os diagramas UML estão localizados em /docs/uml/, representando a estrutura e o comportamento do sistema:

- 📘 diagrama_classe.png
- 📗 diagrama_casos_de_uso.png

Eles descrevem o relacionamento entre as entidades e o fluxo principal de operações do sistema.

---

## 📸 **Evidências de Execução**

As principais evidências estão localizadas em /docs/prints/, incluindo:

- 🗂️ kanban.png — Kanban (GitHub Projects com ≥10 cards)
- 🧾 commits_history.png — Histórico de commits (≥10 mensagens)
- 🧪 pytest_local.png — Execução dos testes locais
- ⚙️ flask_running.png — Servidor Flask em execução
- 🌐 api_browser.png — Exibição das tarefas no navegador
- 💻 api_terminal.png — Teste de rotas via terminal

Essas imagens comprovam o funcionamento completo do ciclo ágil e a execução correta de todos os requisitos.

---

## 🎥 **Vídeo Pitch**

🎬 Apresentação demonstrando:

- Funcionamento completo do sistema (CRUD);
- Aplicação das metodologias ágeis;
- Execução dos testes locais e no GitHub Actions;
- Evidências de mudança de escopo e conclusões finais.

📎 Link do vídeo: (adicionar aqui quando disponível)

---

## 💡 **Tecnologias Utilizadas**

- 🐍 Python 3.13
- 🔬 PyTest
- 🌐 Flask
- ⚙️ Git & GitHub
- 🚀 GitHub Actions (CI/CD)
- 🧩 Kanban (GitHub Projects)
- 💾 JSON (armazenamento local)

## 👨‍💻 **Autor**

Lucas Ferreira da Silva

Projeto desenvolvido como parte da disciplina de Software Engineering – EAD

Curso: Engenharia da Computação — 3º Semestre (UniFECAF)

📅 2025 — Todos os direitos reservados.

---

## 🏁 *Status Final do Projeto*

✅ Ambiente configurado

✅ Estrutura de pastas concluída

✅ Testes automatizados aprovados

✅ CI/CD funcional (GitHub Actions)

✅ Documentação teórica e roteiro do vídeo incluídos

✅ Prints e evidências anexadas

✅ Vídeo Gravado

---