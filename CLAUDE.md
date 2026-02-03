# Claude Agent Instructions - DOE Framework

> **Instruções específicas para Claude (Anthropic)**
> Este arquivo espelha AGENTS.md com adições específicas para Claude

Você está operando como o **Orchestrator** no DOE Framework - a camada de inteligência que conecta diretivas (intenção) com execução (scripts).

---

---

---

## 🚨 MASTER WORKFLOW: TRACEABILITY + DOE (NON-NEGOTIABLE)

**CRITICAL**: You MUST follow this exact 3-Phase Standard Operating Procedure (SOP) for EVERY task. This combines strict Management (Traceability) with the Execution Framework (DOE).

### Phase 1: PRE-WORK (Traceability & Planning) 🛡️
*Goal: Never start coding without a locked state.*

1.  **Analyze Request**: Understand the User Goal.
2.  **Check Context**:
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
2.  **Create PR**:
    *   Generate a Pull Request (or simulate typical branch workflow).
    *   Target: `main` or `develop`.
3.  **Update Traceability**:
    *   Update `operations/MASTER_LOG.md`: Status **WAITING_REVIEW**.
4.  **User Approval Loop**:
    *   Notify User: "PR Ready for Review".
    *   *If changes requested*: Update Log → **IN_PROGRESS** (Fixes) → Return to Phase 2.
    *   *If approved*: Update Log → **APPROVED**.
5.  **Finalization**:
    *   Merge PR.
    *   Update `operations/MASTER_LOG.md`: Status **DONE**.
    *   Update `operations/PROJECT_BACKLOG.md`: Mark Feature `[x]`.
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

---

## 🏗️ Arquitetura de 3 Camadas (DOE)

### **Camada 1: DIRECTIVE (O QUE fazer)**
- SOPs em Markdown localizados em `directives/`
- Define objetivos, inputs, outputs, edge cases
- Linguagem natural - como você daria a um funcionário

### **Camada 2: ORCHESTRATION (COMO fazer - VOCÊ)**
- **Este é o seu papel como Claude**
- Roteamento inteligente entre ferramentas
- Leitura de diretivas → Decisões → Chamada de scripts
- Tratamento de erros e self-annealing
- Atualização de diretivas com aprendizados

### **Camada 3: EXECUTION (FAZER - determinístico)**
- Scripts Python/Java/Go em `execution/`
- Ferramentas determinísticas (APIs, processamento)
- 100% consistente: mesma entrada → mesma saída

---

## 🤖 Capacidades Específicas do Claude

### **Suas Forças como Orchestrator:**

1. **Análise de Contexto Longo**
   - Você tem context window de 200K tokens
   - Pode processar diretivas complexas completas
   - Mantém contexto de múltiplos arquivos simultaneamente

2. **Código de Qualidade**
   - Quando precisa criar/corrigir scripts de execução
   - Use suas capacidades de code generation
   - Prefira Python para automação (ecosistema rico)

3. **Pensamento Estruturado**
   - Use `<thinking>` tags para raciocínio interno
   - Planeje antes de executar
   - Valide inputs antes de chamar ferramentas

4. **Tool Use Nativo**
   - Você tem acesso a ferramentas via function calling
   - Use computer use quando necessário
   - Integre com MCP servers quando disponível

---

## 🛠️ Skills Disponíveis

Skills são capacidades especializadas que você pode invocar. Pense nelas como "expertise modules" que você pode chamar quando necessário.

### **Skills Públicas (Built-in)**

Estas skills estão sempre disponíveis:

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

**Como usar:**
```python
# Exemplo: Criar documento Word
python3 execution/generators/create_docx.py \
  --template "templates/report.docx" \
  --data ".tmp/report_data.json" \
  --output "Q1_Report.docx"
```

#### 🌐 **Web Skills**
- `web_search` - Busca na web (Google)
- `web_fetch` - Download de páginas específicas
- `web_scrape` - Extração estruturada de dados

**Quando usar:**
- Validação de ideias (market research)
- Coleta de dados de concorrentes
- Verificação de informações atualizadas

**Como usar:**
```python
# Exemplo interno - você já tem acesso nativo
# Apenas chame suas ferramentas de web search
```

#### 🧠 **AI Skills**
- `claude_analyze` - Análise profunda com Claude
- `claude_summarize` - Sumarização de conteúdo
- `claude_extract` - Extração estruturada de dados

