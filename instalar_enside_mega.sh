#!/bin/bash
#
# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║                    INSTALADOR ENSIDE MEGA v4.0                             ║
# ║                                                                            ║
# ║              45 Categorias | 45 Cores | 225+ Etiquetas                    ║
# ║                                                                            ║
# ╚════════════════════════════════════════════════════════════════════════════╝
#
# Uso: bash instalar_enside_mega.sh
#

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Configuracao
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENSIDE_BASE="/Users/Shared/ENSIDE_ORGANIZADO"
ENSIDE_MEGA="$HOME/Enside_Master_MEGA"

# Funcoes
print_header() {
    clear
    echo ""
    echo -e "${PURPLE}╔════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║                                                                            ║${NC}"
    echo -e "${PURPLE}║${WHITE}                    INSTALADOR ENSIDE MEGA v4.0                             ${PURPLE}║${NC}"
    echo -e "${PURPLE}║                                                                            ║${NC}"
    echo -e "${PURPLE}║${CYAN}              45 Categorias | 45 Cores | 225+ Etiquetas                    ${PURPLE}║${NC}"
    echo -e "${PURPLE}║                                                                            ║${NC}"
    echo -e "${PURPLE}╚════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_step() {
    echo -e "${BLUE}[$1/$2]${NC} ${WHITE}$3${NC}"
}

print_success() {
    echo -e "    ${GREEN}✓${NC} $1"
}

print_info() {
    echo -e "    ${CYAN}ℹ${NC} $1"
}

print_warning() {
    echo -e "    ${YELLOW}⚠${NC} $1"
}

# Verificar sistema
check_system() {
    print_step "1" "6" "Verificando sistema..."

    # Verificar Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1)
        print_success "Python encontrado: $PYTHON_VERSION"
    else
        print_warning "Python3 nao encontrado. Instalando..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            xcode-select --install 2>/dev/null || true
        fi
    fi

    # Verificar OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_success "Sistema: macOS"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        print_success "Sistema: Linux"
    else
        print_info "Sistema: $OSTYPE"
    fi

    echo ""
}

# Criar estrutura de diretorios
create_directories() {
    print_step "2" "6" "Criando estrutura de diretorios..."

    # Criar diretorio base
    mkdir -p "$ENSIDE_BASE"
    print_success "Diretorio base: $ENSIDE_BASE"

    # Criar diretorio MEGA
    mkdir -p "$ENSIDE_MEGA"
    print_success "Diretorio MEGA: $ENSIDE_MEGA"

    echo ""
}

# Copiar scripts
copy_scripts() {
    print_step "3" "6" "Copiando scripts..."

    # Copiar script de triagem MEGA
    if [ -f "$SCRIPT_DIR/scripts/triagem_mega_45.py" ]; then
        cp "$SCRIPT_DIR/scripts/triagem_mega_45.py" "$ENSIDE_MEGA/triagem_mega.py"
        chmod +x "$ENSIDE_MEGA/triagem_mega.py"
        print_success "triagem_mega.py copiado"
    fi

    # Copiar script de triagem universal
    if [ -f "$SCRIPT_DIR/scripts/triagem_universal.py" ]; then
        cp "$SCRIPT_DIR/scripts/triagem_universal.py" "$ENSIDE_BASE/triagem.py"
        chmod +x "$ENSIDE_BASE/triagem.py"
        print_success "triagem.py copiado"
    fi

    echo ""
}

# Copiar dashboards
copy_dashboards() {
    print_step "4" "6" "Copiando dashboards..."

    # Dashboard MEGA
    if [ -f "$SCRIPT_DIR/DASHBOARD_MEGA_45.html" ]; then
        cp "$SCRIPT_DIR/DASHBOARD_MEGA_45.html" "$ENSIDE_MEGA/DASHBOARD_MEGA.html"
        print_success "DASHBOARD_MEGA.html copiado"
    fi

    # Dashboard padrao
    if [ -f "$SCRIPT_DIR/DASHBOARD.html" ]; then
        cp "$SCRIPT_DIR/DASHBOARD.html" "$ENSIDE_BASE/DASHBOARD.html"
        print_success "DASHBOARD.html copiado"
    fi

    echo ""
}

