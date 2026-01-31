# Quick Start - DOE Framework

> Comece em 10 minutos

---

## ⚡ Setup Rápido

### 1. Dependências (3 min)

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar core dependencies apenas
pip install python-dotenv requests anthropic google-api-python-client
```

### 2. Configuração (5 min)

```bash
# Copiar template de .env
cp .env.example .env

# Editar .env com APENAS o essencial:
nano .env
```

**Mínimo necessário no .env:**
```bash
ANTHROPIC_API_KEY=sk-ant-your_key
GOOGLE_CREDENTIALS_PATH=credentials.json
```

### 3. Primeiro Teste (2 min)

```bash
# Criar diretiva simples
cp directives/TEMPLATE.md directives/minha_tarefa.md

# Editar e testar
python3 execution/sprint_report_generator.py --sprint-id "TEST-1" --team "test"
```

---

## 📋 Workflow Básico

```
1. Identifique tarefa repetitiva
   ↓
2. Crie diretiva em directives/
   ↓
3. Crie script em execution/ (se necessário)
   ↓
4. Execute via AI Agent ou diretamente
   ↓
5. Itere e melhore (self-anneal!)
```

---

## 🎯 Exemplos Prontos

### Exemplo 1: Relatório de Sprint
```bash
python3 execution/sprint_report_generator.py \
  --sprint-id "SPRINT-42" \
  --team "platform"
```

### Exemplo 2: Validação de Ideia SaaS
```bash
python3 execution/saas_idea_validator.py \
  --idea "Seu SaaS aqui" \
  --target-market "SMBs"
```

---

## 🔑 Primeiros Passos com Claude

**Prompt para Claude:**

```
Olá Claude! Leia o arquivo AGENTS.md primeiro.

Depois, quero que você execute a diretiva em 
directives/sprint_report_automation.md com os 
seguintes inputs:
- sprint-id: SPRINT-42
- team: platform

Siga exatamente o processo DOE:
1. Leia a diretiva
2. Valide inputs
3. Execute os scripts necessários
4. Gere o relatório
```

---

## 💡 Dicas Importantes

✅ **FAÇA:**
- Comece simples (1 tarefa por vez)
- Use .tmp/ para tudo temporário
- Documente aprendizados nas diretivas
- Deixe o sistema self-anneal

❌ **NÃO FAÇA:**
- Commitar .env ou .tmp/
- Criar scripts gigantes
- Ignorar erros
- Esquecer de atualizar diretivas

---

## 🆘 Problemas Comuns

**"ModuleNotFoundError"**
```bash
pip install [module-name]
```

**"Authentication failed"**
```bash
# Regenerar API key e atualizar .env
```

**"Permission denied"**
```bash
chmod +x execution/script.py
```

---

## 📚 Próximos Passos

1. ✅ Setup básico completo
2. ⬜ Ler README.md completo
3. ⬜ Estudar exemplo: sprint_report_automation.md
4. ⬜ Criar sua primeira diretiva
5. ⬜ Executar e iterar

---

**Boa automação! 🚀**

Para documentação completa: [README.md](README.md)
