#!/usr/bin/env python3
"""
TRIAGEM UNIVERSAL - Sistema de Organizacao de Arquivos ENSIDE
Classifica e organiza automaticamente arquivos em 15 categorias

Versao: 2.0
"""

import sys
import os
import shutil
from pathlib import Path
from datetime import datetime
import re
import json

# Configuracao
BASE = Path(os.path.expanduser("~/ENSIDE_ORGANIZADO"))

# ===============================================================================
# CATEGORIAS DO SISTEMA (15 categorias com cores e tags)
# ===============================================================================

CATEGORIAS = {
    "01_INBOX": {
        "nome": "INBOX",
        "descricao": "Triagem de novos arquivos",
        "cor_hex": "#9b59b6",
        "cor_finder": "Purple",
        "tags": ["pessoal", "urgente"],
        "subcategorias": ["Para_Classificar", "Downloads", "Emails"]
    },
    "02_DOCUMENTOS_PESSOAIS": {
        "nome": "Documentos Pessoais",
        "descricao": "CPF, RG, CNH, Certidoes",
        "cor_hex": "#3498db",
        "cor_finder": "Blue",
        "tags": ["pessoal", "sensivel"],
        "subcategorias": ["CPF", "RG", "CNH", "Certidoes", "Comprovantes", "Titulo_Eleitor", "Passaporte"]
    },
    "03_FINANCEIRO": {
        "nome": "Financeiro",
        "descricao": "Bancos, Impostos, Investimentos",
        "cor_hex": "#27ae60",
        "cor_finder": "Green",
        "tags": ["empresa", "sensivel"],
        "subcategorias": ["Bancos", "Impostos", "Investimentos", "Contas_Pagar", "Contas_Receber", "Extratos", "Boletos"]
    },
    "04_JURIDICO": {
        "nome": "Juridico",
        "descricao": "Contratos, Processos, Procuracoes",
        "cor_hex": "#e74c3c",
        "cor_finder": "Red",
        "tags": ["empresa", "urgente", "sensivel"],
        "subcategorias": ["Contratos", "Processos", "Procuracoes", "CNPJ", "Alvaras", "Certidoes_Negativas"]
    },
    "05_SAUDE": {
        "nome": "Saude",
        "descricao": "Exames, Receitas, Planos",
        "cor_hex": "#1abc9c",
        "cor_finder": "Gray",
        "tags": ["pessoal", "sensivel"],
        "subcategorias": ["Exames", "Receitas", "Plano_Saude", "Vacinas", "Laudos", "Historico_Medico"]
    },
    "06_IMOVEIS": {
        "nome": "Imoveis",
        "descricao": "Escrituras, IPTU, Condominios",
        "cor_hex": "#f39c12",
        "cor_finder": "Orange",
        "tags": ["pessoal", "sensivel"],
        "subcategorias": ["Escrituras", "IPTU", "Condominio", "Contratos_Aluguel", "Fotos", "Reformas"]
    },
    "07_VEICULOS": {
        "nome": "Veiculos",
        "descricao": "CRLV, Multas, Seguros",
        "cor_hex": "#e91e63",
        "cor_finder": "Purple",
        "tags": ["pessoal"],
        "subcategorias": ["CRLV", "IPVA", "Multas", "Seguros", "Manutencao", "Compra_Venda"]
    },
    "08_EDUCACAO": {
        "nome": "Educacao",
        "descricao": "Diplomas, Certificados, Cursos",
        "cor_hex": "#00bcd4",
        "cor_finder": "Blue",
        "tags": ["pessoal"],
        "subcategorias": ["Diplomas", "Certificados", "Cursos", "Materiais", "Historicos"]
    },
    "09_TRABALHO": {
        "nome": "Trabalho",
        "descricao": "Curriculos, Holerites, CTPS",
        "cor_hex": "#ff5722",
        "cor_finder": "Orange",
        "tags": ["pessoal", "empresa"],
        "subcategorias": ["Curriculos", "Holerites", "CTPS", "INSS_FGTS", "Rescisoes", "Ferias"]
    },
    "10_PROJETOS": {
        "nome": "Projetos",
        "descricao": "Desenvolvimento, Sistemas, Codigo",
        "cor_hex": "#673ab7",
        "cor_finder": "Purple",
        "tags": ["empresa", "tecnico"],
        "subcategorias": ["Desenvolvimento", "Documentacao", "Design", "Backups", "Scripts"]
    },
    "11_MIDIA": {
        "nome": "Midia",
        "descricao": "Fotos, Videos, Musicas",
        "cor_hex": "#ff9800",
        "cor_finder": "Yellow",
        "tags": ["pessoal"],
        "subcategorias": ["Fotos", "Videos", "Musicas", "Screenshots", "Apresentacoes"]
    },
    "12_COMUNICACAO": {
        "nome": "Comunicacao",
        "descricao": "Emails, Mensagens, Contatos",
        "cor_hex": "#4caf50",
        "cor_finder": "Green",
        "tags": ["empresa"],
        "subcategorias": ["Emails_Importantes", "Contatos", "Whatsapp", "Telegram"]
    },
    "13_COMPRAS": {
        "nome": "Compras",
        "descricao": "Notas Fiscais, Garantias, Manuais",
        "cor_hex": "#795548",
        "cor_finder": "Gray",
        "tags": ["pessoal", "empresa"],
        "subcategorias": ["Notas_Fiscais", "Garantias", "Manuais", "Recibos"]
    },
    "14_SEGURANCA": {
        "nome": "Seguranca",
        "descricao": "Senhas, Certificados, Chaves",
        "cor_hex": "#607d8b",
        "cor_finder": "Gray",
        "tags": ["sensivel", "tecnico"],
        "subcategorias": ["Certificados_Digitais", "Chaves_SSH", "2FA_Backup", "Senhas_Backup"]
    },
    "15_BACKUP": {
        "nome": "Backup",
        "descricao": "Backups, Arquivos Antigos",
        "cor_hex": "#9e9e9e",
        "cor_finder": "Gray",
        "tags": ["tecnico"],
        "subcategorias": ["Diario", "Semanal", "Mensal", "Arquivos_Antigos"]
    }
}

