# Agent Instructions - DOE Framework

> **Arquitetura DOE (Directive → Orchestration → Execution)**
> Sistema de separação de responsabilidades para workflows agênticos confiáveis

Você opera em uma arquitetura de 3 camadas que separa responsabilidades para maximizar confiabilidade. LLMs são probabilísticos, mas a maioria da lógica de negócio é determinística e requer consistência. Este sistema resolve essa incompatibilidade.

---

## 🎯 COMMUNICATION GUIDELINES (MANDATORY)

**CRITICAL**: Be concise and executive in ALL responses.

### Response Style Requirements:
- ✅ **Direct and actionable** - Get to the point immediately
- ✅ **Minimal words** - Use shortest clear phrasing
- ✅ **No fluff** - Avoid unnecessary explanations or repetition
- ✅ **Structured** - Use bullets, tables, code blocks for clarity
- ✅ **Token-efficient** - Every word must add value
- ❌ **No verbose introductions** - Start with the answer
- ❌ **No excessive formatting** - Only what aids understanding
- ❌ **No repeated information** - Say it once clearly

### Examples:

**❌ BAD (Verbose)**:
```
I understand that you want to implement a new feature for the application.
This is a great idea and I think we should definitely proceed with this.
Let me explain what I'm going to do step by step. First, I will create
a new branch for this feature...
```

**✅ GOOD (Concise)**:
```
Creating feature branch and implementing. Steps:
1. Branch: `feature/new-feature`
2. Files: `src/component.tsx`, `src/service.ts`
3. PR ready in ~10min
```

---

---

## 🔄 MASTER WORKFLOW: TRACEABILITY + DOE (NON-NEGOTIABLE)

**CRITICAL**: You MUST follow this exact 3-Phase Standard Operating Procedure (SOP) for EVERY task. This combines strict Management (Traceability) with the Execution Framework (DOE).

### Phase 1: PRE-WORK (Traceability & Planning) 🛡️
*Goal: Never start coding without a locked state.*

0.  **Sync First (CRITICAL)**:
    *   **Action**: Run `git checkout main && git pull origin main` to ensure you are on the latest verified state.
    *   **Validaton**: Verify that `operations/MASTER_LOG.md` matches the remote version.

1.  **Analyze Request**: Understand the User Goal.
2.  **Check Context**:
    *   **PR Status Validation (MANDATORY)**:
        *   Identify tasks in `operations/MASTER_LOG.md` that are **NOT** `DONE` (e.g., `WAITING_REVIEW`, `IN_PROGRESS`).
        *   If the task has an associated PR #, check its status (`gh pr view <PR_NUMBER>`).
        *   **If Open**: Status remains active (`IN_PROGRESS` or `WAITING_REVIEW`).
        *   **If Merged/Closed**: The task is **DONE**. Update `MASTER_LOG.md` immediately.
    *   Read `operations/MASTER_LOG.md` (What was the last action?).
    *   Read `operations/PROJECT_BACKLOG.md` (Where does this fit?).
3.  **Plan Strategy**:
    *   **Existing Plan**: Check `operations/features/` for an active plan file.
    *   **New Task**: Create a new plan in `operations/features/` (e.g., `operations/features/feature_X/implementation_plan.md`).
4.  **Lock State**:
    *   Update `operations/MASTER_LOG.md`:
        *   **Status**: `IN_PROGRESS`
        *   **Link**: Path to the active Plan file.
        *   **Start**: Current Timestamp.

### Phase 2: EXECUTION (The DOE Loop) 🧠
*Goal: Deterministic execution via the DOE Framework.*

1.  **Select Directive**:
    *   Locate relevant SOP in `directives/` (e.g., `directives/sprint_report.md`).
    *   *If none exists*: Create a new Directive first.
2.  **Orchestrate**:
    *   Read the Directive.
    *   Validate Inputs (using Multimodal capabilities if needed).
    *   Plan the tool execution order.
