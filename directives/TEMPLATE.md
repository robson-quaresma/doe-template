# [Nome da Tarefa/Processo]

> Template de Diretiva DOE Framework - Copie e adapte para suas necessidades

[Uma linha descrevendo o objetivo principal desta diretiva]

---

## 📋 Overview

Descrição detalhada do que este processo faz e por que existe.

**Use este processo quando:**
- Cenário 1
- Cenário 2
- Cenário 3

**NÃO use quando:**
- Cenário negativo 1
- Cenário negativo 2

---

## 🎯 Objetivo

Defina claramente o objetivo final deste processo. Seja específico e mensurável.

**Exemplo:**
> Gerar relatório semanal de métricas de desenvolvimento contendo: velocity da sprint, código review time médio, taxa de bugs em produção, e deployment frequency.

---

## 📥 Inputs (Entradas)

Liste todos os inputs necessários com tipo, obrigatoriedade e descrição.

| Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
|-----------|------|-------------|-----------|---------|
| `--data-inicio` | Date | Sim | Data inicial do período | `2024-01-01` |
| `--data-fim` | Date | Sim | Data final do período | `2024-01-31` |
| `--equipe` | String | Não | Nome da equipe (default: todas) | `platform-team` |
| `--formato` | String | Não | Formato de saída (pdf/xlsx) | `pdf` |

---

## 🔧 Ferramentas/Scripts

Liste os scripts de execução que devem ser usados e em que ordem.

### Script Principal
```bash
python3 execution/nome_script_principal.py \
  --data-inicio "2024-01-01" \
  --data-fim "2024-01-31" \
  --equipe "platform-team"
```

### Scripts Auxiliares (se aplicável)
```bash
# Pré-processamento
python3 execution/preparar_dados.py --fonte jira

# Pós-processamento
python3 execution/enviar_relatorio.py --destinatarios "email@example.com"
```

---

## 📤 Outputs (Saídas)

Descreva o formato e estrutura das saídas esperadas.

### Formato de Saída

**Tipo:** PDF Report / Google Sheet / JSON / etc.

**Estrutura:**
```
Seção 1: Métricas de Velocity
- Sprint velocity (média 4 semanas)
- Trend de velocity (crescimento/queda)
- Comparação com meta

Seção 2: Code Review
- Tempo médio de review
- PRs pendentes
- Top reviewers

Seção 3: Qualidade
- Bugs em produção
- Taxa de hotfix
- Test coverage
```

### Schema de Dados (se aplicável)

```json
{
  "period": {
    "start": "2024-01-01",
    "end": "2024-01-31"
  },
  "metrics": {
    "velocity": {
      "average": 45,
      "trend": "+12%",
      "target": 50
    },
    "code_review": {
      "avg_time_hours": 6.5,
      "pending_prs": 12
    },
    "quality": {
      "production_bugs": 3,
      "hotfix_rate": "2%",
      "test_coverage": "78%"
    }
  }
}
```

---

## 🔄 Fluxo de Execução

Descreva o fluxo passo a passo do processo.

### Passo 1: Coleta de Dados
- Conectar com fonte de dados (Jira, GitHub, etc.)
- Filtrar por período e equipe
- Validar dados coletados

### Passo 2: Processamento
- Calcular métricas agregadas
- Aplicar normalização/limpeza
- Identificar anomalias

### Passo 3: Geração de Output
- Formatar dados conforme template
- Gerar visualizações (gráficos)
- Exportar para formato final

### Passo 4: Distribuição
- Salvar em cloud storage
- Enviar notificações
- Atualizar dashboard (se aplicável)

---

## ⚠️ Edge Cases e Tratamento de Erros

Liste situações especiais e como lidar com elas.

### Caso 1: Dados Incompletos
**Situação:** Período solicitado tem dados faltando
**Ação:** 
- Logar aviso indicando períodos sem dados
- Continuar processamento com dados disponíveis
- Adicionar disclaimer no relatório

### Caso 2: API Rate Limit
**Situação:** Limite de chamadas de API atingido
**Ação:**
- Implementar exponential backoff
- Cachear dados quando possível
- Falhar graciosamente com mensagem clara

### Caso 3: Formato de Dados Inesperado
**Situação:** API retorna schema diferente do esperado
**Ação:**
- Validar schema antes de processar
- Logar erro detalhado
- Notificar usuário para verificação manual

