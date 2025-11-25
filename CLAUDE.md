Revisado e padronizado em 2025-11-25 — Versão 4.1

# CLAUDE.md - Guia para assistentes de IA

Este documento fornece orientações para assistentes de IA (como Claude) que trabalham com o repositório **Sistema ENSIDE v2.0**.

## Visão geral do projeto

O **Sistema ENSIDE** é um sistema de organização inteligente de documentos. Ele organiza automaticamente arquivos e documentos em uma estrutura hierárquica de **15 categorias**, com:

- **Detecção inteligente** de tipos de documento (PDFs, extratos bancários, notas fiscais etc.)
- **Sistema de cores** integrado ao Finder do macOS
- **Dashboard HTML** interativo com filtros e busca
- **Tags e etiquetas** para organização visual
- **Skill para Claude Code** para comandos em linguagem natural

### Propósito principal
Automatizar a organização de documentos pessoais e empresariais, incluindo:
- Documentos pessoais (CPF, RG, CNH)
- Financeiro (bancos, impostos, investimentos)
- Jurídico (contratos, processos, CNPJ)
- Saúde (exames, receitas, vacinas)
- Mídia (fotos, vídeos, músicas)
- E muito mais...

## Estrutura do repositório

```
ENSIDE-PUBLICO/
├── DASHBOARD.html            # Interface web interativa (15 categorias)
├── CLAUDE.md                 # Este arquivo - guia para IA
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

## Estrutura de categorias (15)

O sistema organiza documentos em **15 categorias** principais:

| #  | Categoria                 | Cor Finder | Tags                     | Descrição                                  |
|----|--------------------------:|:----------:|:------------------------:|--------------------------------------------|
| 01 | 01_INBOX                 | Roxo (3)   | Pessoal, Urgente         | Triagem de novos arquivos                  |
| 02 | 02_DOCUMENTOS_PESSOAIS   | Azul (4)   | Pessoal, Sensível        | CPF, RG, CNH, certidões                    |
| 03 | 03_FINANCEIRO            | Verde (2)  | Empresa, Sensível        | Bancos, impostos, investimentos            |
| 04 | 04_JURIDICO             | Vermelho (6)| Empresa, Urgente        | Contratos, processos, CNPJ                 |
| 05 | 05_SAUDE                | Cinza (1)  | Pessoal, Sensível        | Exames, receitas, planos                   |
| 06 | 06_IMOVEIS              | Laranja (7) | Pessoal, Sensível       | Escrituras, IPTU, condomínios              |
| 07 | 07_VEICULOS             | Roxo (3)   | Pessoal                  | CRLV, multas, seguros                      |
| 08 | 08_EDUCACAO            | Azul (4)   | Pessoal                  | Diplomas, certificados, cursos             |
| 09 | 09_TRABALHO            | Laranja (7) | Pessoal, Empresa        | Currículos, holerites, CTPS                |
| 10 | 10_PROJETOS            | Roxo (3)   | Empresa, Técnico         | Desenvolvimento, sistemas                  |
| 11 | 11_MIDIA               | Amarelo (5)| Pessoal                  | Fotos, vídeos, músicas                     |
| 12 | 12_COMUNICACAO         | Verde (2)  | Empresa                  | Emails, mensagens, contatos                |
| 13 | 13_COMPRAS             | Cinza (1)  | Pessoal, Empresa         | Notas fiscais, garantias                   |
| 14 | 14_SEGURANCA           | Cinza (1)  | Sensível, Técnico        | Certificados, chaves, senhas               |
| 15 | 15_BACKUP              | Cinza (1)  | Técnico                  | Backups, arquivos antigos                  |

### Subcategorias por categoria

Cada categoria tem subcategorias específicas. Exemplo de estrutura:

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

## Scripts principais

### `triagem_universal.py` (RECOMENDADO)
Script principal para organização com 15 categorias.

Uso:
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

Uso:
```bash
bash scripts/aplicar_cores_finder.sh
```

### `DASHBOARD.html`
Interface web interativa para visualizar e navegar nas categorias.

Funcionalidades:
- 15 categorias com cores e ícones
- Busca em tempo real
- Filtros por tags (Pessoal, Empresa, Urgente, Sensível, Técnico)
- Visualização em grade ou lista
- Subcategorias expansíveis
- Modal de importação

## Caminhos importantes

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

## Convenções para assistentes de IA

### Ao trabalhar com este repositório

1. **Idioma**: O projeto é em português brasileiro. Mantenha mensagens e documentação em português.
2. **Organização de arquivos**:
   - Scripts Python ficam em `scripts/`
   - Documentação em `docs/`
   - Interface web em `DASHBOARD.html` na raiz
3. **Ao modificar scripts**:
   - `triagem_universal.py` é o script principal
   - Teste com `--dry-run` antes de aplicar mudanças
   - As 15 categorias estão definidas no dicionário `CATEGORIAS`
   - As regras de palavras-chave estão em `PALAVRAS_CHAVE`
4. **Sistema de cores**:
   - Cores do Finder: 0=None, 1=Gray, 2=Green, 3=Purple, 4=Blue, 5=Yellow, 6=Red, 7=Orange
   - Configurações em `aplicar_cores_finder.sh`

### Comandos úteis

```bash
# Abrir o Dashboard
open DASHBOARD.html

