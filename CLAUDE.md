# CLAUDE.md - Guia para Assistentes de IA

> **Revisado e padronizado em 2025-11-25 — Versão 4.1**

Este documento fornece orientações para assistentes de IA (como Claude) que trabalham com o repositório **Sistema ENSIDE v2.0**.

## Visão Geral do Projeto

O **Sistema ENSIDE** é um sistema de organização inteligente de documentos. Ele organiza automaticamente arquivos e documentos em uma estrutura hierárquica de **15 categorias**, com:

- **Detecção inteligente** de tipos de documento (PDFs, extratos bancários, notas fiscais, etc.)
- **Sistema de cores** integrado com o Finder do macOS
- **Dashboard HTML** interativo com filtros e busca
- **Tags e etiquetas** para organização visual
- **Skill para Claude Code** para comandos de linguagem natural

### Propósito Principal
Automatizar a organização de documentos pessoais e empresariais, incluindo:
- Documentos pessoais (CPF, RG, CNH)
- Financeiro (bancos, impostos, investimentos)
- Jurídico (contratos, processos, CNPJ)
- Saúde (exames, receitas, vacinas)
- Mídia (fotos, vídeos, músicas)
- E muito mais...

## Estrutura do Repositório

```
ENSIDE-PUBLICO/
├── DASHBOARD.html            # Interface web interativa (15 categorias)
├── CLAUDE.md                 # Este arquivo — guia para IA
├── README.md                 # Documentação principal
├── CHANGELOG.md              # Histórico de versões
├── LICENSE                   # Licença MIT
├── install.sh                # Script de instalação
├── requirements.txt          # Dependências Python
│
├── docs/                     # Documentação adicional
│   ├── INSTALLATION.md       # Guia de instalação
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
    ├── claude.yml            # Integração Claude
    └── ...
```

## Estrutura de Categorias (15)

O sistema organiza documentos em **15 categorias** principais:

| #  | Categoria           | Cor Finder   | Tags              | Descrição                         |
|----|---------------------|--------------|-------------------|-----------------------------------|
| 01 | INBOX               | Roxo (3)     | Pessoal, Urgente  | Triagem de novos arquivos         |
| 02 | DOCUMENTOS_PESSOAIS | Azul (4)     | Pessoal, Sensível | CPF, RG, CNH, Certidões           |
| 03 | FINANCEIRO          | Verde (2)    | Empresa, Sensível | Bancos, Impostos, Investimentos   |
| 04 | JURIDICO            | Vermelho (6) | Empresa, Urgente  | Contratos, Processos, CNPJ        |
| 05 | SAUDE               | Cinza (1)    | Pessoal, Sensível | Exames, Receitas, Planos          |
| 06 | IMOVEIS             | Laranja (7)  | Pessoal, Sensível | Escrituras, IPTU, Condomínios     |
| 07 | VEICULOS            | Roxo (3)     | Pessoal           | CRLV, Multas, Seguros             |
| 08 | EDUCACAO            | Azul (4)     | Pessoal           | Diplomas, Certificados, Cursos    |
| 09 | TRABALHO            | Laranja (7)  | Pessoal, Empresa  | Currículos, Holerites, CTPS       |
| 10 | PROJETOS            | Roxo (3)     | Empresa, Técnico  | Desenvolvimento, Sistemas         |
| 11 | MIDIA               | Amarelo (5)  | Pessoal           | Fotos, Vídeos, Músicas            |
| 12 | COMUNICACAO         | Verde (2)    | Empresa           | E-mails, Mensagens, Contatos      |
| 13 | COMPRAS             | Cinza (1)    | Pessoal, Empresa  | Notas Fiscais, Garantias          |
| 14 | SEGURANCA           | Cinza (1)    | Sensível, Técnico | Certificados, Chaves, Senhas      |
| 15 | BACKUP              | Cinza (1)    | Técnico           | Backups, Arquivos Antigos         |

### Subcategorias por Categoria

Cada categoria tem subcategorias específicas:

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

... (cada categoria segue padrão similar)
```

## Scripts Principais

### `triagem_universal.py` (RECOMENDADO)
Script principal para organização com 15 categorias.

**Uso:**
```bash
# Organizar pasta
python3 scripts/triagem_universal.py ~/Downloads

# Modo simulação
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
- 15 categorias com cores e ícones
- Busca em tempo real
- Filtros por tags (Pessoal, Empresa, Urgente, Sensível, Técnico)
- Visualização em grade ou lista
- Subcategorias expansíveis
- Modal de importação

## Caminhos Importantes

