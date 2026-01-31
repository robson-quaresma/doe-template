# DOE Framework Template

> **D**irective → **O**rchestration → **E**xecution
> 
> Template para construir workflows agênticos confiáveis e escaláveis

---

## 📖 O Que é o DOE Framework?

DOE é uma arquitetura de separação de responsabilidades para workflows com IA, criada por Nick Saraev. Resolve o problema fundamental de LLMs serem probabilísticos enquanto negócios precisam de determinismo.

### O Problema

Quando você pede a uma IA para fazer tudo (scraping + processamento + análise + output):
- **90% de precisão por passo** = **59% de sucesso em 5 passos**
- Erros se acumulam exponencialmente
- Debugging é impossível
- Não é confiável para produção

### A Solução DOE

```
┌─────────────────────────────────────┐
│  DIRECTIVE (O QUE fazer)            │
│  - SOPs em Markdown                 │
│  - Sem código, apenas instruções    │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  ORCHESTRATION (COMO fazer)         │
│  - AI Agent (você, Claude)          │
│  - Decisões inteligentes            │
│  - Roteamento entre ferramentas     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  EXECUTION (FAZER)                  │
│  - Scripts determinísticos          │
│  - 100% consistente                 │
│  - Mesma entrada → Mesma saída      │
└─────────────────────────────────────┘
```

**Resultado:** Sistema confiável que self-anneal (se auto-corrige) ao longo do tempo.

---

## 🚀 Quick Start

### 1. Clone/Copie este Template

```bash
# Estrutura básica
projeto/
├── directives/          # SOPs em Markdown
├── execution/           # Scripts Python/Java/Go
├── .tmp/               # Arquivos temporários (git ignored)
├── AGENTS.md           # Instruções para o AI Agent
├── .env.example        # Template de variáveis de ambiente
└── requirements.txt    # Dependências Python
```

### 2. Setup Inicial

```bash
# Criar ambiente virtual Python
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas credenciais
```

### 3. Criar Sua Primeira Diretiva

Copie `directives/TEMPLATE.md` e adapte:

```bash
cp directives/TEMPLATE.md directives/meu_processo.md
```

Edite `meu_processo.md`:
- Defina objetivo claro
- Liste inputs necessários
- Especifique ferramentas/scripts
- Defina Definition of Done
- Documente edge cases

### 4. Criar Scripts de Execução (se necessário)

Se sua diretiva precisa de scripts novos:

```bash
# Criar script Python
touch execution/meu_script.py
chmod +x execution/meu_script.py
```

Estrutura básica:
```python
#!/usr/bin/env python3
"""
Descrição clara do que o script faz.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    # Lógica determinística aqui
    pass

if __name__ == "__main__":
    main()
```

### 5. Executar com AI Agent

Forneça ao AI Agent (Claude) o arquivo `AGENTS.md` como contexto:

```
Prompt: "Leia directives/meu_processo.md e execute o processo com os 
seguintes inputs: [seus inputs aqui]"
```

O agent vai:
1. Ler a diretiva
2. Validar inputs
3. Executar scripts na ordem correta
4. Lidar com erros (self-annealing)
5. Retornar resultados

---

## 📂 Estrutura de Diretórios

```
seu-projeto/
│
├── directives/                    # 📋 SOPs (Diretivas)
│   ├── TEMPLATE.md               # Template genérico
│   ├── sprint_report_automation.md  # Exemplo: relatório de sprint
│   └── [suas_diretivas].md
│
├── execution/                     # ⚙️ Scripts de Execução
│   ├── utils/                    # Utilitários reutilizáveis
│   │   ├── jira_client.py
│   │   ├── github_client.py
│   │   └── gdocs_helper.py
│   │
│   ├── collectors/               # Scripts de coleta de dados
│   │   ├── jira_collector.py
│   │   └── github_collector.py
│   │
│   ├── generators/               # Scripts de geração de output
│   │   └── report_generator.py
│   │
│   └── sprint_report_generator.py  # Exemplo completo
│
├── .tmp/                         # 🗂️ Arquivos Temporários
│   ├── data/                    # Dados temporários
│   ├── charts/                  # Gráficos gerados
│   └── logs/                    # Logs de execução
│   # ⚠️ NUNCA commitar .tmp/
│
├── templates/                    # 📄 Templates de Documentos
│   ├── report_template.docx
│   └── presentation_template.pptx
│
├── config/                       # ⚙️ Configurações
│   └── settings.yaml
│
├── .env                          # 🔐 Variáveis de Ambiente (SECRET)
├── .env.example                  # Template de .env
├── .gitignore                    # Git ignore
├── requirements.txt              # Dependências Python
├── AGENTS.md                     # 🤖 Instruções para AI Agent
└── README.md                     # Este arquivo
```

