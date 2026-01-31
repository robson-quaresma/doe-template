# Competitor Analyzer Skill

> **Skill customizada para análise automatizada de concorrentes**

Esta skill automatiza a análise de concorrentes para produtos SaaS, coletando dados de múltiplas fontes e gerando relatório comparativo estruturado.

---

## 📋 Overview

**O que faz:**
- Busca informações sobre concorrente (website, pricing, features)
- Analisa reviews em múltiplas plataformas
- Extrai dados de tráfego (via SimilarWeb)
- Gera relatório comparativo estruturado

**Quando usar:**
- Validação de ideias de produto
- Research de mercado
- Análise competitiva trimestral
- Preparação de pitch decks

---

## 🎯 Inputs

| Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
|-----------|------|-------------|-----------|---------|
| `--competitor` | String | Sim | Nome ou domínio do concorrente | "mailchimp.com" |
| `--aspects` | List | Não | Aspectos a analisar (default: all) | "pricing,features,reviews" |
| `--depth` | String | Não | Profundidade (quick/standard/deep) | "standard" |
| `--output-format` | String | Não | Formato (json/markdown/gdoc) | "markdown" |

---

## 📤 Outputs

### Formato JSON

```json
{
  "competitor": {
    "name": "Mailchimp",
    "domain": "mailchimp.com",
    "description": "Email marketing platform"
  },
  "pricing": {
    "model": "freemium",
    "tiers": [
      {"name": "Free", "price": 0, "limits": "2,000 contacts"},
      {"name": "Essentials", "price": 13, "limits": "50,000 contacts"},
      {"name": "Standard", "price": 20, "limits": "100,000 contacts"}
    ]
  },
  "features": {
    "core": ["Email campaigns", "Automation", "Analytics"],
    "advanced": ["A/B testing", "Segmentation", "API"]
  },
  "reviews": {
    "g2": {"rating": 4.3, "count": 12500, "pros": [...], "cons": [...]},
    "capterra": {"rating": 4.5, "count": 8900}
  },
  "traffic": {
    "monthly_visits": 45000000,
    "bounce_rate": 0.42,
    "avg_duration": "4:23"
  },
  "analysis": {
    "strengths": [...],
    "weaknesses": [...],
    "opportunities": [...]
  }
}
```

### Formato Markdown

```markdown
# Competitor Analysis: Mailchimp

## Overview
Email marketing platform with 45M monthly visits...

## Pricing
- Free: $0 (2,000 contacts)
- Essentials: $13/mo (50,000 contacts)
- Standard: $20/mo (100,000 contacts)

## Key Features
- Email campaigns
- Marketing automation
- Analytics & reporting

## User Reviews (G2: 4.3/5, 12.5K reviews)
**Pros:**
- Easy to use
- Great templates
- Reliable delivery

**Cons:**
- Expensive at scale
- Limited customization
- Support could be better

## Traffic Analysis
- 45M monthly visits
- 42% bounce rate
- 4:23 avg session

## Competitive Position
**Strengths:** Brand recognition, ease of use
**Weaknesses:** Pricing at scale, feature limitations
**Opportunities:** Better SMB pricing, more integrations
```

---

## 🔧 Como Usar

### Básico

```bash
python3 execution/skills/competitor_analyzer/analyze.py \
  --competitor "mailchimp.com" \
  --output-format "markdown"
```

### Avançado

```bash
python3 execution/skills/competitor_analyzer/analyze.py \
  --competitor "mailchimp.com" \
  --aspects "pricing,features,reviews,traffic" \
  --depth "deep" \
  --output-format "gdoc"
```

### Via Python

```python
from execution.skills.competitor_analyzer import CompetitorAnalyzer

analyzer = CompetitorAnalyzer()
result = analyzer.analyze(
    competitor="mailchimp.com",
    aspects=["pricing", "features", "reviews"],
    depth="standard"
)

print(result.summary)
```

---

## 📦 Dependências

### Python Packages

```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
anthropic>=0.8.1  # Para análise com Claude
google-api-python-client>=2.100.0  # Se output em Google Doc
```

### APIs Necessárias

- Anthropic Claude API (obrigatório)
- SimilarWeb API (opcional - tem free tier limitado)
- Google Workspace API (se output em Google Doc)

### Environment Variables

```bash
ANTHROPIC_API_KEY=sk-ant-xxx
SIMILARWEB_API_KEY=xxx  # Opcional
GOOGLE_CREDENTIALS_PATH=credentials.json  # Se usar Google Doc
```

---

## ⚙️ Configuração

### config.json

```json
{
  "skill_name": "competitor_analyzer",
  "version": "1.0.0",
  "default_aspects": ["pricing", "features", "reviews"],
  "default_depth": "standard",
  "cache_ttl_hours": 24,
  "sources": {
    "reviews": ["g2.com", "capterra.com", "trustpilot.com"],
    "traffic": "similarweb",
    "features": "website_scrape"
  },
  "output": {
    "default_format": "markdown",
    "gdoc_template_id": null
  }
}
```