# ===============================================================================
# REGRAS DE CLASSIFICACAO
# ===============================================================================

# Extensoes de arquivo
EXTENSOES = {
    # Documentos
    'pdf': 'documento',
    'doc': 'documento', 'docx': 'documento', 'odt': 'documento',
    'txt': 'texto', 'rtf': 'texto',

    # Planilhas
    'xls': 'planilha', 'xlsx': 'planilha', 'ods': 'planilha', 'csv': 'planilha',

    # Apresentacoes
    'ppt': 'apresentacao', 'pptx': 'apresentacao', 'odp': 'apresentacao',

    # Imagens
    'jpg': 'imagem', 'jpeg': 'imagem', 'png': 'imagem', 'gif': 'imagem',
    'bmp': 'imagem', 'svg': 'imagem', 'webp': 'imagem', 'heic': 'imagem',
    'tiff': 'imagem', 'raw': 'imagem',

    # Videos
    'mp4': 'video', 'mov': 'video', 'avi': 'video', 'mkv': 'video',
    'wmv': 'video', 'flv': 'video', 'webm': 'video', 'm4v': 'video',

    # Audio
    'mp3': 'audio', 'wav': 'audio', 'aac': 'audio', 'flac': 'audio',
    'm4a': 'audio', 'ogg': 'audio', 'wma': 'audio',

    # Codigo
    'py': 'codigo', 'js': 'codigo', 'html': 'codigo', 'css': 'codigo',
    'java': 'codigo', 'cpp': 'codigo', 'c': 'codigo', 'sh': 'codigo',
    'rb': 'codigo', 'go': 'codigo', 'php': 'codigo', 'swift': 'codigo',
    'ts': 'codigo', 'jsx': 'codigo', 'tsx': 'codigo',

    # Compactados
    'zip': 'compactado', 'rar': 'compactado', '7z': 'compactado',
    'tar': 'compactado', 'gz': 'compactado', 'bz2': 'compactado',

    # Dados
    'json': 'dados', 'xml': 'dados', 'yaml': 'dados', 'yml': 'dados',
    'sql': 'dados', 'db': 'dados', 'sqlite': 'dados',

    # Seguranca
    'pem': 'certificado', 'crt': 'certificado', 'key': 'chave',
    'p12': 'certificado', 'pfx': 'certificado',
}