```bash
# Sistema principal
~/ENSIDE_ORGANIZADO/

# Categorias
~/ENSIDE_ORGANIZADO/01_INBOX/
~/ENSIDE_ORGANIZADO/02_DOCUMENTOS_PESSOAIS/
... (até 15_BACKUP/)
```

## Dependências

### Sistema
- **macOS** 10.15+ ou Linux/Windows
- **Python** 3.8+
- Navegador moderno (para o Dashboard)

### Python
```
PyPDF2>=3.0.0
```

## Convenções para Assistentes de IA

### Ao Trabalhar com Este Repositório

1. **Idioma**: O projeto é em Português Brasileiro. Mantenha mensagens e documentação em português.

2. **Organização de Arquivos**:
   - Scripts Python vão em `scripts/`
   - Documentação em `docs/`
   - Interface web é `DASHBOARD.html` na raiz

3. **Ao Modificar Scripts**:
   - O `triagem_universal.py` é o script principal
   - Teste com `--dry-run` antes de aplicar mudanças
   - As 15 categorias estão definidas no dicionário `CATEGORIAS`
   - As regras de palavras-chave estão em `PALAVRAS_CHAVE`

4. **Sistema de Cores**:
   - Cores do Finder: 0=None, 1=Gray, 2=Green, 3=Purple, 4=Blue, 5=Yellow, 6=Red, 7=Orange
   - Configurações em `aplicar_cores_finder.sh`

### Comandos Úteis

```bash
# Abrir Dashboard
open DASHBOARD.html

# Organizar arquivos (simulação)
python3 scripts/triagem_universal.py ~/Downloads --dry-run

# Criar estrutura
python3 scripts/triagem_universal.py --criar-estrutura

# Aplicar cores (macOS)
bash scripts/aplicar_cores_finder.sh
```

### Ao Responder Usuários

1. **Para organizar arquivos**: Use `triagem_universal.py`
2. **Para visualizar o sistema**: Abra `DASHBOARD.html`
3. **Para aplicar cores**: Use `aplicar_cores_finder.sh`
4. **Para criar estrutura**: Use `--criar-estrutura`

## Palavras-Chave de Detecção

O sistema detecta automaticamente os seguintes tipos:

### Documentos Pessoais
`cpf`, `rg`, `cnh`, `certidão`, `nascimento`, `casamento`, `comprovante de residência`

### Financeiro
`extrato`, `banco`, `itaú`, `bradesco`, `santander`, `nubank`, `imposto`, `irpf`, `boleto`

### Jurídico
`contrato`, `processo`, `procuração`, `cnpj`, `contrato social`

### Saúde
`exame`, `receita`, `vacina`, `plano de saúde`, `unimed`

### Veículos
`crlv`, `ipva`, `multa`, `seguro auto`, `renavam`

### Educação
`diploma`, `certificado`, `curso`, `histórico escolar`

### Trabalho
`currículo`, `holerite`, `ctps`, `inss`, `fgts`

### Compras
`nota fiscal`, `garantia`, `manual`

### Segurança
`certificado digital`, `ssh`, `password`, `2fa`

## Licença

MIT License — Copyright (c) 2025 Anderson Enside

## Recursos Adicionais

- **Dashboard**: `DASHBOARD.html`
- **Issues**: https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/issues
- **Documentação**: Visualizar `docs/` no repositório

---

## Sistema MEGA (45 Categorias)

O sistema também suporta a versão MEGA com 45 categorias especializadas para empresas do setor madeireiro:

### Grupos de Categorias MEGA

| Grupo           | Categorias | Descrição                                           |
|-----------------|------------|-----------------------------------------------------|
| Documentos      | 01-05      | INBOX, Pessoais, Empresa, CV/Lattes, Viagens        |
| Produtos Madeira| 06-11      | Pinus, Eucalipto, Especial, Preços, Peso/Umidade, Catálogos |
| Logística       | 12-16      | Fretes, Rastreamento, NFes/CTRC, Tributária, Seguros|
| Financeiro      | 17-21      | Receitas, Despesas, Conciliação, Impostos, Recibos  |
| Bancos          | 22-24      | Dados, Transferências, Linhas de Crédito            |
| Clientes        | 25-29      | Cotações, Pedidos, Faturamento, Negociações, Reclamações |
| Fornecedores    | 30-33      | Cadastro, Contratos, Compras, Negócios              |
| Projetos        | 34-36      | Planejamento, Execução, Documentação                |
| Desenvolvimento | 37-41      | Python, JavaScript, SQL, APIs, Docs Técnica         |
| Sistemas        | 42-45      | Backup, Logs/Configs, Segurança/Senhas, Arquivos Antigos |

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

*Última atualização: 2025-11-25*  
*Versão: 4.1*