3.  **Execute (DOE)**:
    *   Run scripts in `execution/` or standard Skills.
    *   **Self-Annealing**: If error -> Fix Script -> Update Directive -> Retry.
4.  **Security Check**:
    *   Ensure NO secrets are hardcoded (use `.env`).
    *   Ensure configs are in `config/`.
    *   Ensure architecture is clean (DDD).

### Phase 3: REVIEW & HANDOFF (The Quality Gate) 🏁
*Goal: Ensure quality and user approval before merging.*

1.  **Self-Correction**:
    *   Run linters/tests.
    *   Verify code against constraints (SOPs).
2.  **Create PR (NON-NEGOTIABLE - ABSOLUTELY MANDATORY)**:
    *   ⚠️ **CRITICAL RULE**: **NEVER EVER commit directly to `main` branch**
    *   ⚠️ **CRITICAL RULE**: **EVERY file change REQUIRES a Pull Request** - even a single character change
    *   ⚠️ **CRITICAL RULE**: **NO EXCEPTIONS** - documentation, logs, code, configs - ALL require PR
    *   **Why**: PRs maintain history, enable review, and prevent accidental mistakes
    *   **Process**:
        1. Create a feature branch (e.g., `docs/update-master-log`, `fix/button-color`)
        2. Make changes on the feature branch
        3. Commit changes to feature branch
        4. Push feature branch to remote
        5. Create Pull Request targeting `main`
        6. Wait for user approval
        7. User merges PR (NOT the agent)
    *   **Output**: You MUST provide the direct Link to the PR in your final response.
    *   **Conflict Resolution (MANDATORY)**:
        1. BEFORE creating PR, check for conflicts: `gh pr create` then `gh pr view <PR#> --json mergeable`
        2. If `mergeable: CONFLICTING`, you MUST resolve immediately:
           - Pull latest main: `git pull origin main`
           - Resolve conflicts in affected files
           - Commit resolution: `git add . && git commit`
           - Push: `git push`
        3. NEVER deliver PR to user with unresolved conflicts
        4. Only notify user when PR status is `mergeable: MERGEABLE`
    *   **Sync**: Ensure `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` are always synchronized.
    *   Target: `main` or `develop`.
3.  **Update Traceability**:
    *   Update `operations/MASTER_LOG.md`: Status **WAITING_REVIEW**.
4.  **User Approval Loop**:
    *   Notify User: "PR Ready for Review".
    *   *If changes requested*: Update Log → **IN_PROGRESS** (Fixes) → Return to Phase 2.
    *   *If approved*: User merges PR.
5.  **Finalization (CRITICAL - Requires NEW PR)**:
    *   ⚠️ After PR is merged, you MUST create a NEW PR to finalize:
        1. Create new branch: `docs/finalize-release-X`
        2. Update `operations/MASTER_LOG.md`: Status **DONE**
        3. Update `operations/PROJECT_BACKLOG.md`: Mark Feature `[x]`
        4. Commit and push
        5. Create PR with title "Finalize Release X"
        6. Wait for user approval
    *   **Why**: Maintains traceability - other agents/sessions need to see completion status
    *   **Never**: Update MASTER_LOG to DONE without a PR

### 📝 Standardized Statuses (`operations/MASTER_LOG.md`)
*   `TODO`: Not started.
*   `IN_PROGRESS`: Active work.
*   `BLOCKED`: Waiting on external dependency.
*   `WAITING_REVIEW`: PR ready, waiting for user.
*   `APPROVED`: User gave green light.
*   `DONE`: Completed & Merged.

---

## 🛡️ SECURITY & ARCHITECTURE STANDARDS (NON-NEGOTIABLE)

### 1. Secrets Management
*   **Use `.env`**: ALL API keys, passwords, and sensitive tokens MUST be stored in `.env`.
*   **Directives**: NEVER hardcode secrets in scripts or code.
*   **Verification**: Ensure `.env` is listed in `.gitignore`.

### 2. Configuration Management
*   **Location**: ALL configuration files (e.g., `config.json`, `settings.yaml`) MUST be located in the `config/` directory.
*   **Root Hygiene**: Do NOT clutter the root directory with config files.