# Palavras-chave para classificacao
PALAVRAS_CHAVE = {
    # 02 - Documentos Pessoais
    'documentos_pessoais': {
        'cpf': ['cpf', 'cadastro pessoa fisica'],
        'rg': ['rg', 'identidade', 'registro geral'],
        'cnh': ['cnh', 'habilitacao', 'carteira motorista'],
        'certidao': ['certidao', 'nascimento', 'casamento', 'obito'],
        'comprovante': ['comprovante residencia', 'conta luz', 'conta agua'],
    },

    # 03 - Financeiro
    'financeiro': {
        'banco': ['extrato', 'saldo', 'banco', 'itau', 'bradesco', 'santander',
                  'bb', 'caixa', 'nubank', 'inter', 'c6', 'picpay'],
        'imposto': ['imposto', 'irpf', 'irpj', 'darf', 'das', 'inss', 'icms', 'iss'],
        'investimento': ['investimento', 'cdb', 'tesouro', 'acao', 'fundo', 'renda fixa'],
        'boleto': ['boleto', 'fatura', 'codigo barras', 'linha digitavel'],
        'cartao': ['cartao credito', 'cartao debito', 'fatura cartao'],
    },

    # 04 - Juridico
    'juridico': {
        'contrato': ['contrato', 'acordo', 'termo', 'clausula'],
        'processo': ['processo', 'acao judicial', 'sentenca', 'recurso'],
        'procuracao': ['procuracao', 'substabelecimento'],
        'cnpj': ['cnpj', 'contrato social', 'alteracao contratual', 'junta comercial'],
    },

    # 05 - Saude
    'saude': {
        'exame': ['exame', 'laboratorio', 'resultado', 'hemograma', 'ultrassom'],
        'receita': ['receita', 'prescricao', 'medicamento'],
        'plano': ['plano saude', 'unimed', 'amil', 'bradesco saude', 'sulamerica'],
        'vacina': ['vacina', 'vacinacao', 'imunizacao'],
    },

    # 06 - Imoveis
    'imoveis': {
        'escritura': ['escritura', 'matricula', 'registro imovel'],
        'iptu': ['iptu', 'imposto predial'],
        'condominio': ['condominio', 'taxa condominio', 'sindico'],
        'aluguel': ['aluguel', 'locacao', 'inquilino', 'locador'],
    },

    # 07 - Veiculos
    'veiculos': {
        'documento': ['crlv', 'crv', 'renavam', 'detran'],
        'ipva': ['ipva', 'licenciamento'],
        'multa': ['multa', 'infracao', 'auto infracao'],
        'seguro': ['seguro auto', 'apolice', 'sinistro'],
        'manutencao': ['revisao', 'troca oleo', 'manutencao', 'oficina'],
    },

    # 08 - Educacao
    'educacao': {
        'diploma': ['diploma', 'formatura', 'conclusao curso'],
        'certificado': ['certificado', 'conclusao', 'participacao'],
        'curso': ['curso', 'treinamento', 'capacitacao', 'workshop'],
        'material': ['apostila', 'material didatico', 'livro', 'ebook'],
    },

    # 09 - Trabalho
    'trabalho': {
        'curriculo': ['curriculo', 'cv', 'resume'],
        'holerite': ['holerite', 'contracheque', 'folha pagamento'],
        'ctps': ['ctps', 'carteira trabalho'],
        'inss': ['inss', 'fgts', 'contribuicao', 'previdencia'],
    },

    # 10 - Projetos (tecnico)
    'projetos': {
        'codigo': ['source', 'repository', 'git', 'branch', 'commit'],
        'documentacao': ['readme', 'changelog', 'documentation', 'api'],
        'design': ['wireframe', 'mockup', 'prototype', 'figma', 'sketch'],
    },

    # 11 - Midia
    'midia': {
        'foto': ['foto', 'imagem', 'picture', 'img', 'dcim'],
        'video': ['video', 'movie', 'clip', 'recording'],
        'musica': ['musica', 'music', 'song', 'album', 'playlist'],
        'screenshot': ['screenshot', 'captura', 'print', 'screen'],
    },

    # 13 - Compras
    'compras': {
        'nota_fiscal': ['nota fiscal', 'nfe', 'danfe', 'cupom fiscal'],
        'garantia': ['garantia', 'warranty', 'termo garantia'],
        'manual': ['manual', 'instrucoes', 'guia usuario'],
    },

    # 14 - Seguranca
    'seguranca': {
        'certificado_digital': ['certificado digital', 'e-cpf', 'e-cnpj', 'token'],
        'chave': ['ssh', 'private key', 'public key', 'pgp', 'gpg'],
        'senha': ['senha', 'password', '2fa', 'otp', 'backup codes'],
    },
}


