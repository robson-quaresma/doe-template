# CHANGELOG Usage Guide for AI Agents

> **Instruções específicas para AI Agents sobre como usar o CHANGELOG.md de forma eficiente**

---

## 🎯 Objetivo

CHANGELOG.md é o **registro histórico de mudanças significativas** no projeto. Agents devem:
- ✅ Consultá-lo ANTES de modificar componentes existentes
- ✅ Atualizar após TODA mudança significativa
- ❌ NUNCA ler o arquivo completo (desperdício de tokens!)

---

## 📖 Quando Consultar (Leitura)

### ✅ SEMPRE Consultar Quando:

1. **Antes de modificar diretiva/skill existente**
   ```
   User: "Atualize a diretiva de setup do Firebase"
   Agent: [LER últimas mudanças em directives/dev/setup-firebase.md]
   ```

2. **Usuário pergunta sobre mudanças recentes**
   ```
   User: "O que mudou na última semana?"
   Agent: [LER entries dos últimos 7 dias]
   ```

3. **Debugging de erro recente**
   ```
   User: "Por que o deploy está falhando?"
   Agent: [LER entries [FIX] recentes relacionados a deploy]
   ```

4. **Entender contexto de feature existente**
   ```
   User: "Por que temos cache no competitor analyzer?"
   Agent: [GREP "competitor_analyzer" em CHANGELOG.md]
   ```

### ❌ NUNCA Consultar Quando:

1. **Criar novo componente do zero**
   ```
   User: "Crie nova diretiva de teste de API"
   Agent: [NÃO precisa ler CHANGELOG, é nova]
   ```

2. **Responder questões gerais do produto**
   ```
   User: "Qual é o público-alvo do BeautyBot?"
   Agent: [Ler product/resumo-executivo.md, NÃO CHANGELOG]
   ```

3. **Executar diretiva sem modificá-la**
   ```
   User: "Execute análise de concorrentes"
   Agent: [Executar diretiva, NÃO precisa ver histórico]
   ```

---

## 📝 Como Ler (Técnicas de Economia de Tokens)

### Técnica 1: Leitura Filtrada por Linhas

```bash
# ✅ BOM: Apenas últimas 5 entradas (primeiras 50 linhas)
head -n 50 CHANGELOG.md

# ❌ RUIM: Ler arquivo inteiro
cat CHANGELOG.md
```

### Técnica 2: Grep por Componente Específico

```bash
# ✅ BOM: Apenas mudanças em componente específico
grep -A 3 "directives/dev/setup-firebase" CHANGELOG.md

# A 3 = mostra 3 linhas após match (pega Ação, Motivo, Impacto)
```

### Técnica 3: Filtro por Categoria

```bash
# ✅ BOM: Apenas correções recentes
grep "\[FIX\]" CHANGELOG.md | head -n 20

# ✅ BOM: Apenas adições
grep "\[ADD\]" CHANGELOG.md | head -n 20
```

### Técnica 4: Filtro por Data (Últimos N dias)

```bash
# ✅ BOM: Mudanças nos últimos 7 dias
# Filtra por YYYY-MM (mês atual) e pega últimas 30 linhas
grep "$(date +%Y-%m)" CHANGELOG.md | tail -n 30
```

---

## 📤 Quando Escrever (Atualização)

### ✅ SEMPRE Adicionar Entry Quando:

1. **Criar nova diretiva**
   ```
   ### 2024-01-30 | [ADD] | directives/ops/metrics-report.md
   - Ação: Nova diretiva de relatório semanal de métricas
   - Motivo: Automatizar compilação de KPIs semanais
   - Impacto: Stakeholders recebem report automático
   ```

2. **Modificar diretiva existente**
   ```
   ### 2024-01-30 | [CHG] | directives/dev/setup-firebase.md
   - Ação: Adicionado suporte para Firebase Emulators
   - Motivo: Facilitar desenvolvimento local
   - Impacto: Devs podem testar sem deploy
   ```