---

## 🔄 Workflow Interno

```
1. Validar inputs
   ↓
2. Buscar dados do concorrente
   ├─ Website scraping (pricing page, features)
   ├─ Reviews (G2, Capterra)
   └─ Traffic data (SimilarWeb)
   ↓
3. Processar e normalizar dados
   ↓
4. Análise com Claude
   ├─ Identificar strengths
   ├─ Identificar weaknesses
   └─ Sugerir opportunities
   ↓
5. Gerar output no formato solicitado
   ↓
6. Cache results (evitar re-scraping)
```

---

## ⚠️ Limitações

- **Rate Limits:** Respeita robots.txt e rate limits de sites
- **Paywall Content:** Não consegue acessar conteúdo pago
- **Dynamic Content:** Pode ter dificuldade com sites JavaScript-heavy
- **Accuracy:** Pricing/features podem mudar (cache de 24h)

---

## 💰 Custos Estimados

| Componente | Custo por Análise |
|------------|-------------------|
| Web scraping | $0.00 (gratuito) |
| Claude API | ~$0.10 (análise) |
| SimilarWeb API | $0.00 (free tier) |
| Google Doc API | $0.00 (gratuito) |
| **Total** | **~$0.10** |

**Análises mensais:** 10-20
**Custo mensal:** ~$1.00-2.00

---

## 🐛 Troubleshooting

### "Website scraping failed"
**Causa:** Site bloqueia bots ou requer JavaScript
**Solução:** 
- Verificar robots.txt
- Adicionar User-Agent apropriado
- Considerar usar Selenium para sites dinâmicos

### "No pricing found"
**Causa:** Pricing não está em página pública
**Solução:**
- Procurar em /pricing, /plans
- Buscar em blog posts ou press releases
- Marcar como "Contact for pricing"

### "Reviews data incomplete"
**Causa:** Plataforma de review mudou HTML
**Solução:**
- Atualizar seletores CSS/XPath
- Usar API se disponível
- Aceitar dados parciais

---

## 📈 Melhorias Futuras

- [ ] Integração com ProductHunt API
- [ ] Análise de posts em redes sociais
- [ ] Tracking de mudanças ao longo do tempo
- [ ] Dashboard comparativo interativo
- [ ] Export para Notion/Airtable

---

## 📚 Exemplos de Uso

### Caso 1: Validação de Pricing

```bash
# Comparar pricing de 3 concorrentes
for competitor in mailchimp.com sendinblue.com activecampaign.com; do
  python3 execution/skills/competitor_analyzer/analyze.py \
    --competitor "$competitor" \
    --aspects "pricing" \
    --output-format "json" > ".tmp/${competitor}_pricing.json"
done

# Compilar relatório comparativo
python3 execution/skills/competitor_analyzer/compare.py \
  --inputs ".tmp/*_pricing.json" \
  --output "pricing_comparison.md"
```

### Caso 2: Análise Completa para Pitch Deck

```bash
python3 execution/skills/competitor_analyzer/analyze.py \
  --competitor "mailchimp.com" \
  --depth "deep" \
  --output-format "gdoc"
```

---

## 🔗 Arquivos Relacionados

```
execution/skills/competitor_analyzer/
├── SKILL.md                    # Este arquivo
├── config.json                 # Configurações
├── analyze.py                  # Script principal
├── scrapers/
│   ├── website_scraper.py     # Scraping do site
│   ├── reviews_scraper.py     # Scraping de reviews
│   └── traffic_analyzer.py    # SimilarWeb integration
├── analyzers/
│   └── claude_analyzer.py     # Análise com Claude
└── formatters/
    ├── json_formatter.py
    ├── markdown_formatter.py
    └── gdoc_formatter.py
```

---

**Versão:** 1.0.0
**Autor:** Quaresma (Qriterion Tech Lab)
**Última atualização:** 2024-01-30
**Status:** ✅ Ativo

---

## 📝 Como Criar Sua Própria Skill

Use esta como template:

1. **Copie a estrutura:**
```bash
cp -r execution/skills/competitor_analyzer execution/skills/your_skill
```

2. **Customize:**
- Edite `SKILL.md` com sua documentação
- Ajuste `config.json`
- Implemente lógica em `analyze.py`

3. **Teste:**
```bash
python3 execution/skills/your_skill/analyze.py --help
```

4. **Use em diretivas:**
```markdown
## Ferramentas/Scripts

### Análise de Concorrente
\`\`\`bash
python3 execution/skills/competitor_analyzer/analyze.py \
  --competitor "example.com"
\`\`\`
```

---

**Skills tornam o DOE Framework mais poderoso e reutilizável! 🚀**