### 3. Architecture Principles
*   **Clean Architecture**: Follow DDD (Domain-Driven Design) principles. Separate Domain, Application, and Infrastructure layers.
*   **Professional Output**: Ensure code is clean, modular, and testable.

### 4. Design & UI Standards
*   **Directive**: You MUST read `directives/product/design_system.md` before making ANY UI changes.
*   **Mandatory**: Use standard `Ionicons`, `Slate/Gray` palette, and `Flat/Solid` components.
*   **Consistency**: Do not introduce new colors or styles without updating the Design Directive first.

---

## 🚀 DEVELOPMENT PHILOSOPHY (CRITICAL - NEW REQUIREMENTS)

### 1. Incremental Releases Strategy (MANDATORY)
**Goal**: NEVER break user experience. Deploy small, testable increments.

#### **Rule: Small Releases Only**
- **Maximum Scope**: 1-2 problems per release
- **Maximum Duration**: 3-7 days per release
- **Rollback**: Must be easy if issues arise
- **Testing**: Each release fully tested independently

#### **Breaking Down Large Features**
If a feature requires > 7 days:
1. **STOP**: Do NOT implement as single release
2. **ANALYZE**: Identify logical sub-features
3. **PLAN**: Create multiple releases (e.g., 2.0.1, 2.0.2, 2.0.3)
4. **EXECUTE**: One sub-release at a time
5. **VALIDATE**: User approval between sub-releases

**Example - BAD (Monolithic)**:
```
❌ Release 2.0: Complete DDD Refactoring (30 days, 100+ files)
   - High risk
   - Hard to test
   - Impossible to rollback partially
   - User experience broken for weeks
```

**Example - GOOD (Incremental)**:
```
✅ Release 2.0.1: DDD Foundation (3 days, 10 files)
   - Low risk
   - Easy to test
   - Can rollback completely
   - User experience unchanged

✅ Release 2.0.2: Data Layer Migration (5 days, 15 files)
   - Builds on 2.0.1
   - Testable independently
   - User experience still works

✅ Release 2.0.3: Use Cases Migration (5 days, 20 files)
   ...and so on
```

### 2. Test-Driven Development (NON-NEGOTIABLE)
**Rule**: EVERY code change MUST have tests. NO EXCEPTIONS.

#### **TDD Workflow (MANDATORY)**
```
1. Write Test (RED)
   ↓
2. Write Minimal Code to Pass (GREEN)
   ↓
3. Refactor & Improve (REFACTOR)
   ↓
4. Run ALL Tests
   ↓
5. Commit ONLY if 100% passing
```

#### **Test Coverage Requirements**
- **Domain Layer**: 90%+ coverage (business logic is critical)
- **Data Layer**: 80%+ coverage (repositories, data sources)
- **Presentation Layer**: 70%+ coverage (view models, screens)
- **E2E Tests**: All critical user flows

#### **Test Types (By Layer)**

**Unit Tests** (`src/__tests__/unit/`)
- **Domain**: Entities, Value Objects, Use Cases
- **Data**: Models, DTOs (serialization/deserialization)
- **Presentation**: ViewModels (logic without UI)

**Integration Tests** (`src/__tests__/integration/`)
- **Data**: Repository implementations (with Firestore emulator)
- **Services**: API clients (with mock servers)

**E2E Tests** (`src/__tests__/e2e/`)
- **Critical Flows**: Login, Add Food, View History
- **Tool**: Detox (React Native)

#### **Before Committing (Quality Gate)**
```bash
# MANDATORY checks before ANY commit
npm run test          # All tests must pass (100%)
npm run lint          # Zero warnings
npm run format        # Code formatted
npm run type-check    # Zero TypeScript errors
```

#### **No Tests = No Merge**
- PRs without tests will be **REJECTED**
- "I'll add tests later" is **NOT acceptable**
- Tests are **NOT optional** - they ARE the code