# Executar triagem MEGA
run_mega_setup() {
    print_step "5" "6" "Configurando Sistema MEGA (45 categorias)..."

    cd "$ENSIDE_MEGA"

    if [ -f "triagem_mega.py" ]; then
        python3 triagem_mega.py --criar-estrutura 2>/dev/null || {
            print_warning "Executando setup manual..."
            # Criar pastas manualmente se o script falhar
            for i in $(seq -w 1 45); do
                case $i in
                    01) mkdir -p "${i}_INBOX" ;;
                    02) mkdir -p "${i}_DOCUMENTOS_PESSOAIS" ;;
                    03) mkdir -p "${i}_DOCUMENTOS_EMPRESA" ;;
                    04) mkdir -p "${i}_CV_LATTES" ;;
                    05) mkdir -p "${i}_VIAGENS_HOSPEDAGEM" ;;
                    06) mkdir -p "${i}_PRODUTOS_MADEIRA_PINUS" ;;
                    07) mkdir -p "${i}_PRODUTOS_MADEIRA_EUCALIPTO" ;;
                    08) mkdir -p "${i}_PRODUTOS_MADEIRA_ESPECIAL" ;;
                    09) mkdir -p "${i}_TABELAS_PRECOS" ;;
                    10) mkdir -p "${i}_PESO_UMIDADE" ;;
                    11) mkdir -p "${i}_CATALOGOS_FORNECEDORES" ;;
                    12) mkdir -p "${i}_LOGISTICA_FRETES" ;;
                    13) mkdir -p "${i}_RASTREAMENTO" ;;
                    14) mkdir -p "${i}_NFES_CTRC" ;;
                    15) mkdir -p "${i}_RETENCAO_TRIBUTARIA" ;;
                    16) mkdir -p "${i}_SEGUROS" ;;
                    17) mkdir -p "${i}_FINANCEIRO_RECEITAS" ;;
                    18) mkdir -p "${i}_FINANCEIRO_DESPESAS" ;;
                    19) mkdir -p "${i}_FINANCEIRO_CONCILIACAO" ;;
                    20) mkdir -p "${i}_FINANCEIRO_IMPOSTOS" ;;
                    21) mkdir -p "${i}_RECIBOS_COMPROVANTES" ;;
                    22) mkdir -p "${i}_BANCOS_DADOS" ;;
                    23) mkdir -p "${i}_BANCOS_TRANSFERENCIAS" ;;
                    24) mkdir -p "${i}_BANCOS_LINHAS_CREDITO" ;;
                    25) mkdir -p "${i}_CLIENTES_COTACOES" ;;
                    26) mkdir -p "${i}_CLIENTES_PEDIDOS" ;;
                    27) mkdir -p "${i}_CLIENTES_FATURAMENTO" ;;
                    28) mkdir -p "${i}_CLIENTES_NEGOCIACOES" ;;
                    29) mkdir -p "${i}_CLIENTES_RECLAMACOES" ;;
                    30) mkdir -p "${i}_FORNECEDORES_CADASTRO" ;;
                    31) mkdir -p "${i}_FORNECEDORES_CONTRATOS" ;;
                    32) mkdir -p "${i}_FORNECEDORES_COMPRAS" ;;
                    33) mkdir -p "${i}_FORNECEDORES_NEGOCIOS" ;;
                    34) mkdir -p "${i}_PROJETOS_PLANEJAMENTO" ;;
                    35) mkdir -p "${i}_PROJETOS_EXECUCAO" ;;
                    36) mkdir -p "${i}_PROJETOS_DOCUMENTACAO" ;;
                    37) mkdir -p "${i}_CODIGO_PYTHON" ;;
                    38) mkdir -p "${i}_CODIGO_JAVASCRIPT" ;;
                    39) mkdir -p "${i}_CODIGO_SQL_DATABASE" ;;
                    40) mkdir -p "${i}_APIS_INTEGRACAO" ;;
                    41) mkdir -p "${i}_DOCUMENTACAO_TECNICA" ;;
                    42) mkdir -p "${i}_SISTEMAS_BACKUP" ;;
                    43) mkdir -p "${i}_SISTEMAS_LOGS_CONFIGS" ;;
                    44) mkdir -p "${i}_SEGURANCA_SENHAS" ;;
                    45) mkdir -p "${i}_ARQUIVOS_ANTIGOS_BACKUP" ;;
                esac
            done
        }
        print_success "45 categorias criadas"
    fi

    echo ""
}

# Aplicar cores no Finder (macOS)
apply_finder_colors() {
    print_step "6" "6" "Aplicando cores no Finder..."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        if [ -f "$SCRIPT_DIR/scripts/aplicar_cores_finder.sh" ]; then
            bash "$SCRIPT_DIR/scripts/aplicar_cores_finder.sh" 2>/dev/null || {
                print_warning "Cores nao aplicadas (requer macOS)"
            }
            print_success "Cores aplicadas no Finder"
        fi
    else
        print_info "Cores do Finder apenas para macOS"
    fi

    echo ""
}

# Abrir dashboard
open_dashboard() {
    echo -e "${GREEN}════════════════════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "    ${WHITE}INSTALACAO CONCLUIDA!${NC}"
    echo ""
    echo -e "    ${CYAN}Sistema MEGA:${NC}"
    echo -e "        Pasta: $ENSIDE_MEGA"
    echo -e "        Dashboard: $ENSIDE_MEGA/DASHBOARD_MEGA.html"
    echo ""
    echo -e "    ${CYAN}Sistema Padrao:${NC}"
    echo -e "        Pasta: $ENSIDE_BASE"
    echo -e "        Dashboard: $ENSIDE_BASE/DASHBOARD.html"
    echo ""
    echo -e "${GREEN}════════════════════════════════════════════════════════════════════════════${NC}"
    echo ""

    # Perguntar se quer abrir
    read -p "Abrir Dashboard MEGA no navegador? (s/n): " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Ss]$ ]]; then
        if [[ "$OSTYPE" == "darwin"* ]]; then
            open "$ENSIDE_MEGA/DASHBOARD_MEGA.html"
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$ENSIDE_MEGA/DASHBOARD_MEGA.html"
        else
            echo ""
            echo -e "    Abra manualmente: ${CYAN}$ENSIDE_MEGA/DASHBOARD_MEGA.html${NC}"
        fi
    fi

    echo ""
    echo -e "${PURPLE}Obrigado por usar o Sistema ENSIDE MEGA!${NC}"
    echo ""
}