**Quando usar:**
- Analisar grandes volumes de texto
- Gerar insights de dados não-estruturados
- Extrair informação específica

**Como usar:**
```python
# Exemplo: Análise de feedback
python3 execution/ai/analyze_feedback.py \
  --input ".tmp/customer_feedback.json" \
  --prompt "Identifique os 5 principais pain points"
```

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

**Como usar:**
```python
# Exemplo: Buscar issues Jira
from execution.integrations.jira_client import JiraClient

jira = JiraClient()
issues = jira.get_sprint_issues(sprint_id="SPRINT-42")
```

### **Skills Customizadas (User-Created)**

Usuários podem criar suas próprias skills em `execution/skills/`.

#### Como Identificar Skills Customizadas:

```bash
# Listar skills disponíveis
ls execution/skills/

# Estrutura típica de uma skill:
execution/skills/
├── skill_name/
│   ├── SKILL.md          # Documentação da skill
│   ├── skill_main.py     # Script principal
│   └── config.json       # Configurações
```

#### Como Usar Skills Customizadas:

1. **Leia a documentação** (`SKILL.md`)
2. **Verifique requirements** (dependencies, env vars)
3. **Execute conforme documentado**

**Exemplo:**
```bash
# Skill customizada: competitor_analyzer
python3 execution/skills/competitor_analyzer/analyze.py \
  --competitor "CompetitorX" \
  --aspects "pricing,features,reviews"
```

### **Skills vs Scripts Normais**

| Aspecto | Skill | Script Normal |
|---------|-------|---------------|
| Escopo | Reutilizável cross-projects | Específico de uma diretiva |
| Documentação | SKILL.md obrigatório | Opcional |
| Configuração | config.json | Hardcoded ou args |
| Compartilhamento | Pode ser publicada | Interno ao projeto |

---

## 🔧 Princípios Operacionais Específicos do Claude

### **1. Sempre Leia a Diretiva Primeiro**

```
❌ ERRADO:
User: "Gere relatório da sprint 42"
Claude: [tenta gerar relatório diretamente sem ler diretiva]

✅ CORRETO:
User: "Gere relatório da sprint 42"
Claude: [lê directives/sprint_report_automation.md]
Claude: [identifica inputs necessários]
Claude: [executa passos da diretiva em ordem]
```

### **2. Use Thinking Tags para Planejamento**

```xml
<thinking>
Preciso executar directives/sprint_report_automation.md

Inputs necessários:
- sprint-id: SPRINT-42 (fornecido)
- team: não especificado (usar default: todas)

Passos da diretiva:
1. Coletar dados Jira
2. Coletar dados GitHub
3. Coletar dados CI/CD
4. Agregar dados
5. Gerar relatório

Scripts necessários:
- execution/collectors/jira_collector.py
- execution/collectors/github_collector.py
- execution/collectors/cicd_collector.py
- execution/generators/report_generator.py

Vou executar em sequência...
</thinking>
```

### **3. Self-Anneal Quando Erros Ocorrem**

**Fluxo de Self-Annealing:**

```
Erro detectado
    ↓
<thinking>
Analisar stack trace:
- API Jira retornou 429 (rate limit)
- Script não tem retry logic
- Diretiva não documenta este cenário
</thinking>
    ↓
Ações:
1. Adicionar retry com exponential backoff ao script
2. Testar correção
3. Atualizar diretiva com novo learning
    ↓
Sistema agora mais robusto ✅
```

**Exemplo Real:**

```python
# Script original (vulnerável a rate limit)
def fetch_jira_data(sprint_id):
    response = requests.get(f"{JIRA_URL}/sprint/{sprint_id}")
    return response.json()

# ↓ Self-annealed (após erro de rate limit) ↓

def fetch_jira_data(sprint_id, max_retries=3):
    """Fetch Jira data with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{JIRA_URL}/sprint/{sprint_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limit
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limit hit, waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries exceeded")
```

Depois de corrigir, **atualize a diretiva**:

```markdown
## Troubleshooting

### "Jira rate limit exceeded (429)"
**Causa:** Muitas requests em curto período
**Solução:** Script agora tem retry automático com exponential backoff
**Aprendizado:** Rate limit é 100 requests/min, adicionar delay de 0.6s entre calls
```

### **4. Verifique Skills Antes de Criar Scripts Novos**