---

## 💡 Exemplos de Uso

### Exemplo 1: Relatório de Sprint

**Diretiva:** `directives/sprint_report_automation.md`

**Execução:**
```bash
python3 execution/sprint_report_generator.py \
  --sprint-id "SPRINT-42" \
  --team "platform"
```

**Output:**
- Google Doc com métricas de sprint
- Notificação no Slack
- Log em `.tmp/logs/`

### Exemplo 2: Análise de Concorrentes (SaaS)

**Diretiva:** `directives/competitor_analysis.md`

**Processo:**
1. Web research sobre concorrentes
2. Scraping de features e pricing
3. Análise com Claude
4. Geração de relatório comparativo

### Exemplo 3: Automação de Code Review

**Diretiva:** `directives/code_review_automation.md`

**Processo:**
1. Buscar PRs pendentes no GitHub
2. Análise estática (linter, security scan)
3. Review com Claude (sugestões de melhoria)
4. Postar comentários no PR

---

## 🛠️ Tecnologias Suportadas

### Backend/Scripts
- **Python** ✅ (recomendado para IA/automação)
- **Java/Spring Boot** (para sistemas robustos)
- **Go** (para alta performance)
- **Node.js** (para integrações web)

### Integrações
- **Jira** - Project management
- **GitHub/GitLab** - Source control
- **Google Workspace** - Docs, Sheets, Drive
- **Slack** - Notificações
- **Anthropic Claude** - AI analysis
- **Firebase** - Backend para SaaS

---

## 📊 Self-Annealing (Auto-Correção)

O sistema melhora automaticamente ao longo do tempo:

```
Erro encontrado
    ↓
AI Agent lê stack trace
    ↓
Identifica causa raiz
    ↓
Corrige script
    ↓
Testa correção
    ↓
Atualiza diretiva com aprendizado
    ↓
Sistema agora mais robusto ✅
```

**Exemplo Real:**

```
1ª Execução: Rate limit da API Jira
   → Agent adiciona retry com backoff
   → Atualiza diretiva: "Use exponential backoff"

2ª Execução: Dados malformados
   → Agent adiciona validação
   → Atualiza diretiva: "Validar schema antes de processar"

3ª Execução: Tudo funciona ✅
   → Sistema agora resiliente
```

---

## ⚡ Boas Práticas

### Para Diretivas

✅ **FAÇA:**
- Seja específico sobre inputs/outputs
- Defina Definition of Done clara
- Documente edge cases conhecidos
- Inclua exemplos de uso
- Mantenha atualizado (living document)

❌ **NÃO FAÇA:**
- Colocar código na diretiva
- Ser vago sobre objetivos
- Esquecer de documentar aprendizados
- Criar diretivas duplicadas

### Para Scripts de Execução

✅ **FAÇA:**
- Scripts atômicos (fazem UMA coisa bem)
- Determinísticos (mesma entrada → mesma saída)
- Logging detalhado
- Tratamento de erros robusto
- Validação de inputs
- Uso de type hints (Python)

❌ **NÃO FAÇA:**
- Scripts que tentam fazer tudo
- Hardcoded secrets/credentials
- Ignorar erros silenciosamente
- Deixar de documentar

### Para Organização

✅ **FAÇA:**
- Usar `.tmp/` para intermediários
- Cloud storage para deliverables
- Git para código e diretivas
- .env para secrets
- Logs para debugging

❌ **NÃO FAÇA:**
- Commitar `.tmp/` ou `.env`
- Deixar secrets no código
- Versionar outputs finais
- Ignorar logs