---

## ✅ Definition of Done (DoD)

Critérios claros para considerar a tarefa completa.

**Este processo está completo quando:**
- [ ] Todos os inputs foram validados
- [ ] Dados foram coletados de todas as fontes necessárias
- [ ] Métricas calculadas passaram validação
- [ ] Output gerado no formato especificado
- [ ] Arquivo salvo em localização acessível ao usuário
- [ ] Notificações enviadas (se aplicável)
- [ ] Logs registrados para auditoria
- [ ] Sem erros críticos no processo

---

## 💰 Considerações de Custo

Estime custos associados à execução.

| Componente | Custo Estimado | Observações |
|------------|----------------|-------------|
| API Calls (Jira) | $0.00 | Incluído no plano |
| Claude API | ~$0.05 | Para sumarização |
| Google Sheets API | $0.00 | Gratuito |
| Armazenamento | ~$0.01 | S3/GCS |
| **Total por execução** | **~$0.06** | |

**Execuções mensais:** 4 (semanal)
**Custo mensal:** ~$0.24

---

## 📦 Dependências

Liste todas as dependências necessárias.

### Python Packages
```txt
requests>=2.31.0
pandas>=2.0.0
matplotlib>=3.7.0
anthropic>=0.8.0
google-api-python-client>=2.100.0
python-dotenv>=1.0.0
```

### Environment Variables
```bash
# .env file
JIRA_API_TOKEN=your_token_here
JIRA_BASE_URL=https://company.atlassian.net
GITHUB_TOKEN=your_github_token
ANTHROPIC_API_KEY=your_claude_key
GOOGLE_CREDENTIALS_PATH=credentials.json
```

### External Services
- Jira Cloud API
- GitHub REST API
- Google Sheets API
- Anthropic Claude API

---

## 📂 Arquivos Relacionados

Liste scripts e arquivos relacionados.

### Scripts de Execução
- `execution/nome_script_principal.py` - Script principal
- `execution/utils/data_collector.py` - Utilitário de coleta
- `execution/utils/report_generator.py` - Gerador de relatório

### Configurações
- `.env` - Variáveis de ambiente
- `config/report_template.json` - Template do relatório

### Outputs
- `.tmp/raw_data/` - Dados brutos coletados
- Deliverable final em Google Drive/OneDrive

---

## 🐛 Troubleshooting

Problemas comuns e soluções.

### "Authentication failed"
**Causa:** Token de API expirado ou inválido
**Solução:**
1. Verifique `.env` tem token válido
2. Regenere token no portal do serviço
3. Confirme permissões necessárias

### "No data found for period"
**Causa:** Período especificado sem atividade
**Solução:**
1. Verifique datas estão no formato correto (YYYY-MM-DD)
2. Confirme equipe existe no sistema
3. Amplie período de busca

### "Output file not created"
**Causa:** Permissões insuficientes ou path inválido
**Solução:**
1. Verifique permissões de escrita no diretório
2. Confirme path está correto
3. Crie diretório manualmente se necessário

---

## 📚 Aprendizados e Melhorias

Documente aprendizados para melhorias futuras.

### Versão Atual: 1.0

**O que funciona bem:**
- [Item 1]
- [Item 2]

**Limitações conhecidas:**
- [Limitação 1]
- [Limitação 2]

**Melhorias planejadas:**
- [ ] Melhoria 1
- [ ] Melhoria 2

### Changelog

**2024-01-30:** Versão inicial criada
- Setup inicial do processo
- Definição de inputs/outputs
- Primeira versão dos scripts

---

## 📊 Métricas de Sucesso

Como medir se este processo está funcionando.

| Métrica | Método de Medição | Meta |
|---------|-------------------|------|
| Tempo de execução | Timestamp início/fim | < 5 minutos |
| Taxa de sucesso | Execuções OK / Total | > 95% |
| Precisão dos dados | Validação manual | > 98% |
| Satisfação do usuário | Feedback direto | 4.5/5 |

---

## 🔗 Referências

Links úteis e documentação relacionada.

- [Documentação da API X](https://example.com)
- [Guia de configuração Y](https://example.com)
- [Dashboard de monitoramento](https://example.com)

---

**Última atualização:** 2024-01-30
**Responsável:** [Seu Nome]
**Status:** ✅ Ativo / ⚠️ Em Desenvolvimento / ❌ Depreciado