### 3. Domain-Driven Design (DDD) - Architectural Target
**Status**: Current project does NOT follow DDD (mixed responsibilities).
**Goal**: Migrate to DDD incrementally (Release 2.0.x series).

#### **Current Problems**
- Business logic mixed with UI code
- Services doing everything (data + logic + transformation)
- Hard to test (everything coupled)
- Unclear boundaries (where does a feature start/end?)

#### **DDD Principles (Target State)**

**Domain Layer** (Pure Business Logic)
- **Entities**: Core objects (Food, Meal, User Profile)
- **Value Objects**: Immutable values (MacroNutrient, ServingSize)
- **Use Cases**: Business operations (AddFoodToMeal, CalculateNutrition)
- **Repositories**: Interfaces ONLY (contracts, not implementations)

**Data Layer** (Infrastructure)
- **Data Sources**: Firestore, APIs, Cache
- **DTOs**: Data Transfer Objects (Firestore documents)
- **Repository Implementations**: Concrete implementations of domain interfaces

**Presentation Layer** (UI)
- **Screens**: Pure UI (minimal logic)
- **ViewModels**: Presentation logic (MVVM pattern)
- **Components**: Reusable UI elements

#### **Migration Strategy**
- **DO NOT** refactor everything at once (breaks user experience)
- **DO** migrate incrementally (Release 2.0.1 → 2.0.5)
- **SEE**: `operations/features/release_2_0_ddd_refactoring.md` for detailed plan

### 4. Definition of Done (Per Release)

A release is DONE when ALL of these are met:

#### **Code Quality**
- [ ] TypeScript: Zero errors
- [ ] ESLint: Zero warnings
- [ ] Prettier: All files formatted
- [ ] No console.log (use proper logger)
- [ ] No commented code (delete or document why)

#### **Testing**
- [ ] Unit tests: 90%+ coverage (domain layer)
- [ ] Integration tests: All repos tested
- [ ] E2E tests: Critical flows passing
- [ ] Manual testing: Smoke test entire app

#### **Documentation**
- [ ] README updated (if architecture changed)
- [ ] CHANGELOG updated
- [ ] API docs (if new interfaces added)
- [ ] Migration guide (if breaking changes)

#### **Performance**
- [ ] No regression in load times
- [ ] No memory leaks (profiler check)
- [ ] Smooth animations (60fps)

#### **Security**
- [ ] No secrets in code
- [ ] Firestore rules validated
- [ ] Input validation on all user inputs

#### **Deployment**
- [ ] Build succeeds (iOS + Android)
- [ ] App launches without crashes
- [ ] No console errors/warnings

### 5. Workflow Summary (Per Task)

```
1. PRE-WORK
   - Sync with main branch
   - Read MASTER_LOG / PROJECT_BACKLOG
   - Create small, focused plan (max 7 days)

2. IMPLEMENTATION (TDD)
   - Write test FIRST (RED)
   - Write minimal code (GREEN)
   - Refactor (REFACTOR)
   - Repeat for each function/feature

3. QUALITY GATE
   - Run all tests (100% passing)
   - Run linters (zero warnings)
   - Format code
   - Type check

4. PR & REVIEW
   - Create PR with tests
   - Wait for user approval
   - Merge ONLY after approval

5. DEPLOY
   - Small release (users won't notice)
   - Monitor for issues
   - Roll back if needed (easy with small changes)
```

### 6. Red Flags (STOP and Ask User)

**STOP immediately if:**
- Release scope > 7 days
- > 50 files touched in single PR
- Tests would take > 1 week to write
- Architecture change without plan
- "We'll add tests later" is suggested

**ASK user for approval before:**
- Major refactoring (DDD migration)
- Breaking changes to public APIs
- New dependencies (npm packages)
- Infrastructure changes (Firebase rules, etc.)

---

## 🏗️ Arquitetura de 3 Camadas (DOE)

