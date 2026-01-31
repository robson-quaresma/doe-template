# Skills - Capacidades Especializadas

> **Skills são módulos de expertise reutilizáveis que estendem as capacidades do DOE Framework**

---

## 🎯 O Que São Skills?

Skills são como "ferramentas especializadas" ou "expertise modules" que o AI Agent pode invocar quando necessário. Pense nelas como mini-aplicações focadas em resolver um tipo específico de problema.

### **Analogia:**

```
DOE Framework = Oficina mecânica
Skills = Ferramentas especializadas (torquímetro, scanner OBD, etc.)
Scripts normais = Ferramentas básicas (chave de fenda, alicate, etc.)
```

---

## 🔑 Skills vs Scripts Normais

| Característica | Skill | Script Normal |
|----------------|-------|---------------|
| **Escopo** | Reutilizável em vários projetos | Específico de uma diretiva |
| **Documentação** | SKILL.md obrigatório | Opcional/inline |
| **Configuração** | config.json estruturado | Args ou hardcoded |
| **Compartilhamento** | Pode ser publicada/compartilhada | Interno ao projeto |
| **Manutenção** | Versionada e testada | Ad-hoc |
| **Complexidade** | Pode ter múltiplos módulos | Geralmente single-file |

---

## 📂 Estrutura de uma Skill

```
execution/skills/
├── skill_name/
│   ├── SKILL.md              # 📄 Documentação completa
│   ├── config.json           # ⚙️ Configurações
│   ├── main.py               # 🎯 Script principal
│   │
│   ├── modules/              # 📦 Módulos internos (opcional)
│   │   ├── scraper.py
│   │   ├── analyzer.py
│   │   └── formatter.py
│   │
│   ├── tests/                # ✅ Testes (opcional mas recomendado)
│   │   └── test_main.py
│   │
│   └── examples/             # 💡 Exemplos de uso (opcional)
│       └── example_usage.py
```

---

## 📋 Anatomia de SKILL.md

Todo SKILL.md deve conter (no mínimo):

```markdown
# Nome da Skill

## Overview
- O que faz
- Quando usar

## Inputs
- Parâmetros obrigatórios
- Parâmetros opcionais

## Outputs
- Formato(s) de saída
- Schema de dados

## Como Usar
- Exemplos básicos
- Exemplos avançados

## Dependências
- Python packages
- APIs necessárias
- Env vars

## Troubleshooting
- Problemas comuns
- Soluções

## Versão
- Número da versão
- Changelog
```

---

## 🛠️ Skills Disponíveis

### **Built-in (Públicas)**

Já incluídas no framework:

- `docx` - Manipulação de Word documents
- `xlsx` - Manipulação de planilhas Excel
- `pptx` - Geração de apresentações
- `pdf` - Leitura e criação de PDFs
- `web_search` - Busca na web
- `web_scrape` - Web scraping estruturado

### **Customizadas (User-Created)**

Criadas para necessidades específicas:

- `competitor_analyzer` - Análise de concorrentes (exemplo neste template)
- `[sua_skill]` - Crie suas próprias!

---

## 🚀 Como Criar Sua Própria Skill

### Passo 1: Identificar Necessidade

Pergunte-se:
- ❓ Este processo é reutilizável em múltiplos projetos?
- ❓ É complexo o suficiente para merecer documentação dedicada?
- ❓ Outras pessoas poderiam se beneficiar desta skill?

**Se SIM para 2+ perguntas** → Crie uma skill!
**Se NÃO** → Um script normal em `execution/` é suficiente

### Passo 2: Criar Estrutura

```bash
# Copiar template
cp -r execution/skills/competitor_analyzer execution/skills/minha_skill

# Renomear arquivos
cd execution/skills/minha_skill
mv main.py minha_skill.py
```

### Passo 3: Documentar (SKILL.md)

```markdown
# Minha Skill

## Overview
Faz X, Y e Z de forma automatizada.

## Inputs
- `--param1`: Descrição
- `--param2`: Descrição

## Outputs
```json
{
  "resultado": "..."
}
```

## Como Usar
\`\`\`bash
python3 execution/skills/minha_skill/minha_skill.py --param1 "valor"
\`\`\`
```

