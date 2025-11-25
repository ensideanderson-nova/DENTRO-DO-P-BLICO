# CLAUDE.md - Guia para Assistentes de IA

Este documento fornece orientações para assistentes de IA (como Claude) que trabalham com o repositório **Sistema ENSIDE**.

## Visão Geral do Projeto

O **Sistema ENSIDE** é um sistema de organização inteligente de documentos desenvolvido para macOS. Ele organiza automaticamente arquivos e documentos empresariais em uma estrutura hierárquica de 14 categorias, com:

- **733+ pastas** estruturadas automaticamente
- **Detecção inteligente** de tipos de documento (PDFs, extratos bancários, notas fiscais, etc.)
- **Sistema de cores** integrado com o Finder do macOS
- **Visualização HTML** interativa com filtros e busca
- **Skill para Claude Code** para comandos de linguagem natural

### Propósito Principal
Automatizar a organização de documentos empresariais brasileiros, incluindo:
- Extratos bancários (6 bancos principais)
- Notas fiscais e documentos fiscais
- Contratos e documentos de clientes/fornecedores
- Documentos de segurança e fraudes
- Código-fonte e projetos

## Estrutura do Repositório

```
ENSIDE-PUBLICO/
├── README.md                 # Documentação principal
├── CHANGELOG.md              # Histórico de versões
├── LICENSE                   # Licença MIT
├── install.sh                # Script de instalação automatizada
├── requirements.txt          # Dependências Python (PyPDF2, python-magic-bin)
├── .gitignore                # Arquivos ignorados pelo Git
│
├── docs/                     # Documentação adicional
│   ├── INSTALLATION.md       # Guia detalhado de instalação
│   └── EXEMPLOS.md           # Casos de uso e exemplos
│
├── scripts/                  # Scripts principais do sistema
│   ├── importador_universal.py    # Importador principal (Python)
│   ├── organize_master.sh         # Criador da estrutura completa
│   ├── aplicar_cores_completo.sh  # Aplicador de cores no Finder
│   ├── gerar_html_completo.py     # Gerador de HTML interativo
│   ├── gerar_html_cores.py        # Gerador HTML simples
│   ├── file_organizer.py          # Organizador de arquivos
│   ├── general_organizer.py       # Organizador geral
│   ├── pdf_processor.py           # Processador específico de PDFs
│   ├── organizar_home_completo.sh # Organizador da HOME
│   ├── criar_categorias_novas.sh  # Criador de novas categorias
│   └── mover_arquivos_para_sistema.sh # Movimentador de arquivos
│
└── .github/workflows/        # GitHub Actions
    ├── claude.yml            # Integração Claude Code Action
    ├── claude-integration.yml # Análise automática de issues/PRs
    └── claude-code-review.yml # Code review automatizado
```

## Estrutura de Categorias do Sistema

O sistema organiza documentos em 14 categorias principais:

| # | Categoria | Cor Finder | Descrição |
|---|-----------|------------|-----------|
| 00 | TRIAGEM_POR_PESSOA | Roxo | Organização por CPF ou CNPJ |
| 01 | DOCUMENTOS_PESSOAIS | Verde | RG, CPF, CNH, Certidões |
| 02 | DOCUMENTOS_EMPRESA | Azul | CNPJ, Contratos, Alvarás |
| 03 | MADEIRAS | Roxo | Fornecedores, Estoque, Certificados |
| 04 | FRETES | Laranja | Motoristas, CTe, Cotações |
| 05 | BANCOS | Vermelho | 6 Bancos (Itaú, Bradesco, Santander, BB, Caixa, Nubank) |
| 06 | FINANCEIRO | Amarelo | Contas, Impostos (12 meses organizados) |
| 07 | CLIENTES | Rosa | Cadastros, Contratos, Notas Fiscais |
| 08 | FORNECEDORES | Cinza | Cadastros, Contratos, Pedidos |
| 09 | SISTEMAS | Roxo | Código-fonte, Scripts, Projetos |
| 10 | BACKUP | Cinza | Backups Diários/Semanais/Mensais |
| 11 | VIDEOS | Vermelho | Tutoriais, Segurança, Reuniões |
| 12 | PRINTS_TELA | Azul | Screenshots, Evidências |
| 13 | SEGURANCA_FRAUDES | Vermelho | Fraudes, Cheques Suspeitos |

## Scripts Principais

### `importador_universal.py`
Script principal para importação e classificação de arquivos.

**Uso:**
```bash
# Importar pasta inteira
python3 scripts/importador_universal.py ~/Downloads

# Importar arquivo específico
python3 scripts/importador_universal.py ~/Desktop/documento.pdf

# Modo simulação (dry-run)
python3 scripts/importador_universal.py ~/Downloads --dry-run
```