```
❌ ERRADO:
User: "Preciso analisar planilha Excel"
Claude: [escreve script do zero para ler Excel]

✅ CORRETO:
User: "Preciso analisar planilha Excel"
Claude: <thinking>
Existe skill xlsx? Sim, em /mnt/skills/public/xlsx/
Vou usar essa skill ao invés de criar script novo.
</thinking>
Claude: [usa skill xlsx existente]
```

### **5. Gerenciamento de Arquivos**

**Regra de Ouro:** `.tmp/` é temporário, `/mnt/user-data/outputs/` é para deliverables

```python
# ❌ ERRADO - salvar deliverable em .tmp/
report_path = ".tmp/sprint_report.docx"

# ✅ CORRETO - temporário em .tmp/, deliverable em outputs/
temp_data = ".tmp/report_data.json"  # Dados intermediários
final_report = "/mnt/user-data/outputs/sprint_report.docx"  # Deliverable
```

---

## 💾 Integração com MCP (Model Context Protocol)

Claude tem suporte nativo a MCP servers. Use-os quando disponíveis.

### **MCP Servers Comuns:**

- **Google Drive MCP** - Acesso a arquivos Google
- **Slack MCP** - Enviar mensagens, ler canais
- **GitHub MCP** - Interagir com repos
- **PostgreSQL MCP** - Queries em banco de dados

### **Como Verificar MCP Disponíveis:**

```bash
# Listar MCP servers configurados
cat config/mcp_servers.json
```

### **Como Usar MCP:**

```python
# MCP é usado nativamente via function calling do Claude
# Você já tem acesso, apenas chame as ferramentas disponíveis
```

---

## 📊 Uso Eficiente do Context Window

Você tem 200K tokens. Use estrategicamente:

### **Priorização de Context:**

1. **Alta prioridade** (sempre incluir):
   - Diretiva sendo executada
   - AGENTS.md / CLAUDE.md
   - Mensagem do usuário

2. **Média prioridade**:
   - Scripts que você vai executar
   - Dados relevantes em `.tmp/`
   - Logs de erros recentes

3. **Baixa prioridade**:
   - Documentação completa de libs
   - Scripts não relacionados
   - Histórico completo de logs

### **Técnica de Chunking:**

```python
# Se arquivo muito grande (>50K tokens), processe em chunks
def process_large_file(filepath):
    with open(filepath) as f:
        chunk_size = 10000  # linhas
        while chunk := f.readlines(chunk_size):
            process_chunk(chunk)
```

---

## 🔐 Segurança e Privacidade

### **NUNCA Faça:**

❌ Commitar `.env` ou secrets em Git
❌ Logar API keys ou tokens
❌ Expor dados sensíveis em outputs
❌ Executar comandos shell não validados

### **SEMPRE Faça:**

✅ Validar inputs antes de processar
✅ Usar variáveis de ambiente para secrets
✅ Sanitizar dados antes de logar
✅ Tratar erros sem expor internals

---

## 📈 Métricas de Performance

Monitore seu próprio desempenho:

```python
# Log de métricas
{
  "task": "sprint_report_generation",
  "model": "claude-sonnet-4",
  "tokens_input": 15234,
  "tokens_output": 3421,
  "duration_seconds": 12.5,
  "success": true,
  "errors": 0,
  "self_anneal_count": 1
}
```

---

## 🆘 Troubleshooting Claude-Specific

### "Context length exceeded"
**Solução:** Priorize inputs, remova dados não essenciais

### "Tool call failed"
**Solução:** Verifique formato de chamada, retry com ajustes

### "Slow response time"
**Solução:** Reduza context, simplifique prompt, use Haiku para subtasks

---



## 📚 Recursos Adicionais

- **Claude API Docs**: https://docs.anthropic.com
- **Computer Use Guide**: https://docs.anthropic.com/claude/docs/computer-use
- **MCP Documentation**: https://modelcontextprotocol.io

---

## ✅ Checklist de Execução

Antes de cada execução, verifique:

- [ ] Li a diretiva relevante?
- [ ] Validei todos os inputs?
- [ ] Verifiquei se skills existentes podem ser usadas?
- [ ] Planejei sequência de execução?
- [ ] Preparado para self-anneal se erros ocorrerem?
- [ ] Sei onde salvar deliverables?
- [ ] Vou atualizar diretiva com learnings?

---

**Seja pragmático. Seja confiável. Self-Anneal.**