### **Camada 1: DIRECTIVE (O QUE fazer)**
- SOPs (Standard Operating Procedures) escritos em Markdown
- Localizados em: `directives/`
- Definem: objetivos, inputs, tools/scripts a usar, outputs, edge cases
- Instruções em linguagem natural, como você daria a um funcionário de nível médio
- **NUNCA** contém código - apenas descrição do processo

### **Camada 2: ORCHESTRATION (COMO fazer - decisões)**
- **Este é VOCÊ** - Seu trabalho: roteamento inteligente
- Lê diretivas, chama ferramentas de execução na ordem correta, lida com erros
- Solicita esclarecimentos quando necessário, atualiza diretivas com aprendizados
- Você é a cola entre intenção (diretivas) e execução (scripts)
- **REGRA:** Você NÃO tenta fazer scraping, processamento pesado, ou lógica complexa sozinho
- Você lê `directives/tarefa.md` → identifica inputs/outputs → executa `execution/script.py`

### **Camada 3: EXECUTION (FAZER - trabalho determinístico)**
- Scripts determinísticos (Python, Java, Go, etc.) em `execution/`
- Variáveis de ambiente, tokens de API armazenados em `.env`
- Lidam com: chamadas de API, processamento de dados, operações de arquivo, interações com banco de dados
- Confiáveis, testáveis, rápidos
- **SEMPRE** preferir scripts a trabalho manual

---

## 📊 Por Que Isso Funciona

**Problema:** Se você faz tudo sozinho, erros se acumulam
- 90% de precisão por passo = 59% de sucesso em 5 passos
- LLMs são probabilísticos → mesma entrada pode gerar saídas diferentes

**Solução:** Empurre complexidade para código determinístico
- Scripts = 100% consistentes (mesma entrada → mesma saída)
- Agent = foco apenas em decisões de alto nível
- Resultado: sistema confiável e escalável

---

## ⚙️ Princípios Operacionais

### **1. Verifique ferramentas existentes primeiro**
Antes de escrever um script novo:
1. Verifique `execution/` conforme sua diretiva
2. Apenas crie novos scripts se nenhum existente atender a necessidade
3. Sempre pergunte antes de criar ferramentas duplicadas

### **2. Self-Annealing (Auto-Correção) quando algo quebra**
Quando encontrar erros:
1. Leia a mensagem de erro e stack trace
2. Corrija o script e teste novamente
   - **EXCETO:** se usar tokens/créditos pagos → confirme com usuário primeiro
3. Atualize a diretiva com o que aprendeu (limites de API, timing, edge cases)

**Exemplo de Self-Annealing:**
```
Erro: Rate limit de API atingido
↓
Você investiga a API → encontra endpoint batch
↓
Reescreve script para usar batch
↓
Testa e valida
↓
Atualiza diretiva com nova abordagem
```

### **3. Atualize diretivas conforme aprende**
Diretivas são documentos **vivos**. Quando você descobrir:
- Limitações de API
- Abordagens melhores
- Erros comuns
- Expectativas de timing

→ **ATUALIZE a diretiva**

**⚠️ IMPORTANTE:**
- NÃO crie ou sobrescreva diretivas sem perguntar
- Diretivas são seu conjunto de instruções
- Devem ser preservadas e melhoradas ao longo do tempo

---

## 🔄 Loop de Self-Annealing

Erros são oportunidades de aprendizado. Quando algo quebrar:

```
1. Corrija o problema
   ↓
2. Atualize a ferramenta/script
   ↓
3. Teste a ferramenta → garanta que funciona
   ↓
4. Atualize a diretiva para incluir novo fluxo
   ↓
5. Sistema agora é mais forte
```

Este loop torna o sistema mais resiliente a cada execução.

---

## 📁 Organização de Arquivos

### **Deliverables vs Intermediários:**

**Deliverables (Entregas Finais):**
- Google Sheets, Docs, Slides
- Planilhas Excel em cloud storage
- APIs publicadas
- Dashboards
- **Regra:** Acessíveis diretamente pelo usuário

**Intermediários (Temporários):**
- Arquivos temporários necessários durante processamento
- Dados raspados (scraped)
- Exports temporários
- Logs de processamento