### Passo 4: Configurar (config.json)

```json
{
  "skill_name": "minha_skill",
  "version": "1.0.0",
  "description": "Breve descrição",
  "dependencies": {
    "python_packages": ["requests"],
    "env_vars_required": ["API_KEY"]
  }
}
```

### Passo 5: Implementar (main.py)

```python
#!/usr/bin/env python3
"""
Minha Skill - Descrição

Usage:
    python3 minha_skill.py --param1 "valor"
"""

import json
import argparse
from pathlib import Path

# Carregar config
config_path = Path(__file__).parent / "config.json"
with open(config_path) as f:
    CONFIG = json.load(f)

def main():
    parser = argparse.ArgumentParser(description=CONFIG['description'])
    parser.add_argument('--param1', required=True, help='...')
    args = parser.parse_args()
    
    # Sua lógica aqui
    result = process(args.param1)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
```

### Passo 6: Testar

```bash
# Teste básico
python3 execution/skills/minha_skill/main.py --param1 "teste"

# Verificar output
# Testar edge cases
# Confirmar documentação está clara
```

### Passo 7: Usar em Diretivas

```markdown
# Minha Diretiva

## Ferramentas/Scripts

### Minha Skill
\`\`\`bash
python3 execution/skills/minha_skill/main.py \
  --param1 "valor1" \
  --param2 "valor2"
\`\`\`
```

---

## 💡 Boas Práticas

### ✅ FAÇA:

- Documentação completa no SKILL.md
- Versionamento semântico (1.0.0, 1.1.0, 2.0.0)
- Validação de inputs
- Error handling robusto
- Exemplos de uso claros
- Changelog de versões

### ❌ NÃO FAÇA:

- Skills sem documentação
- Hardcoded secrets
- Dependências não documentadas
- Output não estruturado
- Skills muito específicas (viram scripts normais)

---

## 📦 Compartilhamento de Skills

### Publicar sua Skill:

1. **Documentar completamente**
2. **Versionar** (git tag)
3. **Compartilhar**:
   - GitHub repo público
   - Gist
   - Package no PyPI (avançado)

### Usar Skill de Terceiros:

```bash
# Clonar skill
git clone https://github.com/user/awesome_skill execution/skills/awesome_skill

# Instalar dependências
pip install -r execution/skills/awesome_skill/requirements.txt

# Configurar env vars (se necessário)
# Usar conforme SKILL.md
```

---

## 🎓 Exemplos de Skills Úteis

### Para Engineering Managers:
- `team_metrics_analyzer` - Análise de métricas de equipe
- `jira_reporter` - Relatórios automáticos do Jira
- `code_review_insights` - Insights de code reviews

### Para SaaS Founders:
- `competitor_analyzer` - Análise de concorrentes (já incluída!)
- `market_validator` - Validação rápida de mercado
- `pricing_optimizer` - Análise de pricing

### Para Desenvolvedores:
- `api_tester` - Testes automáticos de API
- `db_migrator` - Migrações de banco de dados
- `deploy_manager` - Gestão de deploys

---

## 🔗 Recursos Adicionais

- **Exemplo Completo**: `competitor_analyzer/` neste diretório
- **Template**: Copie `competitor_analyzer/` como base
- **Documentação DOE**: `../../../README.md`

---

## ❓ FAQ

**Q: Skill vs Diretiva - qual a diferença?**
A: Diretiva = "O QUE fazer" (processo). Skill = "COMO fazer" (ferramenta).

**Q: Posso ter skills dentro de skills?**
A: Sim, mas evite complexidade excessiva. Skills devem ser focadas.

**Q: Skills podem chamar outras skills?**
A: Sim, mas documente as dependências claramente.

**Q: Preciso criar skill para tudo?**
A: Não! Scripts simples em `execution/` são perfeitamente válidos. Skills são para código reutilizável e complexo.

---

**Versão:** 1.0
**Última atualização:** 2024-01-30

**Skills tornam o DOE Framework extensível e poderoso! 🚀**
