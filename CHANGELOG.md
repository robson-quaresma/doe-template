# CHANGELOG

> Registro conciso de mudanças significativas

**Para AI Agents:** Leia apenas últimas 5-10 entradas ou use grep por categoria/arquivo. NUNCA leia completo!

---

## [Unreleased]

### Added
- Nenhum

### Changed
- Nenhum

### Fixed
- Nenhum

---

## [1.0.0] - 2024-01-30 - Initial Release

### Added
- `[DIRECTIVE]` Setup Firebase Project | directives/development/setup-firebase-project.md
- `[DIRECTIVE]` Competitor Analysis | directives/product/competitor-analysis.md
- `[DIRECTIVE]` Feature Validation | directives/product/feature-validation.md
- `[SKILL]` Competitor Analyzer | execution/skills/competitor_analyzer/
- `[DOC]` README customizado | README.md
- `[DOC]` AGENTS.md, CLAUDE.md, GEMINI.md | /
- `[CONFIG]` Estrutura DOE completa | /

---

## Formato de Entrada (1 linha!)

```
[CATEGORIA] Descrição (<50 chars) | path/do/arquivo
```

**Categorias:** DIRECTIVE, SKILL, SCRIPT, DOC, FIX, CONFIG

---

## Como AI Agents Devem Usar

### Ler (Seletivo!)
```bash
# Últimas entradas
head -30 CHANGELOG.md

# Por categoria
grep '[DIRECTIVE]' CHANGELOG.md

# Por arquivo
grep 'firebase' CHANGELOG.md
```

### Escrever (Conciso!)
```bash
# Adicionar em [Unreleased] > ### Added
echo "- [DIRECTIVE] Nome | path/arquivo" >> CHANGELOG.md
```

---

**Versionamento:** [SemVer](https://semver.org/) - MAJOR.MINOR.PATCH
