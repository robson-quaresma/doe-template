# Sprint Report Automation

> Geração automatizada de relatório semanal de métricas de desenvolvimento

Gera relatório completo de sprint contendo métricas de velocity, code review, qualidade e deployment.

---

## 📋 Overview

Este processo automatiza a geração do relatório semanal de sprint, coletando dados de múltiplas fontes (Jira, GitHub, CI/CD) e compilando em um documento estruturado com análises e insights.

**Use este processo quando:**
- Final de sprint (toda sexta-feira)
- Preparação para sprint review/retrospectiva
- Solicitação de stakeholders por métricas atualizadas
- Avaliação de performance de equipe

**NÃO use quando:**
- Dados em tempo real são necessários (use dashboard ao vivo)
- Análise profunda de um único bug/feature específico

---

## 🎯 Objetivo

Gerar relatório de sprint consolidado em até 5 minutos, contendo:
- Velocity da sprint (pontos completados vs planejados)
- Code review metrics (tempo médio, PRs pendentes)
- Quality metrics (bugs, test coverage, hotfixes)
- Deployment frequency e success rate
- Bloqueios e dependências críticas

Output: Google Doc formatado + notificação no Slack

---

## 📥 Inputs (Entradas)

| Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
|-----------|------|-------------|-----------|---------|
| `--sprint-id` | String | Sim | ID da sprint no Jira | `SPRINT-42` |
| `--team` | String | Não | Nome da equipe (default: todas) | `platform` |
| `--include-graphs` | Boolean | Não | Incluir gráficos visuais (default: true) | `true` |
| `--notify-slack` | Boolean | Não | Enviar para Slack (default: true) | `true` |
| `--slack-channel` | String | Não | Canal do Slack (default: #eng-metrics) | `#platform-team` |

---

## 🔧 Ferramentas/Scripts

### Execução Completa (Recomendado)
```bash
python3 execution/sprint_report_generator.py \
  --sprint-id "SPRINT-42" \
  --team "platform" \
  --include-graphs true \
  --notify-slack true
```

### Execução Modular

**1. Coleta de dados do Jira:**
```bash
python3 execution/collectors/jira_collector.py --sprint-id "SPRINT-42"
# Output: .tmp/jira_data_SPRINT-42.json
```

**2. Coleta de dados do GitHub:**
```bash
python3 execution/collectors/github_collector.py --team "platform" --days 14
# Output: .tmp/github_data_platform.json
```

**3. Coleta de dados de CI/CD:**
```bash
python3 execution/collectors/cicd_collector.py --team "platform" --days 14
# Output: .tmp/cicd_data_platform.json
```

**4. Geração do relatório:**
```bash
python3 execution/generators/report_generator.py \
  --jira-data ".tmp/jira_data_SPRINT-42.json" \
  --github-data ".tmp/github_data_platform.json" \
  --cicd-data ".tmp/cicd_data_platform.json" \
  --template "templates/sprint_report_template.docx"
# Output: Google Doc URL
```

**5. Notificação (opcional):**
```bash
python3 execution/notifiers/slack_notifier.py \
  --message "Sprint 42 Report gerado" \
  --doc-url "https://docs.google.com/..." \
  --channel "#platform-team"
```

---

## 📤 Outputs (Saídas)

### Formato: Google Doc

**Estrutura do Relatório:**

```
SPRINT 42 - REPORT
Período: 20/01/2024 - 02/02/2024
Equipe: Platform Team

═══════════════════════════════════════

1. SPRINT OVERVIEW
   - Pontos planejados: 42
   - Pontos completados: 38 (90%)
   - Velocity média (4 sprints): 40
   - Status: ✅ On Track

2. SPRINT GOALS
   ✅ Migração de 50% dos serviços AS400 → GCP
   ✅ Implementação de monitoring avançado
   ⚠️ Refactoring do módulo de autenticação (80% completo)

3. CODE REVIEW METRICS
   - PRs merged: 45
   - Tempo médio de review: 6.2 horas ⬇️ (anterior: 8.1h)
   - PRs pendentes: 8
   - Top reviewers: @joao (12), @maria (10), @pedro (9)

4. QUALITY METRICS
   - Bugs em produção: 2 (severity: medium)
   - Test coverage: 82% ⬆️ (+3%)
   - Hotfixes: 0
   - Code quality score: 8.7/10

5. DEPLOYMENT METRICS
   - Deploys realizados: 18
   - Success rate: 94%
   - Rollbacks: 1
   - Deploy frequency: 1.3/dia

6. BLOCKERS & DEPENDENCIES
   ⚠️ Aguardando aprovação de infra para ambiente de staging
   ⚠️ Dependência externa: API de terceiros instável

7. TEAM HIGHLIGHTS
   🏆 Zero bugs críticos em produção
   🏆 Melhor tempo de code review do trimestre
   📈 3% de aumento em test coverage

8. ACTION ITEMS PARA PRÓXIMA SPRINT
   - [ ] Finalizar refactoring de autenticação
   - [ ] Implementar circuit breaker na API de terceiros
   - [ ] Revisar processo de deploy staging
```

### Schema de Dados (JSON intermediário)

```json
{
  "sprint": {
    "id": "SPRINT-42",
    "team": "platform",
    "period": {
      "start": "2024-01-20",
      "end": "2024-02-02"
    },
    "points": {
      "planned": 42,
      "completed": 38,
      "completion_rate": 0.90,
      "velocity_avg_4_sprints": 40
    }
  },
  "code_review": {
    "prs_merged": 45,
    "avg_review_time_hours": 6.2,
    "prs_pending": 8,
    "top_reviewers": [
      {"name": "joao", "count": 12},
      {"name": "maria", "count": 10},
      {"name": "pedro", "count": 9}
    ]
  },
  "quality": {
    "production_bugs": 2,
    "bug_severity": "medium",
    "test_coverage": 0.82,
    "hotfixes": 0,
    "code_quality_score": 8.7
  },
  "deployment": {
    "total_deploys": 18,
    "success_rate": 0.94,
    "rollbacks": 1,
    "deploy_frequency_per_day": 1.3
  },
  "blockers": [
    {
      "type": "infrastructure",
      "description": "Aguardando aprovação staging",
      "severity": "medium"
    },
    {
      "type": "external_dependency",
      "description": "API terceiros instável",
      "severity": "medium"
    }
  ]
}
```

---

## 🔄 Fluxo de Execução

### Passo 1: Validação de Inputs
- Verificar sprint-id existe no Jira
- Validar permissões de acesso às APIs
- Confirmar período da sprint

### Passo 2: Coleta Paralela de Dados
**Thread 1 - Jira:**
- Listar todas as issues da sprint
- Calcular story points (planejados vs completados)
- Identificar blockers e dependências

**Thread 2 - GitHub:**
- Buscar PRs do período
- Calcular tempo médio de review
- Identificar top reviewers

**Thread 3 - CI/CD:**
- Listar deployments do período
- Calcular success rate
- Identificar rollbacks

### Passo 3: Processamento e Análise
- Agregar dados de todas as fontes
- Calcular métricas derivadas (trends, averages)
- Identificar anomalias e highlights
- Gerar insights automáticos (usando Claude)

### Passo 4: Geração do Documento
- Aplicar template do Google Doc
- Inserir dados formatados
- Gerar gráficos (matplotlib → imagem → Google Doc)
- Aplicar formatação (cores, títulos, bullet points)

### Passo 5: Distribuição
- Salvar Doc com permissões compartilhadas
- Enviar notificação no Slack com link
- Registrar log de execução

---

## ⚠️ Edge Cases e Tratamento de Erros

### Caso 1: Sprint Incompleta
**Situação:** Relatório solicitado antes do fim da sprint
**Ação:**
- Adicionar disclaimer "Dados parciais - Sprint em andamento"
- Marcar métricas como "current status" não "final"
- Incluir data/hora de geração do relatório

### Caso 2: API Jira Indisponível
**Situação:** Timeout ou erro 500 da API Jira
**Ação:**
- Implementar retry com exponential backoff (3 tentativas)
- Se falhar, usar dados em cache (.tmp) da última execução bem-sucedida
- Adicionar warning no relatório: "Dados do Jira podem estar desatualizados"

### Caso 3: PRs sem Revisores Identificados
**Situação:** GitHub API retorna PRs sem reviewer assignado
**Ação:**
- Usar histórico de comments para inferir reviewers
- Se não possível, marcar como "Auto-merged" ou "No reviewer"
- Logar para investigação manual

### Caso 4: Dados de Múltiplas Equipes Misturados
**Situação:** Filtro de equipe não separa corretamente
**Ação:**
- Usar tags/labels do Jira para filtrar
- Cross-reference com GitHub teams
- Se ambíguo, incluir e marcar como "Shared"

---

## ✅ Definition of Done (DoD)

**Este processo está completo quando:**
- [x] Sprint-id validado no Jira
- [x] Dados coletados de todas 3 fontes (Jira, GitHub, CI/CD)
- [x] Métricas calculadas sem erros
- [x] Google Doc criado com todas seções preenchidas
- [x] Gráficos gerados e inseridos (se --include-graphs=true)
- [x] Documento compartilhado com permissões corretas
- [x] Notificação enviada no Slack (se --notify-slack=true)
- [x] Logs registrados em .tmp/logs/sprint_report_{sprint-id}.log
- [x] Nenhum erro crítico no processo (warnings são OK)

---

## 💰 Considerações de Custo

| Componente | Custo Estimado | Observações |
|------------|----------------|-------------|
| Jira API | $0.00 | Incluído no plano corporativo |
| GitHub API | $0.00 | Incluído no plano Enterprise |
| Claude API | ~$0.10 | Para geração de insights (~2k tokens) |
| Google Docs API | $0.00 | Gratuito |
| Matplotlib (local) | $0.00 | Processamento local |
| **Total por execução** | **~$0.10** | |

**Execuções mensais:** 4 (1 por sprint)
**Custo mensal:** ~$0.40

---

## 📦 Dependências

### Python Packages
```txt
requests==2.31.0
pandas==2.0.3
matplotlib==3.8.0
anthropic==0.8.1
google-api-python-client==2.100.0
google-auth-httplib2==0.1.1
google-auth-oauthlib==1.1.0
python-dotenv==1.0.0
jira==3.5.0
PyGithub==2.1.1
```

### Environment Variables
```bash
# .env
JIRA_URL=https://equifax.atlassian.net
JIRA_EMAIL=seu.email@equifax.com
JIRA_API_TOKEN=your_jira_token

GITHUB_TOKEN=ghp_your_github_token
GITHUB_ORG=equifax-brasil

ANTHROPIC_API_KEY=sk-ant-your_key

GOOGLE_CREDENTIALS_PATH=credentials.json

SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### External Services
- Jira Cloud API (REST v3)
- GitHub REST API v3
- Jenkins/CircleCI/GitLab CI API
- Anthropic Claude API
- Google Docs API v1
- Slack Incoming Webhooks

---

## 📂 Arquivos Relacionados

### Scripts de Execução
```
execution/
├── sprint_report_generator.py          # Script principal (orquestra tudo)
├── collectors/
│   ├── jira_collector.py              # Coleta dados do Jira
│   ├── github_collector.py            # Coleta PRs e reviews
│   └── cicd_collector.py              # Coleta dados de deployment
├── generators/
│   ├── report_generator.py            # Gera Google Doc
│   └── chart_generator.py             # Gera gráficos matplotlib
├── notifiers/
│   └── slack_notifier.py              # Envia notificação Slack
└── utils/
    ├── gdocs_helper.py                # Helpers para Google Docs API
    ├── jira_client.py                 # Cliente Jira simplificado
    └── github_client.py               # Cliente GitHub simplificado
```

### Templates
```
templates/
└── sprint_report_template.docx        # Template Word do relatório
```

### Outputs Temporários
```
.tmp/
├── jira_data_SPRINT-{id}.json         # Cache de dados Jira
├── github_data_{team}.json            # Cache de dados GitHub
├── cicd_data_{team}.json              # Cache de dados CI/CD
├── charts/                            # Gráficos temporários
│   ├── velocity_trend.png
│   ├── review_time.png
│   └── deployment_frequency.png
└── logs/
    └── sprint_report_SPRINT-{id}.log  # Log de execução
```

---

## 🐛 Troubleshooting

### "Jira authentication failed"
**Causa:** Token API Jira expirado ou permissões insuficientes
**Solução:**
1. Regenerar token em: Jira → Profile → Security → API Tokens
2. Verificar email está correto em JIRA_EMAIL
3. Confirmar permissões "Browse Projects" e "View Issues"

### "No PRs found for period"
**Causa:** Filtro de datas ou equipe incorreto
**Solução:**
1. Verificar período da sprint está correto
2. Confirmar nome da equipe GitHub existe
3. Verificar GitHub token tem acesso ao org

### "Google Doc creation failed"
**Causa:** Credenciais Google inválidas ou permissões insuficientes
**Solução:**
1. Deletar token.json e refazer OAuth flow
2. Verificar credentials.json é OAuth client válido
3. Adicionar scopes: `docs`, `drive`

### "Chart generation error"
**Causa:** Matplotlib não instalado ou dados vazios
**Solução:**
1. `pip install matplotlib`
2. Verificar dados coletados não estão vazios
3. Se sem dados, gráfico não será gerado (não é erro crítico)

---

## 📚 Aprendizados e Melhorias

### Versão Atual: 2.1

**O que funciona bem:**
- Coleta paralela reduz tempo de execução em 60%
- Claude gera insights relevantes sobre trends
- Cache evita refazer coletas em caso de erro parcial
- Template do Google Doc facilita leitura

**Limitações conhecidas:**
- Jira API lenta para sprints com >100 issues (> 30s)
- GitHub rate limit pode ser atingido em equipes grandes (>50 devs)
- Gráficos são estáticos (não interativos)

**Melhorias planejadas:**
- [ ] Adicionar comparação com sprints anteriores
- [ ] Implementar alertas automáticos (e.g., velocity caindo >20%)
- [ ] Integração com Confluence para publicação automática
- [ ] Dashboard Grafana complementar em tempo real

### Changelog

**2024-01-30 (v2.1):** Self-annealing update
- Melhorado retry logic para Jira API (exponential backoff)
- Adicionado cache de dados para recuperação de falhas
- Otimizado queries GitHub (redução de 40% nas chamadas API)

**2024-01-15 (v2.0):** Major update
- Migrado de PDF para Google Doc (melhor colaboração)
- Adicionado geração automática de gráficos
- Implementado coleta paralela (3 threads)

**2023-12-01 (v1.0):** Versão inicial
- Setup básico do processo
- Coleta sequencial de dados
- Output em PDF

---

## 📊 Métricas de Sucesso

| Métrica | Método de Medição | Meta Atual | Resultado Última Sprint |
|---------|-------------------|------------|-------------------------|
| Tempo de execução | Timestamp início/fim | < 5 minutos | 3min 42s ✅ |
| Taxa de sucesso | Execuções OK / Total | > 95% | 98% ✅ |
| Precisão dos dados | Validação manual spot-check | > 98% | 99.2% ✅ |
| Satisfação stakeholders | Feedback trimestral | 4.5/5 | 4.7/5 ✅ |
| Adoção pela equipe | Sprints usando / Total | 100% | 100% ✅ |

---

## 🔗 Referências

- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [GitHub REST API v3](https://docs.github.com/en/rest)
- [Google Docs API Guide](https://developers.google.com/docs/api)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference)
- [Dashboard Grafana Complementar](https://grafana.equifax.internal/d/sprint-metrics)

---

**Última atualização:** 2024-01-30
**Responsável:** Quaresma (Engineering Manager - Platform Team)
**Status:** ✅ Ativo e em produção