### **Estrutura de Diretórios:**

```
projeto/
├── .tmp/                    # Arquivos intermediários (NUNCA commitar)
│   ├── scraped_data/       # Dados temporários de scraping
│   ├── processing/         # Arquivos em processamento
│   └── exports/            # Exports temporários
│
├── directives/             # SOPs em Markdown
│   ├── template.md        # Template de diretiva
│   ├── exemplo_api.md     # Exemplo: integração de API
│   └── exemplo_relatorio.md  # Exemplo: geração de relatório
│
├── execution/              # Scripts determinísticos
│   ├── utils/             # Utilitários reutilizáveis
│   ├── api_client.py      # Exemplo: cliente de API
│   └── report_generator.py # Exemplo: gerador de relatório
│
├── .env                    # Variáveis de ambiente e API keys
├── .gitignore             # Ignorar .tmp/, .env, credentials
├── requirements.txt        # Dependências Python
├── AGENTS.md              # Este arquivo
└── README.md              # Documentação do projeto
```

### **Princípio Chave:**
- Arquivos locais são APENAS para processamento
- Deliverables vivem em serviços cloud (Google Workspace, OneDrive, etc.)
- Tudo em `.tmp/` pode ser deletado e regenerado

---

## 🎯 Casos de Uso Recomendados

### **Para Engineering Manager (Equifax):**
- Automação de relatórios de sprint
- Análise de métricas de equipe
- Compilação de status reports
- Automação de processos de onboarding
- Geração de documentação técnica

### **Para Desenvolvimento SaaS (Qriterion):**
- Validação de ideias de produto (web research)
- Análise de concorrentes
- Geração de conteúdo para marketing
- Automação de testes de API
- Processamento de feedback de usuários

### **Para Produtividade Pessoal:**
- Processamento de emails
- Organização de tarefas GTD
- Pesquisa e sumarização de artigos
- Preparação de apresentações
- Análise de dados pessoais

---

## 🛠️ Skills (Capacidades Especializadas)

Skills são módulos de expertise que podem ser invocados quando necessário. Pense nelas como "ferramentas especializadas" que o agent pode usar.

### **Skills Públicas (Built-in)**

Estas skills estão sempre disponíveis no sistema:

#### 📄 **Document Skills**
- `docx` - Criação e edição de Word documents
- `xlsx` - Manipulação de planilhas Excel
- `pptx` - Geração de apresentações PowerPoint
- `pdf` - Leitura e criação de PDFs

**Quando usar:**
- Gerar relatórios formatados
- Criar apresentações automatizadas
- Processar planilhas de dados
- Extrair texto de PDFs

#### 🌐 **Web Skills**
- `web_search` - Busca na web
- `web_fetch` - Download de páginas específicas
- `web_scrape` - Extração estruturada de dados

**Quando usar:**
- Validação de ideias (market research)
- Coleta de dados de concorrentes
- Verificação de informações atualizadas

#### 🧠 **AI Skills**
- `claude_analyze` / `gemini_analyze` - Análise profunda
- `claude_summarize` / `gemini_summarize` - Sumarização
- `claude_extract` / `gemini_extract` - Extração estruturada

**Quando usar:**
- Analisar grandes volumes de texto
- Gerar insights de dados não-estruturados
- Extrair informação específica

#### 🔗 **Integration Skills**
- `jira_client` - Interação com Jira
- `github_client` - Operações no GitHub
- `slack_notify` - Notificações Slack
- `gdocs_client` - Google Docs/Sheets/Drive

**Quando usar:**
- Coletar dados de project management
- Analisar código e PRs
- Enviar notificações
- Criar deliverables em cloud

### **Skills Customizadas (User-Created)**

Usuários podem criar suas próprias skills em `execution/skills/`.

**Estrutura típica:**
```
execution/skills/
├── skill_name/
│   ├── SKILL.md          # Documentação
│   ├── skill_main.py     # Script principal
│   └── config.json       # Configurações
```

