# CLAUDE.md - Guia para Assistentes de IA

Este documento fornece orientacoes para assistentes de IA (como Claude) que trabalham com o repositorio **Sistema ENSIDE v2.0**.

## Visao Geral do Projeto

O **Sistema ENSIDE** e um sistema de organizacao inteligente de documentos. Ele organiza automaticamente arquivos e documentos em uma estrutura hierarquica de **15 categorias**, com:

- **Deteccao inteligente** de tipos de documento (PDFs, extratos bancarios, notas fiscais, etc.)
- **Sistema de cores** integrado com o Finder do macOS
- **Dashboard HTML** interativo com filtros e busca
- **Tags e etiquetas** para organizacao visual
- **Skill para Claude Code** para comandos de linguagem natural

### Proposito Principal
Automatizar a organizacao de documentos pessoais e empresariais, incluindo:
- Documentos pessoais (CPF, RG, CNH)
- Financeiro (bancos, impostos, investimentos)
- Juridico (contratos, processos, CNPJ)
- Saude (exames, receitas, vacinas)
- Midia (fotos, videos, musicas)
- E muito mais...

## Estrutura do Repositorio

```
ENSIDE-PUBLICO/
├── DASHBOARD.html            # Interface web interativa (15 categorias)
├── CLAUDE.md                 # Este arquivo - guia para AI
├── README.md                 # Documentacao principal
├── CHANGELOG.md              # Historico de versoes
├── LICENSE                   # Licenca MIT
├── install.sh                # Script de instalacao
├── requirements.txt          # Dependencias Python
│
├── docs/                     # Documentacao adicional
│   ├── INSTALLATION.md       # Guia de instalacao
│   └── EXEMPLOS.md           # Casos de uso
│
├── scripts/                  # Scripts principais
│   ├── triagem_universal.py       # Organizador principal (15 categorias)
│   ├── aplicar_cores_finder.sh    # Aplicador de cores no Finder
│   ├── importador_universal.py    # Importador (legado)
│   ├── organize_master.sh         # Criador da estrutura
│   ├── gerar_html_completo.py     # Gerador de HTML
│   └── ...
│
└── .github/workflows/        # GitHub Actions
    ├── claude.yml            # Integracao Claude
    └── ...
```

## Estrutura de Categorias (15)

O sistema organiza documentos em **15 categorias** principais:

| # | Categoria | Cor Finder | Tags | Descricao |
|---|-----------|------------|------|-----------|
| 01 | INBOX | Roxo (3) | Pessoal, Urgente | Triagem de novos arquivos |
| 02 | DOCUMENTOS_PESSOAIS | Azul (4) | Pessoal, Sensivel | CPF, RG, CNH, Certidoes |
| 03 | FINANCEIRO | Verde (2) | Empresa, Sensivel | Bancos, Impostos, Investimentos |
| 04 | JURIDICO | Vermelho (6) | Empresa, Urgente | Contratos, Processos, CNPJ |
| 05 | SAUDE | Cinza (1) | Pessoal, Sensivel | Exames, Receitas, Planos |
| 06 | IMOVEIS | Laranja (7) | Pessoal, Sensivel | Escrituras, IPTU, Condominios |
| 07 | VEICULOS | Roxo (3) | Pessoal | CRLV, Multas, Seguros |
| 08 | EDUCACAO | Azul (4) | Pessoal | Diplomas, Certificados, Cursos |
| 09 | TRABALHO | Laranja (7) | Pessoal, Empresa | Curriculos, Holerites, CTPS |
| 10 | PROJETOS | Roxo (3) | Empresa, Tecnico | Desenvolvimento, Sistemas |
| 11 | MIDIA | Amarelo (5) | Pessoal | Fotos, Videos, Musicas |
| 12 | COMUNICACAO | Verde (2) | Empresa | Emails, Mensagens, Contatos |
| 13 | COMPRAS | Cinza (1) | Pessoal, Empresa | Notas Fiscais, Garantias |
| 14 | SEGURANCA | Cinza (1) | Sensivel, Tecnico | Certificados, Chaves, Senhas |
| 15 | BACKUP | Cinza (1) | Tecnico | Backups, Arquivos Antigos |

### Subcategorias por Categoria

Cada categoria tem subcategorias especificas:

```
01_INBOX/
├── Para_Classificar/
├── Downloads/
└── Emails/

02_DOCUMENTOS_PESSOAIS/
├── CPF/
├── RG/
├── CNH/
├── Certidoes/
├── Comprovantes/
├── Titulo_Eleitor/
└── Passaporte/

03_FINANCEIRO/
├── Bancos/
├── Impostos/
├── Investimentos/
├── Contas_Pagar/
├── Contas_Receber/
├── Extratos/
└── Boletos/

... (cada categoria segue padrao similar)
```

## Scripts Principais

### `triagem_universal.py` (RECOMENDADO)
Script principal para organizacao com 15 categorias.

**Uso:**
```bash
# Organizar pasta
python3 scripts/triagem_universal.py ~/Downloads

# Modo simulacao
python3 scripts/triagem_universal.py ~/Downloads --dry-run

# Criar estrutura de pastas
python3 scripts/triagem_universal.py --criar-estrutura
```

### `aplicar_cores_finder.sh`
Aplica cores nas pastas do Finder (macOS).

**Uso:**
```bash
bash scripts/aplicar_cores_finder.sh
```

### `DASHBOARD.html`
Interface web interativa para visualizar e navegar nas categorias.