3. **Criar/modificar skill**
   ```
   ### 2024-01-30 | [ADD] | skills/whatsapp_tester
   - Ação: Nova skill para testes de integração WhatsApp
   - Motivo: Automatizar validação de fluxos conversacionais
   - Impacto: Testes de bot em <5 min
   ```

4. **Corrigir bug**
   ```
   ### 2024-01-30 | [FIX] | execution/utils.py
   - Ação: Cache invalidation agora usa timestamp correto
   - Motivo: Cache nunca expirava (bug de timezone)
   - Impacto: Cache agora respeita TTL de 24h
   ```

5. **Otimização significativa**
   ```
   ### 2024-01-30 | [OPT] | skills/competitor_analyzer
   - Ação: Paralelização de scraping (3 workers)
   - Motivo: Análise de 10 concorrentes levava 15min
   - Impacto: Redução de 15min → 5min (-67%)
   ```

6. **Remover componente**
   ```
   ### 2024-01-30 | [DEL] | directives/legacy/old-deploy.md
   - Ação: Removida diretiva de deploy manual obsoleta
   - Motivo: Substituída por deploy automatizado
   - Impacto: Usar directives/dev/deploy-automated.md
   ```

### ❌ NÃO Adicionar Entry Para:

1. **Mudanças triviais**
   - Correção de typo em comentário
   - Formatação de código
   - Renomear variável interna

2. **Work in progress não finalizado**
   - Apenas quando mudança está completa e testada

3. **Mudanças em arquivos temporários**
   - Nada em `.tmp/` vai para CHANGELOG

---

## ✍️ Como Escrever (Formato)

### Template de Entry

```
### [DATA] | [CATEGORIA] | [componente]
- Ação: [O QUE em <100 chars]
- Motivo: [POR QUÊ em <80 chars]
- Impacto: [O QUE MUDA em <80 chars]
```

### Regras de Concisão

**✅ BOM:**
```
### 2024-01-30 | [FIX] | skills/competitor_analyzer
- Ação: Retry em scraping usa exponential backoff
- Motivo: Rate limit com retry linear
- Impacto: -90% erros de API
```
**Tokens usados:** ~40

**❌ RUIM:**
```
### 2024-01-30 | [FIX] | execution/skills/competitor_analyzer/scraper.py
- Ação: Foi implementado um sistema de retry com exponential backoff 
  no processo de scraping de dados de concorrentes para evitar que...
- Motivo: Estávamos tendo muitos problemas com rate limiting das APIs 
  quando usávamos retry linear, então precisamos mudar para...
- Impacto: Agora o sistema consegue se recuperar automaticamente de 
  erros de rate limit e conseguimos reduzir em 90% os erros...
```
**Tokens usados:** ~180 (4.5x mais!)

---

## 🤖 Fluxo de Trabalho para Agents

### Passo 1: Antes de Modificar

```python
# Pseudo-código de decisão

if user_wants_modify_existing_component:
    component_path = identify_component()
    
    # Ler apenas entradas relevantes
    relevant_changes = grep(f"| {component_path}", "CHANGELOG.md", lines=10)
    
    # Entender contexto
    analyze(relevant_changes)
    
    # Aplicar modificação
    modify_component()
    
    # Atualizar CHANGELOG
    add_changelog_entry()
```

### Passo 2: Adicionar Entry

```python
def add_changelog_entry(category, component, action, reason, impact):
    """
    Adiciona entry ao CHANGELOG.md de forma estruturada.
    
    Args:
        category: ADD/CHG/FIX/DEL/DOC/OPT
        component: Path do componente (ex: directives/dev/setup.md)
        action: O que foi feito (<100 chars)
        reason: Por quê (<80 chars)
        impact: O que muda (<80 chars)
    """
    date = get_current_date()  # YYYY-MM-DD
    
    entry = f"""
### {date} | [{category}] | {component}
- Ação: {action}
- Motivo: {reason}
- Impacto: {impact}
"""
    
    # Inserir após linha "## [Unreleased]"
    insert_after_line(
        file="CHANGELOG.md",
        marker="## [Unreleased]",
        content=entry
    )
```