**Funcionalidades:**
- Detecção automática de tipo por extensão e conteúdo
- Leitura de PDFs para classificação inteligente
- Reconhecimento de bancos, notas fiscais, contratos
- Identificação de documentos de segurança/fraude

### `organize_master.sh`
Cria a estrutura completa de pastas em `/Users/Shared/ENSIDE_ORGANIZADO/`.

### `gerar_html_completo.py`
Gera visualização HTML interativa com todas as pastas e filtros.

### `aplicar_cores_completo.sh`
Aplica cores/etiquetas nas pastas do Finder (requer `brew install tag`).

## Caminhos Importantes

```bash
# Sistema principal (instalação)
/Users/Shared/ENSIDE_ORGANIZADO/

# Workspace pessoal
~/WORKSPACE/

# Skill do Claude Code
~/.claude/skills/organize-pdfs/

# Visualização HTML
~/Desktop/SISTEMA_ENSIDE_COMPLETO.html
```

## Dependências

### Sistema
- **macOS** 10.15 (Catalina) ou superior
- **Python** 3.8+
- **tag** (opcional, para cores no Finder): `brew install tag`

### Python
```
PyPDF2>=3.0.0          # Leitura de PDFs
python-magic-bin>=0.4.14  # Detecção de tipos de arquivo
```

## Fluxo de Desenvolvimento

### Instalação
```bash
git clone https://github.com/ensideanderson-nova/ENSIDE-PUBLICO.git
cd ENSIDE-PUBLICO
bash install.sh
```

### Testando Alterações
```bash
# Testar importador em modo dry-run
python3 scripts/importador_universal.py ~/Downloads --dry-run

# Regenerar HTML
python3 scripts/gerar_html_completo.py
```

## GitHub Actions

### `claude.yml`
Integração com Claude Code Action. Ativado quando:
- Menção de `@claude` em issues ou comentários
- Menção em PRs ou reviews

### `claude-integration.yml`
Análise automática de issues e PRs usando Claude AI.

## Convenções para Assistentes de IA

### Ao Trabalhar com Este Repositório

1. **Idioma**: O projeto é em português brasileiro. Mantenha mensagens, comentários e documentação em português.

2. **Organização de Arquivos**:
   - Scripts Python vão em `scripts/`
   - Documentação em `docs/`
   - Workflows em `.github/workflows/`

3. **Estilo de Código**:
   - Python: Use docstrings em português
   - Bash: Comente seções principais
   - Mantenha compatibilidade com macOS

4. **Ao Modificar Scripts**:
   - O `importador_universal.py` é o script principal - mudanças aqui afetam toda a classificação
   - Teste com `--dry-run` antes de aplicar mudanças reais
   - Os caminhos BASE e WORKSPACE são configurados no início dos scripts

5. **Detecção de Documentos**:
   - Palavras-chave para detecção estão em `PALAVRAS_CHAVE` no `importador_universal.py`
   - Mapeamento de extensões em `EXTENSOES`
   - Para adicionar novos tipos, modifique ambos os dicionários

6. **Sistema de Cores**:
   - Cores são aplicadas via utilitário `tag` do macOS
   - Configurações em `aplicar_cores_completo.sh`

### Comandos Úteis para Contexto

```bash
# Ver estrutura de categorias
ls /Users/Shared/ENSIDE_ORGANIZADO/

# Contar pastas no sistema
find /Users/Shared/ENSIDE_ORGANIZADO -type d | wc -l

# Ver logs de importação
python3 scripts/importador_universal.py ~/Downloads 2>&1 | tee log.txt

# Verificar skill do Claude Code
ls ~/.claude/skills/organize-pdfs/
```

### Ao Responder Usuários

1. **Para organizar arquivos**: Use `importador_universal.py`
2. **Para criar estrutura**: Use `organize_master.sh`
3. **Para visualizar sistema**: Use `gerar_html_completo.py`
4. **Para aplicar cores**: Use `aplicar_cores_completo.sh`

## Palavras-Chave de Detecção

O sistema detecta automaticamente os seguintes tipos:

### Bancário
`extrato`, `saldo`, `banco`, `itau`, `bradesco`, `santander`, `bb`, `caixa`, `nubank`

### Comprovantes
`comprovante`, `pix`, `ted`, `doc`, `transferencia`

### Documentos Fiscais
`nota fiscal`, `nf-e`, `nfe`, `danfe`, `boleto`

### Segurança
`fraude`, `golpe`, `suspeito`, `hack`, `exploit`, `malware`

### Documentos Pessoais
`cpf`, `rg`, `cnh`, `certidao`, `contrato`

## Licença

MIT License - Copyright (c) 2025 Anderson Enside

## Recursos Adicionais

- **Issues**: https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/issues
- **Documentação**: Ver `docs/` no repositório
- **Changelog**: Ver `CHANGELOG.md`

---

*Última atualização: 2025-11-25*