class TriagemUniversal:
    """Sistema de triagem e classificacao de arquivos"""

    def __init__(self):
        self.stats = {
            'total': 0,
            'classificados': 0,
            'erros': 0,
            'por_categoria': {},
            'arquivos': []
        }

    def classificar_arquivo(self, arquivo):
        """
        Classifica um arquivo e retorna a categoria e subcategoria destino
        """
        arquivo = Path(arquivo)

        if not arquivo.exists() or not arquivo.is_file():
            return None

        nome = arquivo.name.lower()
        extensao = arquivo.suffix.lower().replace('.', '')
        tipo = EXTENSOES.get(extensao, 'outro')

        # Ler conteudo para analise (primeiros KB)
        conteudo = self._ler_conteudo(arquivo, tipo)
        texto_analise = f"{nome} {conteudo}".lower()

        # Classificar por regras
        categoria, subcategoria = self._aplicar_regras(
            arquivo, nome, extensao, tipo, texto_analise
        )

        return {
            'arquivo': str(arquivo),
            'nome': arquivo.name,
            'tipo': tipo,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'destino': str(BASE / categoria / subcategoria / arquivo.name),
            'tamanho': arquivo.stat().st_size
        }

    def _ler_conteudo(self, arquivo, tipo):
        """Le o conteudo de um arquivo para analise"""
        try:
            if tipo in ['texto', 'codigo', 'dados']:
                with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read(5000)
            elif tipo == 'documento' and arquivo.suffix.lower() == '.pdf':
                try:
                    import PyPDF2
                    with open(arquivo, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        if len(reader.pages) > 0:
                            return reader.pages[0].extract_text()[:5000]
                except:
                    pass
        except:
            pass
        return ""

    def _aplicar_regras(self, arquivo, nome, extensao, tipo, texto):
        """Aplica regras de classificacao"""

        # ===== REGRAS POR TIPO DE ARQUIVO =====

        # Certificados e chaves -> Seguranca
        if tipo in ['certificado', 'chave']:
            return "14_SEGURANCA", "Certificados_Digitais"

        # Screenshots -> Midia
        if tipo == 'imagem' and any(kw in nome for kw in ['screenshot', 'captura', 'print', 'screen']):
            return "11_MIDIA", "Screenshots"

        # ===== REGRAS POR PALAVRAS-CHAVE =====

        # Documentos Pessoais
        for sub, keywords in PALAVRAS_CHAVE['documentos_pessoais'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'cpf':
                    return "02_DOCUMENTOS_PESSOAIS", "CPF"
                elif sub == 'rg':
                    return "02_DOCUMENTOS_PESSOAIS", "RG"
                elif sub == 'cnh':
                    return "02_DOCUMENTOS_PESSOAIS", "CNH"
                elif sub == 'certidao':
                    return "02_DOCUMENTOS_PESSOAIS", "Certidoes"
                elif sub == 'comprovante':
                    return "02_DOCUMENTOS_PESSOAIS", "Comprovantes"

        # Financeiro
        for sub, keywords in PALAVRAS_CHAVE['financeiro'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'banco':
                    return "03_FINANCEIRO", "Bancos"
                elif sub == 'imposto':
                    return "03_FINANCEIRO", "Impostos"
                elif sub == 'investimento':
                    return "03_FINANCEIRO", "Investimentos"
                elif sub == 'boleto':
                    return "03_FINANCEIRO", "Boletos"
                elif sub == 'cartao':
                    return "03_FINANCEIRO", "Extratos"

        # Juridico
        for sub, keywords in PALAVRAS_CHAVE['juridico'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'contrato':
                    return "04_JURIDICO", "Contratos"
                elif sub == 'processo':
                    return "04_JURIDICO", "Processos"
                elif sub == 'procuracao':
                    return "04_JURIDICO", "Procuracoes"
                elif sub == 'cnpj':
                    return "04_JURIDICO", "CNPJ"

        # Saude
        for sub, keywords in PALAVRAS_CHAVE['saude'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'exame':
                    return "05_SAUDE", "Exames"
                elif sub == 'receita':
                    return "05_SAUDE", "Receitas"
                elif sub == 'plano':
                    return "05_SAUDE", "Plano_Saude"
                elif sub == 'vacina':
                    return "05_SAUDE", "Vacinas"

        # Imoveis
        for sub, keywords in PALAVRAS_CHAVE['imoveis'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'escritura':
                    return "06_IMOVEIS", "Escrituras"
                elif sub == 'iptu':
                    return "06_IMOVEIS", "IPTU"
                elif sub == 'condominio':
                    return "06_IMOVEIS", "Condominio"
                elif sub == 'aluguel':
                    return "06_IMOVEIS", "Contratos_Aluguel"

        # Veiculos
        for sub, keywords in PALAVRAS_CHAVE['veiculos'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'documento':
                    return "07_VEICULOS", "CRLV"
                elif sub == 'ipva':
                    return "07_VEICULOS", "IPVA"
                elif sub == 'multa':
                    return "07_VEICULOS", "Multas"
                elif sub == 'seguro':
                    return "07_VEICULOS", "Seguros"
                elif sub == 'manutencao':
                    return "07_VEICULOS", "Manutencao"

        # Educacao
        for sub, keywords in PALAVRAS_CHAVE['educacao'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'diploma':
                    return "08_EDUCACAO", "Diplomas"
                elif sub == 'certificado':
                    return "08_EDUCACAO", "Certificados"
                elif sub == 'curso':
                    return "08_EDUCACAO", "Cursos"
                elif sub == 'material':
                    return "08_EDUCACAO", "Materiais"

        # Trabalho
        for sub, keywords in PALAVRAS_CHAVE['trabalho'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'curriculo':
                    return "09_TRABALHO", "Curriculos"
                elif sub == 'holerite':
                    return "09_TRABALHO", "Holerites"
                elif sub == 'ctps':
                    return "09_TRABALHO", "CTPS"
                elif sub == 'inss':
                    return "09_TRABALHO", "INSS_FGTS"

        # Compras
        for sub, keywords in PALAVRAS_CHAVE['compras'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'nota_fiscal':
                    return "13_COMPRAS", "Notas_Fiscais"
                elif sub == 'garantia':
                    return "13_COMPRAS", "Garantias"
                elif sub == 'manual':
                    return "13_COMPRAS", "Manuais"

        # Seguranca
        for sub, keywords in PALAVRAS_CHAVE['seguranca'].items():
            if any(kw in texto for kw in keywords):
                if sub == 'certificado_digital':
                    return "14_SEGURANCA", "Certificados_Digitais"
                elif sub == 'chave':
                    return "14_SEGURANCA", "Chaves_SSH"
                elif sub == 'senha':
                    return "14_SEGURANCA", "Senhas_Backup"

        # ===== REGRAS POR TIPO DE ARQUIVO (fallback) =====

        if tipo == 'imagem':
            return "11_MIDIA", "Fotos"
        elif tipo == 'video':
            return "11_MIDIA", "Videos"
        elif tipo == 'audio':
            return "11_MIDIA", "Musicas"
        elif tipo == 'apresentacao':
            return "11_MIDIA", "Apresentacoes"
        elif tipo == 'codigo':
            return "10_PROJETOS", "Desenvolvimento"
        elif tipo in ['documento', 'planilha']:
            # Documento generico vai para INBOX
            return "01_INBOX", "Para_Classificar"
        elif tipo == 'compactado':
            return "15_BACKUP", "Arquivos_Antigos"

        # Default: INBOX para classificacao manual
        return "01_INBOX", "Para_Classificar"

    def organizar_arquivo(self, arquivo, dry_run=False):
        """Organiza um arquivo movendo para o destino correto"""

        info = self.classificar_arquivo(arquivo)

        if not info:
            self.stats['erros'] += 1
            return None

        self.stats['total'] += 1

        # Criar diretorio destino
        destino = Path(info['destino'])

        # Verificar se arquivo ja existe no destino
        if destino.exists():
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            novo_nome = f"{destino.stem}_{timestamp}{destino.suffix}"
            destino = destino.parent / novo_nome
            info['destino'] = str(destino)

        try:
            if not dry_run:
                destino.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(arquivo), str(destino))

            self.stats['classificados'] += 1

            # Estatisticas por categoria
            cat = info['categoria']
            self.stats['por_categoria'][cat] = self.stats['por_categoria'].get(cat, 0) + 1

            self.stats['arquivos'].append(info)

            return info

        except Exception as e:
            self.stats['erros'] += 1
            print(f"   ERRO: {arquivo.name} - {e}")
            return None

    def organizar_pasta(self, pasta, dry_run=False):
        """Organiza todos os arquivos de uma pasta"""

        pasta = Path(pasta)

        if not pasta.exists():
            print(f"Pasta nao encontrada: {pasta}")
            return

        # Listar arquivos
        arquivos = list(pasta.rglob('*'))
        arquivos = [a for a in arquivos if a.is_file() and not a.name.startswith('.')]

        print(f"\n{'='*60}")
        print(f"   TRIAGEM UNIVERSAL - ENSIDE v2.0")
        print(f"{'='*60}")
        print(f"\n   Pasta: {pasta}")
        print(f"   Arquivos: {len(arquivos)}")
        print(f"   Modo: {'SIMULACAO' if dry_run else 'ORGANIZACAO'}")
        print(f"\n{'='*60}\n")

        for arquivo in arquivos:
            info = self.organizar_arquivo(arquivo, dry_run)

            if info:
                status = "[OK]" if not dry_run else "[SIM]"
                print(f"   {status} {info['nome']}")
                print(f"        -> {info['categoria']}/{info['subcategoria']}")

        self._imprimir_resumo()

    def _imprimir_resumo(self):
        """Imprime resumo da organizacao"""

        print(f"\n{'='*60}")
        print(f"   RESUMO")
        print(f"{'='*60}")
        print(f"\n   Total: {self.stats['total']}")
        print(f"   Classificados: {self.stats['classificados']}")
        print(f"   Erros: {self.stats['erros']}")

        if self.stats['por_categoria']:
            print(f"\n   Por Categoria:")
            for cat, count in sorted(self.stats['por_categoria'].items()):
                nome = CATEGORIAS.get(cat, {}).get('nome', cat)
                print(f"      {cat}: {count} ({nome})")

        print(f"\n{'='*60}\n")


def criar_estrutura():
    """Cria a estrutura completa de pastas"""

    print("\n   Criando estrutura de pastas...")

    for cat_id, cat_info in CATEGORIAS.items():
        # Criar pasta categoria
        cat_path = BASE / cat_id
        cat_path.mkdir(parents=True, exist_ok=True)

        # Criar subcategorias
        for sub in cat_info['subcategorias']:
            sub_path = cat_path / sub
            sub_path.mkdir(parents=True, exist_ok=True)

    print(f"   Estrutura criada em: {BASE}")
    print(f"   Total: {len(CATEGORIAS)} categorias\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='TRIAGEM UNIVERSAL - Sistema de Organizacao ENSIDE',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s ~/Downloads              # Organiza pasta Downloads
  %(prog)s ~/Downloads --dry-run    # Simula sem mover
  %(prog)s --criar-estrutura        # Cria estrutura de pastas
        """
    )

    parser.add_argument('pasta', nargs='?', help='Pasta para organizar')
    parser.add_argument('--dry-run', action='store_true', help='Simular sem mover arquivos')
    parser.add_argument('--criar-estrutura', action='store_true', help='Criar estrutura de pastas')

    args = parser.parse_args()

    if args.criar_estrutura:
        criar_estrutura()
        return

    if not args.pasta:
        parser.print_help()
        return

    triagem = TriagemUniversal()
    triagem.organizar_pasta(args.pasta, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