# Organizar arquivos (simulação)
python3 scripts/triagem_universal.py ~/Downloads --dry-run

# Criar estrutura
python3 scripts/triagem_universal.py --criar-estrutura

# Aplicar cores (macOS)
bash scripts/aplicar_cores_finder.sh
```

### Ao responder usuários

1. **Para organizar arquivos**: Use `triagem_universal.py`
2. **Para visualizar o sistema**: Abra `DASHBOARD.html`
3. **Para aplicar cores**: Use `aplicar_cores_finder.sh`
4. **Para criar estrutura**: Use `--criar-estrutura`

## Palavras-chave de detecção

O sistema detecta automaticamente os seguintes termos (exemplos padronizados em minúsculas onde aplicável):

### Documentos pessoais
cpf, rg, cnh, certidao, nascimento, casamento, comprovante residencia

### Financeiro
extrato, banco, itau, bradesco, santander, nubank, imposto, irpf, boleto

### Jurídico
contrato, processo, procuracao, cnpj, contrato social

### Saúde
exame, receita, vacina, plano de saúde, unimed

### Veículos
crlv, ipva, multa, seguro auto, renavam

### Educação
diploma, certificado, curso, historico escolar

### Trabalho
curriculo, holerite, ctps, inss, fgts

### Compras
nota fiscal, garantia, manual

### Segurança
certificado digital, ssh, password, 2fa

## Licença

MIT License — Copyright (c) 2025 Anderson Enside

## Recursos adicionais

- **Dashboard**: `DASHBOARD.html`
- **Issues**: https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/issues
- **Documentação**: ver `docs/` no repositório

---

## Sistema MEGA (45 categorias)

O sistema também suporta a versão MEGA com 45 categorias especializadas para empresas do setor madeireiro:

### Grupos de categorias MEGA

| Grupo | Categorias | Descrição |
|-------|------------|----------|
| Documentos     | 01–05  | INBOX, Pessoais, Empresa, CV/Lattes, Viagens |
| Produtos Madeira | 06–11 | Pinus, Eucalipto, Especial, Preços, Peso/Umidade, Catálogos |
| Logística      | 12–16 | Fretes, Rastreamento, NFes/CTRC, Tributária, Seguros |
| Financeiro     | 17–21 | Receitas, Despesas, Conciliação, Impostos, Recibos |
| Bancos         | 22–24 | Dados, Transferências, Linhas de crédito |
| Clientes       | 25–29 | Cotações, Pedidos, Faturamento, Negociações, Reclamações |
| Fornecedores   | 30–33 | Cadastro, Contratos, Compras, Negócios |
| Projetos       | 34–36 | Planejamento, Execução, Documentação |
| Desenvolvimento| 37–41 | Python, JavaScript, SQL, APIs, Docs técnica |
| Sistemas       | 42–45 | Backup, Logs/Configs, Segurança/Senhas, Arquivos antigos |

### Comandos sistema MEGA

```bash
# Criar estrutura MEGA (45 pastas + arquivos exemplo)
python3 scripts/triagem_mega_45.py --criar-estrutura

# Organizar arquivos com 45 categorias
python3 scripts/triagem_mega_45.py ~/Downloads

# Abrir Dashboard MEGA
open DASHBOARD_MEGA_45.html
```

---

Última atualização: 2025-11-25
Versão: 4.1