---

## 🔐 Segurança

### Checklist de Segurança

- [ ] `.env` está no `.gitignore`
- [ ] Nenhum secret no código fonte
- [ ] Tokens têm permissões mínimas necessárias
- [ ] Rotação regular de credentials
- [ ] Logs não expõem dados sensíveis
- [ ] Validação de inputs contra injection
- [ ] HTTPS para todas as APIs
- [ ] Autenticação OAuth quando possível

### Gerenciamento de Secrets

**Desenvolvimento:**
```bash
# .env local (nunca commitar)
ANTHROPIC_API_KEY=sk-ant-xxx
JIRA_TOKEN=xxx
```

**Produção:**
- AWS Secrets Manager
- Google Secret Manager
- Azure Key Vault
- HashiCorp Vault

---

## 🐛 Troubleshooting

### "ModuleNotFoundError"
```bash
# Ativar venv
source venv/bin/activate
# Reinstalar dependências
pip install -r requirements.txt
```

### "Authentication failed"
```bash
# Verificar .env
cat .env | grep API_KEY
# Regenerar token no serviço
```

### "Permission denied"
```bash
# Tornar script executável
chmod +x execution/script.py
```

### Scripts não executam
```bash
# Verificar shebang
head -1 execution/script.py
# Deve ser: #!/usr/bin/env python3

# Verificar Python path
which python3
```

---

## 📈 Métricas de Sucesso

Acompanhe estas métricas para avaliar sua implementação:

| Métrica | Meta | Como Medir |
|---------|------|------------|
| Taxa de sucesso | >95% | Execuções OK / Total |
| Tempo médio | Definir por processo | Timestamps nos logs |
| Intervenções manuais | Decrescente | Count mensal |
| ROI de tempo | >10x | Tempo antes vs depois |
| Satisfação | 4+/5 | Feedback dos usuários |

---

## 🎯 Casos de Uso Recomendados

### Para Engineering Managers
- ✅ Relatórios de sprint automatizados
- ✅ Análise de métricas de equipe
- ✅ Compilação de status reports
- ✅ Onboarding de novos membros
- ✅ Documentação técnica

### Para Desenvolvimento SaaS
- ✅ Validação de ideias (market research)
- ✅ Análise de concorrentes
- ✅ Content marketing automation
- ✅ User feedback processing
- ✅ API testing automation

### Para Produtividade Pessoal
- ✅ Email processing e triagem
- ✅ Organização GTD
- ✅ Research e summarization
- ✅ Meeting prep automation
- ✅ Personal analytics

---

## 🔗 Recursos Adicionais

### Documentação
- [Nick Saraev - Agentic Workflows Guide](https://nicksaraev.com)
- [Anthropic Claude API Docs](https://docs.anthropic.com)
- [LangChain Documentation](https://python.langchain.com)

### Comunidades
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
- [LangChain Discord](https://discord.gg/langchain)
- [Anthropic Discord](https://discord.gg/anthropic)

### Cursos
- Agentic AI Workflows (Nick Saraev)
- Building with Claude (Anthropic)
- LangChain Masterclass

---

## 🤝 Contribuindo

Este é seu template! Adapte e melhore conforme suas necessidades:

1. **Fork/Clone** este template
2. **Customize** para seu contexto
3. **Documente** seus aprendizados
4. **Compartilhe** com sua equipe

---

## 📝 License

Este template é baseado no trabalho de Nick Saraev e é disponibilizado para uso pessoal e comercial.

---

## 💬 Suporte

**Criado para:** Quaresma (Engineering Manager @ Equifax Brasil)
**Baseado em:** Nick Saraev's DOE Framework
**Data:** 2024-01-30

Para dúvidas ou sugestões:
- Issues neste repo
- Email: [seu email]
- LinkedIn: [seu perfil]

---

**Próximos Passos:**

1. [ ] Configurar `.env` com suas credenciais
2. [ ] Instalar dependências (`pip install -r requirements.txt`)
3. [ ] Criar sua primeira diretiva
4. [ ] Executar exemplo de sprint report
5. [ ] Iterar e melhorar (self-anneal!)

**Boa automação! 🚀**