---

## 📊 Exemplos de Consultas Eficientes

### Exemplo 1: Mudanças Recentes

**Pergunta do usuário:**
```
"O que mudou no projeto nos últimos 7 dias?"
```

**Agent deve fazer:**
```bash
# Ler apenas últimas entradas (aprox. últimos 7 dias)
head -n 100 CHANGELOG.md | grep "^###"

# Ou filtrar por data (se possível)
current_month=$(date +%Y-%m)
grep "$current_month" CHANGELOG.md | head -n 50
```

**NÃO fazer:**
```bash
cat CHANGELOG.md  # ❌ Ler tudo
```

---

### Exemplo 2: Histórico de Componente Específico

**Pergunta do usuário:**
```
"Quando foi a última vez que modificamos a skill de competitor analyzer?"
```

**Agent deve fazer:**
```bash
# Buscar apenas entradas deste componente
grep -A 3 "skills/competitor_analyzer" CHANGELOG.md | head -n 20

# -A 3 = mostra 3 linhas após (Ação, Motivo, Impacto)
# head -n 20 = apenas primeiras 20 linhas (mais recentes)
```

---

### Exemplo 3: Bugs Recentes

**Pergunta do usuário:**
```
"Quais bugs foram corrigidos recentemente?"
```

**Agent deve fazer:**
```bash
# Filtrar apenas [FIX], pegar últimas 10
grep "\[FIX\]" CHANGELOG.md | head -n 30

# 30 linhas = ~10 entries de FIX (3 linhas cada)
```

---

## 🎯 Checklist para Agents

Antes de **LER** CHANGELOG:
- [ ] Mudança envolve componente existente?
- [ ] Usuário perguntou sobre histórico?
- [ ] Preciso entender contexto de modificações anteriores?
- [ ] Se NÃO para todas → NÃO ler CHANGELOG

Antes de **ESCREVER** no CHANGELOG:
- [ ] Mudança é significativa? (não trivial)
- [ ] Componente foi criado ou modificado?
- [ ] Entry tem <100 chars por linha?
- [ ] Categoria correta (ADD/CHG/FIX/DEL/DOC/OPT)?
- [ ] Se SIM para todas → Adicionar entry

---

## 📏 Métricas de Qualidade

**Entry bem escrito:**
- ✅ Total < 250 chars (Ação + Motivo + Impacto)
- ✅ Categoria clara
- ✅ Componente path correto
- ✅ Sem informação redundante

**Entry ruim:**
- ❌ Total > 500 chars
- ❌ Detalhes desnecessários
- ❌ Informação duplicada

---

## 🔧 Manutenção Periódica

### A Cada 3 Meses

```bash
# Arquivar entries antigas
# Mover entries de [Unreleased] para versão release
# Atualizar estatísticas

# Exemplo:
mv CHANGELOG.md CHANGELOG-2024-Q1.md
# Criar novo CHANGELOG.md limpo
```

### Versionamento

Quando fazer release:
```
## [Unreleased]
[entries aqui]

↓ (ao fazer release) ↓

## [1.1.0] - 2024-01-30
[entries movidos de Unreleased]

## [1.0.0] - 2024-01-15
[entries da v1.0.0]
```

---

## 💡 Dicas Finais para Agents

1. **Seja Conciso:** Cada palavra conta em tokens
2. **Seja Consistente:** Use sempre o mesmo formato
3. **Seja Relevante:** Apenas mudanças significativas
4. **Seja Específico:** Componente path correto
5. **Seja Útil:** Entry deve responder "o quê, por quê, e daí?"

---

**Versão:** 1.0.0
**Para:** AI Agents (Claude, Gemini, etc.)
**Objetivo:** Maximizar utilidade, minimizar consumo de tokens
