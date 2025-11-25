# Sistema ENSIDE - Organizacao Inteligente de Documentos v2.0

[![Claude AI Integration](https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/actions/workflows/claude-integration.yml/badge.svg)](https://github.com/ensideanderson-nova/ENSIDE-PUBLICO/actions/workflows/claude-integration.yml)

Sistema completo de organizacao automatica de arquivos e documentos com deteccao inteligente, categorizacao por cores e interface HTML interativa.

## Visao Geral

O Sistema ENSIDE organiza automaticamente seus documentos em **15 categorias** principais, com deteccao inteligente de conteudo, aplicacao de cores no Finder do macOS e visualizacao HTML interativa.

### Principais Caracteristicas

- **15 categorias** principais com codigos de cores
- **Deteccao inteligente** de tipos de documento (PDFs, extratos bancarios, notas fiscais, etc)
- **Sistema de cores** no Finder do macOS
- **Dashboard HTML** interativo com filtros e busca
- **Triagem automatica** por palavras-chave
- **Tags e etiquetas** para organizacao visual
- **Integracao com Claude Code** via skill personalizada

## Estrutura de Categorias (15)

| # | Categoria | Cor Finder | Tags | Descricao |
|---|-----------|------------|------|-----------|
| 01 | INBOX | Roxo | Pessoal, Urgente | Triagem de novos arquivos |
| 02 | DOCUMENTOS_PESSOAIS | Azul | Pessoal, Sensivel | CPF, RG, CNH, Certidoes |
| 03 | FINANCEIRO | Verde | Empresa, Sensivel | Bancos, Impostos, Investimentos |
| 04 | JURIDICO | Vermelho | Empresa, Urgente | Contratos, Processos, CNPJ |
| 05 | SAUDE | Cinza | Pessoal, Sensivel | Exames, Receitas, Planos |
| 06 | IMOVEIS | Laranja | Pessoal, Sensivel | Escrituras, IPTU, Condominios |
| 07 | VEICULOS | Roxo | Pessoal | CRLV, Multas, Seguros |
| 08 | EDUCACAO | Azul | Pessoal | Diplomas, Certificados, Cursos |
| 09 | TRABALHO | Laranja | Pessoal, Empresa | Curriculos, Holerites, CTPS |
| 10 | PROJETOS | Roxo | Empresa, Tecnico | Desenvolvimento, Sistemas |
| 11 | MIDIA | Amarelo | Pessoal | Fotos, Videos, Musicas |
| 12 | COMUNICACAO | Verde | Empresa | Emails, Mensagens, Contatos |
| 13 | COMPRAS | Cinza | Pessoal, Empresa | Notas Fiscais, Garantias |
| 14 | SEGURANCA | Cinza | Sensivel, Tecnico | Certificados, Chaves, Senhas |
| 15 | BACKUP | Cinza | Tecnico | Backups, Arquivos Antigos |

## Instalacao Rapida

```bash
# Clonar o repositorio
git clone https://github.com/ensideanderson-nova/ENSIDE-PUBLICO.git

# Entrar no diretorio
cd ENSIDE-PUBLICO

# Executar instalacao
bash install.sh

# Criar estrutura de pastas
python3 scripts/triagem_universal.py --criar-estrutura

# Aplicar cores no Finder (macOS)
bash scripts/aplicar_cores_finder.sh
```

## Como Usar

### Opcao 1: Dashboard HTML

Abra o arquivo `DASHBOARD.html` no navegador para visualizar e navegar pelas categorias:

```bash
open DASHBOARD.html
```

### Opcao 2: Linha de Comando

```bash
# Organizar pasta Downloads
python3 scripts/triagem_universal.py ~/Downloads

# Organizar arquivo especifico
python3 scripts/triagem_universal.py ~/Desktop/documento.pdf

# Modo simulacao (nao move arquivos)
python3 scripts/triagem_universal.py ~/Downloads --dry-run

# Criar estrutura de pastas
python3 scripts/triagem_universal.py --criar-estrutura
```

### Opcao 3: Claude Code (Recomendado)

Simplesmente peca ao Claude:
- "Organiza os arquivos da pasta Downloads"
- "Importa esta pasta para o sistema"
- "Classifica estes documentos"

## Deteccao Inteligente

O sistema reconhece automaticamente:

### Documentos Pessoais
- CPF, RG, CNH -> `02_DOCUMENTOS_PESSOAIS/`
- Certidoes -> `02_DOCUMENTOS_PESSOAIS/Certidoes/`
- Comprovantes de residencia -> `02_DOCUMENTOS_PESSOAIS/Comprovantes/`

### Financeiro
- Extratos bancarios -> `03_FINANCEIRO/Bancos/`
- Impostos (IRPF, DARF) -> `03_FINANCEIRO/Impostos/`
- Boletos -> `03_FINANCEIRO/Boletos/`
- Investimentos -> `03_FINANCEIRO/Investimentos/`

### Juridico
- Contratos -> `04_JURIDICO/Contratos/`
- CNPJ, Contrato Social -> `04_JURIDICO/CNPJ/`
- Processos -> `04_JURIDICO/Processos/`

### Saude
- Exames -> `05_SAUDE/Exames/`
- Receitas medicas -> `05_SAUDE/Receitas/`
- Vacinas -> `05_SAUDE/Vacinas/`

### Midia
- Fotos (.jpg, .png) -> `11_MIDIA/Fotos/`
- Videos (.mp4, .mov) -> `11_MIDIA/Videos/`
- Screenshots -> `11_MIDIA/Screenshots/`

### Seguranca
- Certificados digitais -> `14_SEGURANCA/Certificados_Digitais/`
- Chaves SSH -> `14_SEGURANCA/Chaves_SSH/`

## Dashboard HTML

O arquivo `DASHBOARD.html` oferece:

- **15 categorias** com cores e icones
- **Busca em tempo real** por nome de arquivo
- **Filtros por tags**: Todas, Pessoal, Empresa, Urgente, Sensivel, Tecnico
- **Visualizacao em grade ou lista**
- **Subcategorias expansiveis** em cada card
- **Modal de importacao** de arquivos
- **Estatisticas** do sistema

### Abrindo o Dashboard

```bash
# macOS
open DASHBOARD.html

# Linux
xdg-open DASHBOARD.html

# Windows
start DASHBOARD.html
```

## Sistema de Cores no Finder

Aplique cores nas pastas do macOS:

```bash
bash scripts/aplicar_cores_finder.sh
```

### Paleta de Cores
| Cor | Codigo | Categorias |
|-----|--------|------------|
| Roxo | 3 | INBOX, Veiculos, Projetos |
| Azul | 4 | Documentos Pessoais, Educacao |
| Verde | 2 | Financeiro, Comunicacao |
| Vermelho | 6 | Juridico |
| Laranja | 7 | Imoveis, Trabalho |
| Amarelo | 5 | Midia |
| Cinza | 1 | Saude, Compras, Seguranca, Backup |

## Scripts Disponiveis

### Organizacao
```bash
# Triagem universal (recomendado)
python3 scripts/triagem_universal.py [PASTA]

# Criar estrutura
python3 scripts/triagem_universal.py --criar-estrutura

# Importador universal (legado)
python3 scripts/importador_universal.py [PASTA]
```

### Cores
```bash
# Aplicar cores Finder
bash scripts/aplicar_cores_finder.sh

# Cores completas (legado)
bash scripts/aplicar_cores_completo.sh
```

### Visualizacao
```bash
# Abrir dashboard
open DASHBOARD.html
```

## Estrutura de Arquivos

```
ENSIDE-PUBLICO/
├── DASHBOARD.html          # Interface web
├── CLAUDE.md               # Guia para AI
├── README.md               # Este arquivo
├── install.sh              # Instalador
├── scripts/
│   ├── triagem_universal.py      # Organizador principal
│   ├── aplicar_cores_finder.sh   # Cores macOS
│   ├── importador_universal.py   # Importador (legado)
│   └── ...
├── docs/
│   ├── INSTALLATION.md
│   └── EXEMPLOS.md
└── .github/
    └── workflows/          # CI/CD
```

## Estrutura de Destino

```
/Users/Shared/ENSIDE_ORGANIZADO/
├── 01_INBOX/
│   ├── Para_Classificar/
│   ├── Downloads/
│   └── Emails/
├── 02_DOCUMENTOS_PESSOAIS/
│   ├── CPF/
│   ├── RG/
│   ├── CNH/
│   └── ...
├── 03_FINANCEIRO/
│   ├── Bancos/
│   ├── Impostos/
│   └── ...
...
└── 15_BACKUP/
    ├── Diario/
    ├── Semanal/
    └── Mensal/
```

## Requisitos

- macOS 10.15+ (ou Linux/Windows para scripts Python)
- Python 3.8+
- Navegador moderno (para Dashboard)

```bash
pip3 install -r requirements.txt
```

## Contribuindo

Contribuicoes sao bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudancas (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licenca

Este projeto esta sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Creditos

Desenvolvido por Anderson Enside
Powered by Claude AI (Anthropic)

---

**Comece agora:**
```bash
python3 scripts/triagem_universal.py ~/Downloads --dry-run
```