**Funcionalidades:**
- 15 categorias com cores e icones
- Busca em tempo real
- Filtros por tags (Pessoal, Empresa, Urgente, Sensivel, Tecnico)
- Visualizacao em grade ou lista
- Subcategorias expansiveis
- Modal de importacao

## Caminhos Importantes

```bash
# Sistema principal
/Users/Shared/ENSIDE_ORGANIZADO/

# Categorias
/Users/Shared/ENSIDE_ORGANIZADO/01_INBOX/
/Users/Shared/ENSIDE_ORGANIZADO/02_DOCUMENTOS_PESSOAIS/
... (ate 15_BACKUP/)
```

## Dependencias

### Sistema
- **macOS** 10.15+ ou Linux/Windows
- **Python** 3.8+
- Navegador moderno (para Dashboard)

### Python
```
PyPDF2>=3.0.0
```

## Convencoes para Assistentes de IA

### Ao Trabalhar com Este Repositorio

1. **Idioma**: O projeto e em portugues brasileiro. Mantenha mensagens e documentacao em portugues.

2. **Organizacao de Arquivos**:
   - Scripts Python vao em `scripts/`
   - Documentacao em `docs/`
   - Interface web e `DASHBOARD.html` na raiz

3. **Ao Modificar Scripts**:
   - O `triagem_universal.py` e o script principal
   - Teste com `--dry-run` antes de aplicar mudancas
   - As 15 categorias estao definidas no dicionario `CATEGORIAS`
   - As regras de palavras-chave estao em `PALAVRAS_CHAVE`

4. **Sistema de Cores**:
   - Cores do Finder: 0=None, 1=Gray, 2=Green, 3=Purple, 4=Blue, 5=Yellow, 6=Red, 7=Orange
   - Configuracoes em `aplicar_cores_finder.sh`

### Comandos Uteis

```bash
# Ver Dashboard
open DASHBOARD.html

# Organizar arquivos (simulacao)
python3 scripts/triagem_universal.py ~/Downloads --dry-run

# Criar estrutura
python3 scripts/triagem_universal.py --criar-estrutura

# Aplicar cores (macOS)
bash scripts/aplicar_cores_finder.sh
```

### Ao Responder Usuarios

1. **Para organizar arquivos**: Use `triagem_universal.py`
2. **Para visualizar sistema**: Abra `DASHBOARD.html`
3. **Para aplicar cores**: Use `aplicar_cores_finder.sh`
4. **Para criar estrutura**: Use `--criar-estrutura`

## Palavras-Chave de Deteccao

O sistema detecta automaticamente os seguintes tipos:

### Documentos Pessoais
`cpf`, `rg`, `cnh`, `certidao`, `nascimento`, `casamento`, `comprovante residencia`

### Financeiro
`extrato`, `banco`, `itau`, `bradesco`, `santander`, `nubank`, `imposto`, `irpf`, `boleto`

### Juridico
`contrato`, `processo`, `procuracao`, `cnpj`, `contrato social`

### Saude
`exame`, `receita`, `vacina`, `plano saude`, `unimed`

### Veiculos
`crlv`, `ipva`, `multa`, `seguro auto`, `renavam`

### Educacao
`diploma`, `certificado`, `curso`, `historico escolar`

### Trabalho
`curriculo`, `holerite`, `ctps`, `inss`, `fgts`

### Compras
`nota fiscal`, `garantia`, `manual`

### Seguranca
`certificado digital`, `ssh`, `password`, `2fa`

## Licenca

MIT License - Copyright (c) 2025 Anderson Enside

## Recursos Adicionais

- **Dashboard**: `DASHBOARD.html`
- **Issues**: https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/issues
- **Documentacao**: Ver `docs/` no repositorio

---

## Sistema MEGA (45 Categorias)

O sistema tambem suporta a versao MEGA com 45 categorias especializadas para empresas do setor madeireiro:

### Grupos de Categorias MEGA

| Grupo | Categorias | Descricao |
|-------|-----------|-----------|
| Documentos | 01-05 | INBOX, Pessoais, Empresa, CV/Lattes, Viagens |
| Produtos Madeira | 06-11 | Pinus, Eucalipto, Especial, Precos, Peso/Umidade, Catalogos |
| Logistica | 12-16 | Fretes, Rastreamento, NFes/CTRC, Tributaria, Seguros |
| Financeiro | 17-21 | Receitas, Despesas, Conciliacao, Impostos, Recibos |
| Bancos | 22-24 | Dados, Transferencias, Linhas Credito |
| Clientes | 25-29 | Cotacoes, Pedidos, Faturamento, Negociacoes, Reclamacoes |
| Fornecedores | 30-33 | Cadastro, Contratos, Compras, Negocios |
| Projetos | 34-36 | Planejamento, Execucao, Documentacao |
| Desenvolvimento | 37-41 | Python, JavaScript, SQL, APIs, Docs Tecnica |
| Sistemas | 42-45 | Backup, Logs/Configs, Seguranca/Senhas, Arquivos Antigos |

### Comandos Sistema MEGA

```bash
# Criar estrutura MEGA (45 pastas + arquivos exemplo)
python3 scripts/triagem_mega_45.py --criar-estrutura

# Organizar arquivos com 45 categorias
python3 scripts/triagem_mega_45.py ~/Downloads

# Abrir Dashboard MEGA
open DASHBOARD_MEGA_45.html
```

---

*Ultima atualizacao: 2025-11-25*
*Versao: 4.0 MEGA*