**Como usar skills customizadas:**
1. Leia a documentação (`SKILL.md`)
2. Verifique requirements (dependencies, env vars)
3. Execute conforme documentado

### **Skills vs Scripts Normais**

| Aspecto | Skill | Script Normal |
|---------|-------|---------------|
| Escopo | Reutilizável cross-projects | Específico de uma diretiva |
| Documentação | SKILL.md obrigatório | Opcional |
| Configuração | config.json | Hardcoded ou args |
| Compartilhamento | Pode ser publicada | Interno ao projeto |

**Regra:** Sempre verifique se existe skill para a tarefa antes de criar script novo!

---

## 📝 Sistema de CHANGELOG (Rastreabilidade)

Este projeto usa `CHANGELOG.md` para rastreabilidade de mudanças.

### Quando Consultar (Leitura Inteligente)

✅ **SEMPRE antes de modificar:**
- Diretivas existentes
- Skills existentes
- Scripts existentes

✅ **Técnicas de leitura eficiente:**
```bash
# Últimas 5-10 entradas apenas
head -30 CHANGELOG.md

# Por categoria específica
grep '[DIRECTIVE]' CHANGELOG.md
grep '[SKILL]' CHANGELOG.md
grep '[FIX]' CHANGELOG.md

# Por arquivo específico
grep 'nome-arquivo' CHANGELOG.md
```

❌ **NUNCA ler changelog completo** (desperdício de tokens!)

### Quando Atualizar (Escrita Concisa)

✅ **SEMPRE após criar/modificar:**
- Nova diretiva
- Nova skill
- Novo script importante
- Fix significativo

📝 **Formato (1 linha!):**
```
[CATEGORIA] Descrição (<50 chars) | path/arquivo
```

**Categorias:** `DIRECTIVE`, `SKILL`, `SCRIPT`, `DOC`, `FIX`, `CONFIG`

**Exemplo:**
```
[DIRECTIVE] Setup Firebase Project | directives/development/setup-firebase-project.md
[SKILL] WhatsApp Tester | execution/skills/whatsapp_tester/
[FIX] Encoding error em metrics | execution/operations/metrics_collector.py
```

📚 **Guia completo:** `CHANGELOG-AGENT-GUIDE.md`

---

## 📝 Como Começar

1. **Identifique uma tarefa repetitiva** que você faz frequentemente
2. **Consulte CHANGELOG** para ver se já existe algo similar
3. **Crie uma diretiva** em `directives/nome_tarefa.md` descrevendo o processo
4. **Verifique skills disponíveis** antes de criar ferramentas novas
5. **Identifique ferramentas** necessárias ou crie scripts em `execution/`
6. **Execute e itere** - deixe o sistema self-anneal
7. **Documente aprendizados** atualizando a diretiva
8. **Atualize CHANGELOG** com a mudança (1 linha concisa!)

---

## ⚡ Resumo

Você se posiciona entre:
- **Intenção humana** (diretivas)
- **Execução determinística** (scripts)

**Suas responsabilidades:**
✅ Ler instruções (diretivas)
✅ Tomar decisões (orquestração)
✅ Chamar ferramentas (execução)
✅ Lidar com erros (self-annealing)
✅ Melhorar continuamente o sistema

**Seja pragmático. Seja confiável. Self-Anneal.**

---

## 🔧 Stack Tecnológica Preferencial

Baseado no perfil do usuário:

**Backend/Scripts:**
- Python (para automação rápida e IA)
- Java/Spring Boot (para sistemas robustos)
- Go (para performance e concorrência)

**Frontend/Mobile (quando aplicável):**
- Flutter/Dart (apps mobile)
- React (web apps)

**Integrações Cloud:**
- Google Workspace APIs (Sheets, Docs, Drive)
- Firebase (auth, database, hosting)
- AWS/GCP (conforme necessidade)

**IA/ML:**
- Anthropic Claude API
- OpenAI API (quando necessário)
- LangChain (para pipelines complexos)
