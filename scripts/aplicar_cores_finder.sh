#!/bin/bash
#
# APLICAR CORES FINDER - Sistema ENSIDE
# Aplica cores e etiquetas nas pastas usando macOS Finder tags
#
# Cores disponiveis no Finder:
# 0 = None, 1 = Gray, 2 = Green, 3 = Purple, 4 = Blue, 5 = Yellow, 6 = Red, 7 = Orange
#

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

BASE="$HOME/ENSIDE_ORGANIZADO"

echo ""
echo "============================================================"
echo "   APLICAR CORES FINDER - Sistema ENSIDE v2.0"
echo "============================================================"
echo ""

# Verificar se estamos no macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}ERRO: Este script requer macOS${NC}"
    exit 1
fi

# Funcao para aplicar cor usando osascript
aplicar_cor() {
    local pasta="$1"
    local cor="$2"  # 0-7
    local nome="$3"

    if [ -d "$pasta" ]; then
        osascript -e "tell application \"Finder\" to set label index of (POSIX file \"$pasta\" as alias) to $cor" 2>/dev/null
        echo -e "   ${GREEN}✓${NC} $nome (cor $cor)"
    else
        echo -e "   ${YELLOW}!${NC} $nome - nao existe"
    fi
}

# Funcao para aplicar tag usando 'tag' command (se disponivel)
aplicar_tag() {
    local pasta="$1"
    local tag="$2"

    if command -v tag &> /dev/null; then
        if [ -d "$pasta" ]; then
            tag -a "$tag" "$pasta" 2>/dev/null
        fi
    fi
}

echo -e "${CYAN}Aplicando cores nas categorias principais...${NC}"
echo ""

# ===============================================
# 01 - INBOX (Roxo - 3)
# ===============================================
echo -e "${PURPLE}01 - INBOX${NC}"
aplicar_cor "$BASE/01_INBOX" 3 "INBOX"
aplicar_tag "$BASE/01_INBOX" "Triagem"

for sub in Para_Classificar Downloads Emails; do
    aplicar_cor "$BASE/01_INBOX/$sub" 3 "  $sub"
done

# ===============================================
# 02 - DOCUMENTOS PESSOAIS (Azul - 4)
# ===============================================
echo ""
echo -e "${BLUE}02 - DOCUMENTOS PESSOAIS${NC}"
aplicar_cor "$BASE/02_DOCUMENTOS_PESSOAIS" 4 "DOCUMENTOS PESSOAIS"
aplicar_tag "$BASE/02_DOCUMENTOS_PESSOAIS" "Pessoal"

for sub in CPF RG CNH Certidoes Comprovantes Titulo_Eleitor Passaporte; do
    aplicar_cor "$BASE/02_DOCUMENTOS_PESSOAIS/$sub" 4 "  $sub"
done

# ===============================================
# 03 - FINANCEIRO (Verde - 2)
# ===============================================
echo ""
echo -e "${GREEN}03 - FINANCEIRO${NC}"
aplicar_cor "$BASE/03_FINANCEIRO" 2 "FINANCEIRO"
aplicar_tag "$BASE/03_FINANCEIRO" "Financeiro"

for sub in Bancos Impostos Investimentos Contas_Pagar Contas_Receber Extratos Boletos; do
    aplicar_cor "$BASE/03_FINANCEIRO/$sub" 2 "  $sub"
done

# ===============================================
# 04 - JURIDICO (Vermelho - 6)
# ===============================================
echo ""
echo -e "${RED}04 - JURIDICO${NC}"
aplicar_cor "$BASE/04_JURIDICO" 6 "JURIDICO"
aplicar_tag "$BASE/04_JURIDICO" "Juridico"

for sub in Contratos Processos Procuracoes CNPJ Alvaras Certidoes_Negativas; do
    aplicar_cor "$BASE/04_JURIDICO/$sub" 6 "  $sub"
done

# ===============================================
# 05 - SAUDE (Cinza - 1)
# ===============================================
echo ""
echo "05 - SAUDE"
aplicar_cor "$BASE/05_SAUDE" 1 "SAUDE"
aplicar_tag "$BASE/05_SAUDE" "Saude"

for sub in Exames Receitas Plano_Saude Vacinas Laudos Historico_Medico; do
    aplicar_cor "$BASE/05_SAUDE/$sub" 1 "  $sub"
done

# ===============================================
# 06 - IMOVEIS (Laranja - 7)
# ===============================================
echo ""
echo -e "${YELLOW}06 - IMOVEIS${NC}"
aplicar_cor "$BASE/06_IMOVEIS" 7 "IMOVEIS"
aplicar_tag "$BASE/06_IMOVEIS" "Imoveis"

for sub in Escrituras IPTU Condominio Contratos_Aluguel Fotos Reformas; do
    aplicar_cor "$BASE/06_IMOVEIS/$sub" 7 "  $sub"
done