# Menu principal
show_menu() {
    print_header

    echo -e "${WHITE}Escolha uma opcao:${NC}"
    echo ""
    echo -e "    ${CYAN}1)${NC} Instalacao completa (MEGA + Padrao)"
    echo -e "    ${CYAN}2)${NC} Apenas Sistema MEGA (45 categorias)"
    echo -e "    ${CYAN}3)${NC} Apenas Sistema Padrao (15 categorias)"
    echo -e "    ${CYAN}4)${NC} Aplicar cores no Finder (macOS)"
    echo -e "    ${CYAN}5)${NC} Abrir Dashboard MEGA"
    echo -e "    ${CYAN}6)${NC} Abrir Dashboard Padrao"
    echo -e "    ${CYAN}0)${NC} Sair"
    echo ""
    read -p "Opcao: " choice

    case $choice in
        1)
            print_header
            check_system
            create_directories
            copy_scripts
            copy_dashboards
            run_mega_setup
            apply_finder_colors
            open_dashboard
            ;;
        2)
            print_header
            check_system
            mkdir -p "$ENSIDE_MEGA"
            copy_scripts
            cp "$SCRIPT_DIR/DASHBOARD_MEGA_45.html" "$ENSIDE_MEGA/DASHBOARD_MEGA.html" 2>/dev/null || true
            run_mega_setup
            echo -e "${GREEN}Sistema MEGA instalado em: $ENSIDE_MEGA${NC}"
            ;;
        3)
            print_header
            check_system
            mkdir -p "$ENSIDE_BASE"
            cp "$SCRIPT_DIR/scripts/triagem_universal.py" "$ENSIDE_BASE/triagem.py" 2>/dev/null || true
            cp "$SCRIPT_DIR/DASHBOARD.html" "$ENSIDE_BASE/DASHBOARD.html" 2>/dev/null || true
            python3 "$ENSIDE_BASE/triagem.py" --criar-estrutura 2>/dev/null || true
            echo -e "${GREEN}Sistema Padrao instalado em: $ENSIDE_BASE${NC}"
            ;;
        4)
            print_header
            apply_finder_colors
            ;;
        5)
            if [[ "$OSTYPE" == "darwin"* ]]; then
                open "$ENSIDE_MEGA/DASHBOARD_MEGA.html" 2>/dev/null || open "$SCRIPT_DIR/DASHBOARD_MEGA_45.html"
            else
                echo "Abra: $ENSIDE_MEGA/DASHBOARD_MEGA.html"
            fi
            ;;
        6)
            if [[ "$OSTYPE" == "darwin"* ]]; then
                open "$ENSIDE_BASE/DASHBOARD.html" 2>/dev/null || open "$SCRIPT_DIR/DASHBOARD.html"
            else
                echo "Abra: $ENSIDE_BASE/DASHBOARD.html"
            fi
            ;;
        0)
            echo "Ate logo!"
            exit 0
            ;;
        *)
            echo "Opcao invalida"
            sleep 1
            show_menu
            ;;
    esac
}

# Verificar argumentos
if [ "$1" == "--auto" ] || [ "$1" == "-a" ]; then
    # Instalacao automatica sem menu
    print_header
    check_system
    create_directories
    copy_scripts
    copy_dashboards
    run_mega_setup
    apply_finder_colors
    open_dashboard
elif [ "$1" == "--mega" ]; then
    # Apenas MEGA
    print_header
    mkdir -p "$ENSIDE_MEGA"
    cd "$ENSIDE_MEGA"
    cp "$SCRIPT_DIR/scripts/triagem_mega_45.py" ./triagem_mega.py 2>/dev/null || true
    cp "$SCRIPT_DIR/DASHBOARD_MEGA_45.html" ./DASHBOARD_MEGA.html 2>/dev/null || true
    python3 triagem_mega.py --criar-estrutura 2>/dev/null || true
    echo -e "${GREEN}Sistema MEGA instalado em: $ENSIDE_MEGA${NC}"
elif [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo ""
    echo "ENSIDE MEGA Installer"
    echo ""
    echo "Uso: bash instalar_enside_mega.sh [OPCAO]"
    echo ""
    echo "Opcoes:"
    echo "  --auto, -a    Instalacao automatica completa"
    echo "  --mega        Instalar apenas Sistema MEGA"
    echo "  --help, -h    Mostrar esta ajuda"
    echo ""
    echo "Sem opcoes: Mostra menu interativo"
    echo ""
else
    # Menu interativo
    show_menu
fi