# ===============================================
# 07 - VEICULOS (Roxo - 3)
# ===============================================
echo ""
echo -e "${PURPLE}07 - VEICULOS${NC}"
aplicar_cor "$BASE/07_VEICULOS" 3 "VEICULOS"
aplicar_tag "$BASE/07_VEICULOS" "Veiculos"

for sub in CRLV IPVA Multas Seguros Manutencao Compra_Venda; do
    aplicar_cor "$BASE/07_VEICULOS/$sub" 3 "  $sub"
done

# ===============================================
# 08 - EDUCACAO (Azul - 4)
# ===============================================
echo ""
echo -e "${BLUE}08 - EDUCACAO${NC}"
aplicar_cor "$BASE/08_EDUCACAO" 4 "EDUCACAO"
aplicar_tag "$BASE/08_EDUCACAO" "Educacao"

for sub in Diplomas Certificados Cursos Materiais Historicos; do
    aplicar_cor "$BASE/08_EDUCACAO/$sub" 4 "  $sub"
done

# ===============================================
# 09 - TRABALHO (Laranja - 7)
# ===============================================
echo ""
echo -e "${YELLOW}09 - TRABALHO${NC}"
aplicar_cor "$BASE/09_TRABALHO" 7 "TRABALHO"
aplicar_tag "$BASE/09_TRABALHO" "Trabalho"

for sub in Curriculos Holerites CTPS INSS_FGTS Rescisoes Ferias; do
    aplicar_cor "$BASE/09_TRABALHO/$sub" 7 "  $sub"
done

# ===============================================
# 10 - PROJETOS (Roxo - 3)
# ===============================================
echo ""
echo -e "${PURPLE}10 - PROJETOS${NC}"
aplicar_cor "$BASE/10_PROJETOS" 3 "PROJETOS"
aplicar_tag "$BASE/10_PROJETOS" "Tecnico"

for sub in Desenvolvimento Documentacao Design Backups Scripts; do
    aplicar_cor "$BASE/10_PROJETOS/$sub" 3 "  $sub"
done

# ===============================================
# 11 - MIDIA (Amarelo - 5)
# ===============================================
echo ""
echo -e "${YELLOW}11 - MIDIA${NC}"
aplicar_cor "$BASE/11_MIDIA" 5 "MIDIA"
aplicar_tag "$BASE/11_MIDIA" "Midia"

for sub in Fotos Videos Musicas Screenshots Apresentacoes; do
    aplicar_cor "$BASE/11_MIDIA/$sub" 5 "  $sub"
done

# ===============================================
# 12 - COMUNICACAO (Verde - 2)
# ===============================================
echo ""
echo -e "${GREEN}12 - COMUNICACAO${NC}"
aplicar_cor "$BASE/12_COMUNICACAO" 2 "COMUNICACAO"
aplicar_tag "$BASE/12_COMUNICACAO" "Comunicacao"

for sub in Emails_Importantes Contatos Whatsapp Telegram; do
    aplicar_cor "$BASE/12_COMUNICACAO/$sub" 2 "  $sub"
done

# ===============================================
# 13 - COMPRAS (Cinza - 1)
# ===============================================
echo ""
echo "13 - COMPRAS"
aplicar_cor "$BASE/13_COMPRAS" 1 "COMPRAS"
aplicar_tag "$BASE/13_COMPRAS" "Compras"

for sub in Notas_Fiscais Garantias Manuais Recibos; do
    aplicar_cor "$BASE/13_COMPRAS/$sub" 1 "  $sub"
done

# ===============================================
# 14 - SEGURANCA (Cinza - 1)
# ===============================================
echo ""
echo "14 - SEGURANCA"
aplicar_cor "$BASE/14_SEGURANCA" 1 "SEGURANCA"
aplicar_tag "$BASE/14_SEGURANCA" "Sensivel"

for sub in Certificados_Digitais Chaves_SSH 2FA_Backup Senhas_Backup; do
    aplicar_cor "$BASE/14_SEGURANCA/$sub" 1 "  $sub"
done

# ===============================================
# 15 - BACKUP (Cinza - 1)
# ===============================================
echo ""
echo "15 - BACKUP"
aplicar_cor "$BASE/15_BACKUP" 1 "BACKUP"
aplicar_tag "$BASE/15_BACKUP" "Backup"

for sub in Diario Semanal Mensal Arquivos_Antigos; do
    aplicar_cor "$BASE/15_BACKUP/$sub" 1 "  $sub"
done

echo ""
echo "============================================================"
echo -e "   ${GREEN}CORES APLICADAS COM SUCESSO!${NC}"
echo "============================================================"
echo ""
echo "   Pasta base: $BASE"
echo "   15 categorias coloridas"
echo ""
echo "   Legenda de cores Finder:"
echo "   1 = Cinza    | 2 = Verde   | 3 = Roxo"
echo "   4 = Azul     | 5 = Amarelo | 6 = Vermelho"
echo "   7 = Laranja"
echo ""
