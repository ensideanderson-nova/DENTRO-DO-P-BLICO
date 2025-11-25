#!/usr/bin/env python3
"""
TRIAGEM MEGA - Sistema de Organizacao de Arquivos ENSIDE
45 Categorias | 45 Cores | 225+ Etiquetas

Versao: 4.0 MEGA
Autor: Anderson Enside - Grupo Lider Madeiras
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

# ===============================================================================
# CONFIGURACAO
# ===============================================================================

ENSIDE_MASTER = os.path.expanduser("~/Enside_Master_MEGA")

# ===============================================================================
# 45 CATEGORIAS COMPLETAS
# ===============================================================================

CATEGORIAS_COMPLETAS = {
    # DOCUMENTOS (5)
    '01_INBOX': {
        'nome': 'INBOX',
        'icone': '📥',
        'cor': 'inbox',
        'tipo': 'documentos',
        'descricao': 'Entrada de documentos novos',
        'tags': ['entrada', 'novo', 'processamento', 'triagem', 'pendente'],
        'palavras_chave': ['novo', 'inbox', 'entrada', 'recem', 'download'],
    },
    '02_DOCUMENTOS_PESSOAIS': {
        'nome': 'DOCUMENTOS_PESSOAIS',
        'icone': '👤',
        'cor': 'pessoais',
        'tipo': 'documentos',
        'descricao': 'RH, folha de pagamento, beneficios',
        'tags': ['rh', 'pessoal', 'funcionario', 'folha_pagamento', 'beneficio', 'contrato_trabalho'],
        'palavras_chave': ['rh', 'folha', 'pagamento', 'beneficio', 'cpf', 'rg', 'cnh'],
    },
    '03_DOCUMENTOS_EMPRESA': {
        'nome': 'DOCUMENTOS_EMPRESA',
        'icone': '🏢',
        'cor': 'empresa',
        'tipo': 'documentos',
        'descricao': 'Contratos, notas fiscais, documentacao legal',
        'tags': ['legal', 'contrato', 'nfe', 'regulamento', 'documentacao', 'compliance'],
        'palavras_chave': ['contrato', 'nfe', 'regulamento', 'cnpj', 'empresa', 'juridico'],
    },
    '04_CV_LATTES': {
        'nome': 'CV_LATTES',
        'icone': '🎓',
        'cor': 'cvlattes',
        'tipo': 'documentos',
        'descricao': 'Curriculos, Lattes, formacao academica',
        'tags': ['cv', 'curriculo', 'lattes', 'educacao', 'certificacao', 'formacao'],
        'palavras_chave': ['curriculo', 'cv', 'lattes', 'diploma', 'certificado'],
    },
    '05_VIAGENS_HOSPEDAGEM': {
        'nome': 'VIAGENS_HOSPEDAGEM',
        'icone': '✈️',
        'cor': 'viagens',
        'tipo': 'documentos',
        'descricao': 'Passagens, hoteis, itinerarios',
        'tags': ['viagem', 'hotel', 'hospedagem', 'passagem_aerea', 'turismo', 'milhas'],
        'palavras_chave': ['viagem', 'hotel', 'passagem', 'voo', 'reserva', 'hospedagem'],
    },

    # PRODUTOS MADEIRA (6)
    '06_PRODUTOS_MADEIRA_PINUS': {
        'nome': 'PRODUTOS_MADEIRA_PINUS',
        'icone': '🌲',
        'cor': 'pinus',
        'tipo': 'negocio',
        'descricao': 'Pinus: precos, especificacoes, catalogo',
        'tags': ['pinus', 'madeira_mole', 'produto', 'tabela_preco', 'especificacao', 'catalogo'],
        'palavras_chave': ['pinus', 'madeira', 'tabua', 'viga', 'caibro'],
    },
    '07_PRODUTOS_MADEIRA_EUCALIPTO': {
        'nome': 'PRODUTOS_MADEIRA_EUCALIPTO',
        'icone': '🌳',
        'cor': 'eucalipto',
        'tipo': 'negocio',
        'descricao': 'Eucalipto: precos, especificacoes',
        'tags': ['eucalipto', 'madeira_dura', 'produto', 'tabela_preco', 'especificacao'],
        'palavras_chave': ['eucalipto', 'eucaliptus', 'tratado'],
    },
    '08_PRODUTOS_MADEIRA_ESPECIAL': {
        'nome': 'PRODUTOS_MADEIRA_ESPECIAL',
        'icone': '💎',
        'cor': 'especial',
        'tipo': 'negocio',
        'descricao': 'Madeiras especiais, premium, exoticas',
        'tags': ['madeira_especial', 'premium', 'exotica', 'rarissima', 'luxo', 'selecionada'],
        'palavras_chave': ['premium', 'especial', 'exotica', 'ipe', 'cedro', 'mogno'],
    },
    '09_TABELAS_PRECOS': {
        'nome': 'TABELAS_PRECOS',
        'icone': '💹',
        'cor': 'precos',
        'tipo': 'negocio',
        'descricao': 'Planilhas de precos, tabelas comparativas',
        'tags': ['preco', 'tabela', 'planilha', 'valor', 'custo', 'comparacao'],
        'palavras_chave': ['preco', 'tabela', 'cotacao', 'valor', 'custo'],
    },
    '10_PESO_UMIDADE': {
        'nome': 'PESO_UMIDADE',
        'icone': '⚖️',
        'cor': 'peso',
        'tipo': 'negocio',
        'descricao': 'Calculos de peso, umidade (seco/verde/murcha)',
        'tags': ['peso', 'umidade', 'densidade', 'calculo', 'verde', 'seco', 'murcha'],
        'palavras_chave': ['peso', 'umidade', 'densidade', 'm3', 'cubagem'],
    },
    '11_CATALOGOS_FORNECEDORES': {
        'nome': 'CATALOGOS_FORNECEDORES',
        'icone': '📑',
        'cor': 'catalogos',
        'tipo': 'negocio',
        'descricao': 'Catalogos, brochuras de fornecedores',
        'tags': ['catalogo', 'brochura', 'fornecedor', 'produto', 'prospeccao', 'marketing'],
        'palavras_chave': ['catalogo', 'brochura', 'prospecto'],
    },

    # LOGISTICA (5)
    '12_LOGISTICA_FRETES': {
        'nome': 'LOGISTICA_FRETES',
        'icone': '🚚',
        'cor': 'fretes',
        'tipo': 'negocio',
        'descricao': 'Fretes, transportadoras, cotacoes de entrega',
        'tags': ['frete', 'transporte', 'entrega', 'logistica', 'cotacao', 'transportadora'],
        'palavras_chave': ['frete', 'transporte', 'entrega', 'cte', 'motorista'],
    },
    '13_RASTREAMENTO': {
        'nome': 'RASTREAMENTO',
        'icone': '🗺️',
        'cor': 'rastreamento',
        'tipo': 'negocio',
        'descricao': 'Rastreamento de pedidos, tracking, localizacao',
        'tags': ['rastreamento', 'tracking', 'localizacao', 'gps', 'envio', 'monitoramento'],
        'palavras_chave': ['rastreamento', 'tracking', 'gps', 'localizacao'],
    },
    '14_NFES_CTRC': {
        'nome': 'NFES_CTRC',
        'icone': '📋',
        'cor': 'nfes',
        'tipo': 'negocio',
        'descricao': 'Notas Fiscais, CTRCs, documentos de entrega',
        'tags': ['nfe', 'ctrc', 'nota_fiscal', 'documento_transporte', 'xml', 'comprovante'],
        'palavras_chave': ['nfe', 'ctrc', 'danfe', 'xml', 'nota fiscal'],
    },
    '15_RETENCAO_TRIBUTARIA': {
        'nome': 'RETENCAO_TRIBUTARIA',
        'icone': '⚖️',
        'cor': 'tributaria',
        'tipo': 'negocio',
        'descricao': 'Retencao de impostos, guias, ICMS, PIS',
        'tags': ['retencao', 'imposto', 'icms', 'pis', 'cofins', 'tributacao', 'guia'],
        'palavras_chave': ['retencao', 'icms', 'pis', 'cofins', 'imposto'],
    },
    '16_SEGUROS': {
        'nome': 'SEGUROS',
        'icone': '🛡️',
        'cor': 'seguros',
        'tipo': 'negocio',
        'descricao': 'Apolices de seguro, protecao de carga',
        'tags': ['seguro', 'apolice', 'protecao', 'carga', 'cobertura', 'sinistro'],
        'palavras_chave': ['seguro', 'apolice', 'sinistro', 'cobertura'],
    },

    # FINANCEIRO (5)
    '17_FINANCEIRO_RECEITAS': {
        'nome': 'FINANCEIRO_RECEITAS',
        'icone': '💰',
        'cor': 'receitas',
        'tipo': 'negocio',
        'descricao': 'Extratos, recibos, comprovantes de receita',
        'tags': ['receita', 'entrada', 'recebimento', 'comprovante', 'extrato', 'deposito'],
        'palavras_chave': ['receita', 'entrada', 'recebimento', 'deposito'],
    },
    '18_FINANCEIRO_DESPESAS': {
        'nome': 'FINANCEIRO_DESPESAS',
        'icone': '💸',
        'cor': 'despesas',
        'tipo': 'negocio',
        'descricao': 'Boletos, faturas, notas de despesa',
        'tags': ['despesa', 'saida', 'pagamento', 'boleto', 'fatura', 'nota_fiscal'],
        'palavras_chave': ['despesa', 'boleto', 'fatura', 'pagamento', 'conta'],
    },
    '19_FINANCEIRO_CONCILIACAO': {
        'nome': 'FINANCEIRO_CONCILIACAO',
        'icone': '📊',
        'cor': 'conciliacao',
        'tipo': 'negocio',
        'descricao': 'Conciliacao bancaria, relatorios financeiros',
        'tags': ['conciliacao', 'balanco', 'relatorio', 'reconciliacao', 'analise'],
        'palavras_chave': ['conciliacao', 'balanco', 'relatorio', 'reconciliacao'],
    },
    '20_FINANCEIRO_IMPOSTOS': {
        'nome': 'FINANCEIRO_IMPOSTOS',
        'icone': '📈',
        'cor': 'impostos',
        'tipo': 'negocio',
        'descricao': 'Guias de impostos, DARF, DAS, GFIP',
        'tags': ['imposto', 'darf', 'das', 'gfip', 'guia_recolhimento', 'contribuicao'],
        'palavras_chave': ['darf', 'das', 'gfip', 'imposto', 'irpf', 'irpj'],
    },
    '21_RECIBOS_COMPROVANTES': {
        'nome': 'RECIBOS_COMPROVANTES',
        'icone': '✅',
        'cor': 'recibos',
        'tipo': 'negocio',
        'descricao': 'Recibos, comprovantes de pagamento',
        'tags': ['recibo', 'comprovante', 'recebimento', 'quitacao', 'pagamento', 'assinado'],
        'palavras_chave': ['recibo', 'comprovante', 'quitacao', 'pix', 'ted'],
    },

    # BANCOS (3)
    '22_BANCOS_DADOS': {
        'nome': 'BANCOS_DADOS',
        'icone': '🏦',
        'cor': 'bancos',
        'tipo': 'negocio',
        'descricao': 'Dados bancarios, agencias, contas, tokens',
        'tags': ['banco', 'conta', 'agencia', 'dados', 'token', 'acesso', 'credencial'],
        'palavras_chave': ['banco', 'itau', 'bradesco', 'santander', 'nubank', 'caixa'],
    },
    '23_BANCOS_TRANSFERENCIAS': {
        'nome': 'BANCOS_TRANSFERENCIAS',
        'icone': '💳',
        'cor': 'transferencias',
        'tipo': 'negocio',
        'descricao': 'Transferencias, DOC, TED, comprovantes',
        'tags': ['transferencia', 'doc', 'ted', 'pix', 'transacao', 'comprovante'],
        'palavras_chave': ['transferencia', 'doc', 'ted', 'pix'],
    },
    '24_BANCOS_LINHAS_CREDITO': {
        'nome': 'BANCOS_LINHAS_CREDITO',
        'icone': '📝',
        'cor': 'credito',
        'tipo': 'negocio',
        'descricao': 'Emprestimos, financiamentos, linhas de credito',
        'tags': ['credito', 'emprestimo', 'financiamento', 'linha', 'contrato', 'juros'],
        'palavras_chave': ['credito', 'emprestimo', 'financiamento', 'juros'],
    },

    # CLIENTES (5)
    '25_CLIENTES_COTACOES': {
        'nome': 'CLIENTES_COTACOES',
        'icone': '📊',
        'cor': 'cotacoes_cli',
        'tipo': 'negocio',
        'descricao': 'Cotacoes enviadas para clientes',
        'tags': ['cotacao', 'proposta', 'cliente', 'preco', 'oferta', 'orcamento'],
        'palavras_chave': ['cotacao', 'proposta', 'orcamento', 'cliente'],
    },
    '26_CLIENTES_PEDIDOS': {
        'nome': 'CLIENTES_PEDIDOS',
        'icone': '🛒',
        'cor': 'pedidos_cli',
        'tipo': 'negocio',
        'descricao': 'Pedidos de clientes, OCs, confirmacoes',
        'tags': ['pedido', 'oc', 'ordem_compra', 'confirmacao', 'cliente', 'entrega'],
        'palavras_chave': ['pedido', 'ordem', 'oc', 'cliente'],
    },
    '27_CLIENTES_FATURAMENTO': {
        'nome': 'CLIENTES_FATURAMENTO',
        'icone': '💵',
        'cor': 'faturamento',
        'tipo': 'negocio',
        'descricao': 'Faturas emitidas, recibos de venda',
        'tags': ['fatura', 'nfe', 'venda', 'recebimento', 'cliente', 'documento'],
        'palavras_chave': ['fatura', 'venda', 'nfe'],
    },
    '28_CLIENTES_NEGOCIACOES': {
        'nome': 'CLIENTES_NEGOCIACOES',
        'icone': '🤝',
        'cor': 'negociacoes_cli',
        'tipo': 'negocio',
        'descricao': 'Conversas, acordos, negociacoes com clientes',
        'tags': ['negociacao', 'acordo', 'contato', 'comunicacao', 'cliente', 'condicao'],
        'palavras_chave': ['negociacao', 'acordo', 'desconto', 'prazo'],
    },
    '29_CLIENTES_RECLAMACOES': {
        'nome': 'CLIENTES_RECLAMACOES',
        'icone': '⚠️',
        'cor': 'reclamacoes',
        'tipo': 'negocio',
        'descricao': 'Reclamacoes, problemas, resolucoes',
        'tags': ['reclamacao', 'problema', 'qualidade', 'devolucao', 'reembolso', 'resolucao'],
        'palavras_chave': ['reclamacao', 'problema', 'devolucao', 'reembolso'],
    },

    # FORNECEDORES (4)
    '30_FORNECEDORES_CADASTRO': {
        'nome': 'FORNECEDORES_CADASTRO',
        'icone': '📇',
        'cor': 'cadastro_forn',
        'tipo': 'negocio',
        'descricao': 'Dados de fornecedores, CNPJ, contatos',
        'tags': ['fornecedor', 'cadastro', 'cnpj', 'contato', 'dados', 'informacoes'],
        'palavras_chave': ['fornecedor', 'cadastro', 'cnpj', 'supplier'],
    },
    '31_FORNECEDORES_CONTRATOS': {
        'nome': 'FORNECEDORES_CONTRATOS',
        'icone': '📜',
        'cor': 'contratos_forn',
        'tipo': 'negocio',
        'descricao': 'Contratos com fornecedores, prazos, condicoes',
        'tags': ['contrato', 'fornecedor', 'acordo', 'prazo', 'condicao', 'clausula'],
        'palavras_chave': ['contrato', 'fornecedor', 'acordo'],
    },
    '32_FORNECEDORES_COMPRAS': {
        'nome': 'FORNECEDORES_COMPRAS',
        'icone': '🛍️',
        'cor': 'compras_forn',
        'tipo': 'negocio',
        'descricao': 'Pedidos de compra, requisicoes, OCs',
        'tags': ['compra', 'pedido_compra', 'oc', 'requisicao', 'fornecedor', 'entrega'],
        'palavras_chave': ['compra', 'pedido', 'requisicao', 'oc'],
    },
    '33_FORNECEDORES_NEGOCIOS': {
        'nome': 'FORNECEDORES_NEGOCIOS',
        'icone': '💼',
        'cor': 'negocios_forn',
        'tipo': 'negocio',
        'descricao': 'Negociacoes, prazos, descontos com fornecedores',
        'tags': ['negociacao', 'fornecedor', 'desconto', 'prazo', 'condicao', 'acordo'],
        'palavras_chave': ['negociacao', 'desconto', 'prazo'],
    },

    # PROJETOS (3)
    '34_PROJETOS_PLANEJAMENTO': {
        'nome': 'PROJETOS_PLANEJAMENTO',
        'icone': '📋',
        'cor': 'planejamento',
        'tipo': 'tecnico',
        'descricao': 'Roadmap, cronograma, metas, objectives',
        'tags': ['projeto', 'planejamento', 'roadmap', 'cronograma', 'meta', 'objetivo'],
        'palavras_chave': ['roadmap', 'cronograma', 'planejamento', 'meta'],
    },
    '35_PROJETOS_EXECUCAO': {
        'nome': 'PROJETOS_EXECUCAO',
        'icone': '⚙️',
        'cor': 'execucao',
        'tipo': 'tecnico',
        'descricao': 'Tarefas, sprints, evolucao, updates',
        'tags': ['projeto', 'execucao', 'sprint', 'tarefa', 'progresso', 'update'],
        'palavras_chave': ['sprint', 'tarefa', 'task', 'progresso'],
    },
    '36_PROJETOS_DOCUMENTACAO': {
        'nome': 'PROJETOS_DOCUMENTACAO',
        'icone': '📚',
        'cor': 'doc_projetos',
        'tipo': 'tecnico',
        'descricao': 'Documentacao de projetos, specs, analises',
        'tags': ['documentacao', 'spec', 'analise', 'requisito', 'design', 'processo'],
        'palavras_chave': ['spec', 'requisito', 'analise', 'design'],
    },

    # DESENVOLVIMENTO (5)
    '37_CODIGO_PYTHON': {
        'nome': 'CODIGO_PYTHON',
        'icone': '🐍',
        'cor': 'python',
        'tipo': 'tecnico',
        'descricao': 'Scripts Python, programacao, automacao',
        'tags': ['python', 'script', 'programacao', 'codigo', 'automacao', 'biblioteca'],
        'palavras_chave': ['python', 'py', 'script', 'automacao'],
    },
    '38_CODIGO_JAVASCRIPT': {
        'nome': 'CODIGO_JAVASCRIPT',
        'icone': '🟨',
        'cor': 'javascript',
        'tipo': 'tecnico',
        'descricao': 'JavaScript, HTML, CSS, Frontend',
        'tags': ['javascript', 'html', 'css', 'frontend', 'web', 'interface'],
        'palavras_chave': ['javascript', 'js', 'html', 'css', 'web'],
    },
    '39_CODIGO_SQL_DATABASE': {
        'nome': 'CODIGO_SQL_DATABASE',
        'icone': '🗄️',
        'cor': 'sql',
        'tipo': 'tecnico',
        'descricao': 'SQL, queries, banco de dados, schemas',
        'tags': ['sql', 'database', 'query', 'schema', 'dados', 'estrutura'],
        'palavras_chave': ['sql', 'query', 'database', 'banco'],
    },
    '40_APIS_INTEGRACAO': {
        'nome': 'APIS_INTEGRACAO',
        'icone': '🔗',
        'cor': 'apis',
        'tipo': 'tecnico',
        'descricao': 'APIs, webhooks, integracoes, endpoints',
        'tags': ['api', 'webhook', 'integracao', 'endpoint', 'conexao', 'rest'],
        'palavras_chave': ['api', 'webhook', 'integracao', 'endpoint'],
    },
    '41_DOCUMENTACAO_TECNICA': {
        'nome': 'DOCUMENTACAO_TECNICA',
        'icone': '📖',
        'cor': 'doc_tecnica',
        'tipo': 'tecnico',
        'descricao': 'README, docs, manuais tecnicos',
        'tags': ['documentacao', 'readme', 'manual', 'guia', 'tutorial', 'howto'],
        'palavras_chave': ['readme', 'manual', 'guia', 'documentacao'],
    },

    # SISTEMAS (3)
    '42_SISTEMAS_BACKUP': {
        'nome': 'SISTEMAS_BACKUP',
        'icone': '💾',
        'cor': 'backup',
        'tipo': 'tecnico',
        'descricao': 'Backups, snapshots, restauracao',
        'tags': ['backup', 'snapshot', 'restore', 'arquivo_completo', 'copia', 'seguranca'],
        'palavras_chave': ['backup', 'snapshot', 'restore', 'bkp'],
    },
    '43_SISTEMAS_LOGS_CONFIGS': {
        'nome': 'SISTEMAS_LOGS_CONFIGS',
        'icone': '⚙️',
        'cor': 'logs',
        'tipo': 'tecnico',
        'descricao': 'Logs, configuracoes, variaveis de ambiente',
        'tags': ['log', 'config', 'configuracao', 'variavel', 'ambiente', 'sistema'],
        'palavras_chave': ['log', 'config', 'env', '.env'],
    },
    '44_SEGURANCA_SENHAS': {
        'nome': 'SEGURANCA_SENHAS',
        'icone': '🔐',
        'cor': 'senhas',
        'tipo': 'sensivel',
        'descricao': 'Senhas, tokens, chaves de acesso (CONFIDENCIAL)',
        'tags': ['senha', 'token', 'chave', 'credencial', 'acesso', 'seguranca', 'privado'],
        'palavras_chave': ['senha', 'password', 'token', 'chave', 'secret'],
    },

    # ESPECIAL (1)
    '45_ARQUIVOS_ANTIGOS_BACKUP': {
        'nome': 'ARQUIVOS_ANTIGOS_BACKUP',
        'icone': '📦',
        'cor': 'antigos',
        'tipo': 'tecnico',
        'descricao': 'Backups antigos, historico, arquivo morto',
        'tags': ['backup_antigo', 'historico', 'arquivo', 'obsoleto', 'legado', 'antigo'],
        'palavras_chave': ['antigo', 'old', 'legado', 'historico', 'arquivo_morto'],
    },
}

# ===============================================================================
# 45 CORES GRADIENTES
# ===============================================================================

CORES_GRADIENTES = {
    'inbox': {'cor1': '#667eea', 'cor2': '#764ba2', 'nome': 'Roxo Profundo'},
    'pessoais': {'cor1': '#f093fb', 'cor2': '#f5576c', 'nome': 'Pink Coral'},
    'empresa': {'cor1': '#4facfe', 'cor2': '#00f2fe', 'nome': 'Azul Turquesa'},
    'cvlattes': {'cor1': '#43e97b', 'cor2': '#38f9d7', 'nome': 'Verde Menta'},
    'viagens': {'cor1': '#fa709a', 'cor2': '#fee140', 'nome': 'Rosa Amarelo'},
    'pinus': {'cor1': '#30cfd0', 'cor2': '#330867', 'nome': 'Teal Roxo'},
    'eucalipto': {'cor1': '#a8edea', 'cor2': '#fed6e3', 'nome': 'Menta Rosa'},
    'especial': {'cor1': '#ff9a56', 'cor2': '#ff6a88', 'nome': 'Laranja Vermelho'},
    'precos': {'cor1': '#2e2e78', 'cor2': '#662d8c', 'nome': 'Roxo Escuro'},
    'peso': {'cor1': '#bdc3c7', 'cor2': '#2c3e50', 'nome': 'Cinza Carvao'},
    'catalogos': {'cor1': '#11998e', 'cor2': '#38ef7d', 'nome': 'Teal Verde'},
    'fretes': {'cor1': '#ee0979', 'cor2': '#ff6a00', 'nome': 'Vermelho Laranja'},
    'rastreamento': {'cor1': '#f6d365', 'cor2': '#fda085', 'nome': 'Amarelo Salmao'},
    'nfes': {'cor1': '#667eea', 'cor2': '#764ba2', 'nome': 'Roxo NFe'},
    'tributaria': {'cor1': '#eb3349', 'cor2': '#f45c43', 'nome': 'Vermelho Fogo'},
    'seguros': {'cor1': '#1fa2ff', 'cor2': '#12d8fa', 'nome': 'Azul Ciano'},
    'receitas': {'cor1': '#43e97b', 'cor2': '#38f9d7', 'nome': 'Verde Claro'},
    'despesas': {'cor1': '#fa709a', 'cor2': '#fee140', 'nome': 'Rosa Ouro'},
    'conciliacao': {'cor1': '#30cfd0', 'cor2': '#330867', 'nome': 'Teal Roxo Escuro'},
    'impostos': {'cor1': '#a8edea', 'cor2': '#fed6e3', 'nome': 'Menta Suave'},
    'recibos': {'cor1': '#11998e', 'cor2': '#38ef7d', 'nome': 'Teal Verde Claro'},
    'bancos': {'cor1': '#ee0979', 'cor2': '#ff6a00', 'nome': 'Vermelho Laranja Quente'},
    'transferencias': {'cor1': '#f6d365', 'cor2': '#fda085', 'nome': 'Amarelo Salmon'},
    'credito': {'cor1': '#667eea', 'cor2': '#764ba2', 'nome': 'Roxo Credito'},
    'cotacoes_cli': {'cor1': '#f093fb', 'cor2': '#f5576c', 'nome': 'Pink Magenta'},
    'pedidos_cli': {'cor1': '#4facfe', 'cor2': '#00f2fe', 'nome': 'Azul Turquesa Brilho'},
    'faturamento': {'cor1': '#43e97b', 'cor2': '#38f9d7', 'nome': 'Verde Jade'},
    'negociacoes_cli': {'cor1': '#fa709a', 'cor2': '#fee140', 'nome': 'Rosa Dourado'},
    'reclamacoes': {'cor1': '#30cfd0', 'cor2': '#330867', 'nome': 'Teal Roxo Profundo'},
    'cadastro_forn': {'cor1': '#bdc3c7', 'cor2': '#2c3e50', 'nome': 'Cinza Profundo'},
    'contratos_forn': {'cor1': '#11998e', 'cor2': '#38ef7d', 'nome': 'Teal Esmeralda'},
    'compras_forn': {'cor1': '#ee0979', 'cor2': '#ff6a00', 'nome': 'Vermelho Laranja Vivo'},
    'negocios_forn': {'cor1': '#f6d365', 'cor2': '#fda085', 'nome': 'Ouro Coral'},
    'planejamento': {'cor1': '#667eea', 'cor2': '#764ba2', 'nome': 'Roxo Planejamento'},
    'execucao': {'cor1': '#f093fb', 'cor2': '#f5576c', 'nome': 'Magenta Coral'},
    'doc_projetos': {'cor1': '#4facfe', 'cor2': '#00f2fe', 'nome': 'Ciano Brilho'},
    'python': {'cor1': '#43e97b', 'cor2': '#38f9d7', 'nome': 'Verde Menta Brilho'},
    'javascript': {'cor1': '#fa709a', 'cor2': '#fee140', 'nome': 'Rosa Banana'},
    'sql': {'cor1': '#30cfd0', 'cor2': '#330867', 'nome': 'Teal Roxo SQL'},
    'apis': {'cor1': '#bdc3c7', 'cor2': '#2c3e50', 'nome': 'Cinza Charcoal'},
    'doc_tecnica': {'cor1': '#11998e', 'cor2': '#38ef7d', 'nome': 'Teal Floresta'},
    'backup': {'cor1': '#ee0979', 'cor2': '#ff6a00', 'nome': 'Vermelho Laranja Backup'},
    'logs': {'cor1': '#f6d365', 'cor2': '#fda085', 'nome': 'Ouro Coral Brilho'},
    'senhas': {'cor1': '#eb3349', 'cor2': '#f45c43', 'nome': 'Vermelho Fogo Senhas'},
    'antigos': {'cor1': '#95a5a6', 'cor2': '#7f8c8d', 'nome': 'Cinza Escuro'},
}

# ===============================================================================
# ARQUIVOS DE EXEMPLO
# ===============================================================================

ARQUIVOS_EXEMPLO = {
    '01_INBOX': ['documento_novo_1.txt', 'arquivo_entrada.pdf', 'pendente.docx'],
    '02_DOCUMENTOS_PESSOAIS': ['folha_pagamento_dez.xlsx', 'beneficios.pdf', 'contracheque.pdf'],
    '03_DOCUMENTOS_EMPRESA': ['contrato_empresa.pdf', 'regulamento_interno.docx', 'nfe_emitida.xml'],
    '04_CV_LATTES': ['cv_anderson.pdf', 'lattes_curriculum.pdf', 'certificado.pdf'],
    '05_VIAGENS_HOSPEDAGEM': ['passagem_aerea.pdf', 'hotel_booking.pdf', 'itinerario.txt'],
    '06_PRODUTOS_MADEIRA_PINUS': ['pinus_tabela_precos.xlsx', 'pinus_especificacoes.pdf', 'catalogo_pinus.docx'],
    '07_PRODUTOS_MADEIRA_EUCALIPTO': ['eucalipto_precos.xlsx', 'eucalipto_specs.pdf', 'ficha_tecnica.pdf'],
    '08_PRODUTOS_MADEIRA_ESPECIAL': ['madeira_premium.pdf', 'madeira_exotica.xlsx', 'catalogo_luxo.pdf'],
    '09_TABELAS_PRECOS': ['tabela_comparativa_2024.xlsx', 'planilha_cotacao.xlsx', 'precos_atualizados.pdf'],
    '10_PESO_UMIDADE': ['calculo_peso_verde.xlsx', 'densidade_madeiras.pdf', 'umidade_tabela.xlsx'],
    '11_CATALOGOS_FORNECEDORES': ['catalogo_supplier_a.pdf', 'brochura_fornecedor.pdf', 'prospecto.pdf'],
    '12_LOGISTICA_FRETES': ['cotacao_frete.xlsx', 'transportadora_dados.pdf', 'tabela_frete.xlsx'],
    '13_RASTREAMENTO': ['rastreamento_001.txt', 'gps_tracking.pdf', 'localizacao.json'],
    '14_NFES_CTRC': ['nfe_transporte.xml', 'ctrc_documento.pdf', 'danfe_emitido.pdf'],
    '15_RETENCAO_TRIBUTARIA': ['guia_retencao.pdf', 'calculo_icms.xlsx', 'pis_cofins.pdf'],
    '16_SEGUROS': ['apolice_seguro.pdf', 'cobertura_carga.docx', 'sinistro_report.pdf'],
    '17_FINANCEIRO_RECEITAS': ['extrato_banco.pdf', 'comprovante_deposito.pdf', 'recibo_venda.pdf'],
    '18_FINANCEIRO_DESPESAS': ['boleto_pagamento.pdf', 'fatura_energia.pdf', 'conta_agua.pdf'],
    '19_FINANCEIRO_CONCILIACAO': ['relatorio_conciliacao.xlsx', 'balanco_mensal.pdf', 'reconciliacao.xlsx'],
    '20_FINANCEIRO_IMPOSTOS': ['guia_darf.pdf', 'das_contribuicao.pdf', 'irpf_2024.pdf'],
    '21_RECIBOS_COMPROVANTES': ['recibo_assinado.pdf', 'comprovante_pix.pdf', 'quitacao.pdf'],
    '22_BANCOS_DADOS': ['dados_banco.txt', 'agencias_contato.xlsx', 'contas_bancarias.pdf'],
    '23_BANCOS_TRANSFERENCIAS': ['comprovante_ted.pdf', 'comprovante_pix.pdf', 'transferencia.pdf'],
    '24_BANCOS_LINHAS_CREDITO': ['contrato_emprestimo.pdf', 'linha_credito_dados.xlsx', 'simulacao.pdf'],
    '25_CLIENTES_COTACOES': ['cotacao_cliente_abc.pdf', 'proposta_xyz.docx', 'orcamento.xlsx'],
    '26_CLIENTES_PEDIDOS': ['pedido_cliente.pdf', 'oc_confirmacao.xlsx', 'ordem_compra.pdf'],
    '27_CLIENTES_FATURAMENTO': ['fatura_emitida.pdf', 'nfe_venda.xml', 'nota_servico.pdf'],
    '28_CLIENTES_NEGOCIACOES': ['email_negociacao.txt', 'acordo_cliente.pdf', 'proposta_final.docx'],
    '29_CLIENTES_RECLAMACOES': ['reclamacao_qualidade.pdf', 'resolucao_problema.docx', 'devolucao.pdf'],
    '30_FORNECEDORES_CADASTRO': ['cadastro_fornecedor.xlsx', 'dados_cnpj.pdf', 'ficha_cadastral.docx'],
    '31_FORNECEDORES_CONTRATOS': ['contrato_fornecedor.pdf', 'condicoes_pagamento.docx', 'termo_acordo.pdf'],
    '32_FORNECEDORES_COMPRAS': ['pedido_compra.pdf', 'oc_fornecedor.xlsx', 'requisicao.docx'],
    '33_FORNECEDORES_NEGOCIOS': ['negociacao_desconto.txt', 'acordo_preco.pdf', 'condicoes.xlsx'],
    '34_PROJETOS_PLANEJAMENTO': ['roadmap_2025.xlsx', 'cronograma_projeto.pdf', 'metas.docx'],
    '35_PROJETOS_EXECUCAO': ['sprint_tarefas.xlsx', 'progresso_update.docx', 'status_report.pdf'],
    '36_PROJETOS_DOCUMENTACAO': ['especificacao_projeto.pdf', 'requisitos.docx', 'analise.pdf'],
    '37_CODIGO_PYTHON': ['script_triagem.py', 'automacao.py', 'utils.py'],
    '38_CODIGO_JAVASCRIPT': ['dashboard.html', 'app.js', 'styles.css'],
    '39_CODIGO_SQL_DATABASE': ['queries.sql', 'schema.sql', 'migrations.sql'],
    '40_APIS_INTEGRACAO': ['api_documentation.md', 'webhook_config.json', 'endpoints.yaml'],
    '41_DOCUMENTACAO_TECNICA': ['README.md', 'MANUAL.pdf', 'GUIA_USUARIO.docx'],
    '42_SISTEMAS_BACKUP': ['backup_completo.zip', 'snapshot_2024.tar', 'db_backup.sql'],
    '43_SISTEMAS_LOGS_CONFIGS': ['app.log', 'config.env', 'settings.json'],
    '44_SEGURANCA_SENHAS': ['senhas_backup.txt', 'chaves_api.txt', 'tokens.json'],
    '45_ARQUIVOS_ANTIGOS_BACKUP': ['backup_2023.zip', 'arquivo_antigo.pdf', 'legado.tar.gz'],
}

# ===============================================================================
# FUNCOES
# ===============================================================================

def criar_estrutura():
    """Cria 45 pastas com nomes padronizados"""
    print("\n📁 Criando estrutura de 45 pastas...")
    os.makedirs(ENSIDE_MASTER, exist_ok=True)

    for cat_codigo in CATEGORIAS_COMPLETAS.keys():
        pasta = os.path.join(ENSIDE_MASTER, cat_codigo)
        os.makedirs(pasta, exist_ok=True)
        print(f"   ✓ {cat_codigo}")

    print(f"\n   Total: {len(CATEGORIAS_COMPLETAS)} pastas criadas")


def criar_arquivos_exemplo():
    """Cria 3 arquivos de exemplo em cada categoria"""
    print("\n📄 Criando arquivos de exemplo...")
    total = 0

    for cat_codigo, arquivos in ARQUIVOS_EXEMPLO.items():
        pasta = os.path.join(ENSIDE_MASTER, cat_codigo)
        for arquivo in arquivos:
            caminho = os.path.join(pasta, arquivo)
            if not os.path.exists(caminho):
                with open(caminho, 'w') as f:
                    f.write(f"# Arquivo de exemplo: {arquivo}\n")
                    f.write(f"# Categoria: {cat_codigo}\n")
                    f.write(f"# Criado em: {datetime.now().isoformat()}\n")
                total += 1

    print(f"   Total: {total} arquivos criados")


def obter_tamanho(caminho):
    """Formata tamanho de arquivo"""
    try:
        bytes_size = os.path.getsize(caminho)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_size < 1024:
                return f"{bytes_size:.1f} {unit}"
            bytes_size /= 1024
        return f"{bytes_size:.1f} TB"
    except:
        return "0 B"


def gerar_json_completo():
    """Gera JSON com todas as 45 categorias"""
    print("\n📊 Gerando JSON sincronizado...")
    dados = {}

    for cat_codigo, info in CATEGORIAS_COMPLETAS.items():
        pasta = os.path.join(ENSIDE_MASTER, cat_codigo)

        # Obter cores
        cor_info = CORES_GRADIENTES.get(info['cor'], {'cor1': '#667eea', 'cor2': '#764ba2', 'nome': 'Padrao'})

        # Listar arquivos
        arquivos = []
        if os.path.exists(pasta):
            for arquivo in os.listdir(pasta):
                caminho = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho):
                    ext = os.path.splitext(arquivo)[1].upper().replace('.', '')
                    arquivos.append({
                        'nome': arquivo,
                        'tipo': ext if ext else 'FILE',
                        'tamanho': obter_tamanho(caminho)
                    })

        dados[cat_codigo] = {
            'icone': info['icone'],
            'nome': info['nome'],
            'tipo': info['tipo'],
            'descricao': info['descricao'],
            'cor': info['cor'],
            'cor1': cor_info['cor1'],
            'cor2': cor_info['cor2'],
            'nome_gradiente': cor_info['nome'],
            'tags': info['tags'],
            'total_arquivos': len(arquivos),
            'arquivos': arquivos[:10]  # Limitar a 10 arquivos
        }

    # Salvar JSON
    json_path = os.path.join(ENSIDE_MASTER, 'categorias_45.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"   Salvo em: {json_path}")
    return dados


def classificar_arquivo(nome_arquivo):
    """Classifica arquivo baseado em nome e extensao"""
    nome_lower = nome_arquivo.lower()
    extensao = os.path.splitext(nome_arquivo)[1].lower().replace('.', '')

    # Verificar palavras-chave
    for cat_codigo, info in CATEGORIAS_COMPLETAS.items():
        if 'palavras_chave' in info:
            for palavra in info['palavras_chave']:
                if palavra.lower() in nome_lower:
                    return cat_codigo

    # Classificar por extensao
    if extensao in ['py']:
        return '37_CODIGO_PYTHON'
    elif extensao in ['js', 'html', 'css']:
        return '38_CODIGO_JAVASCRIPT'
    elif extensao in ['sql']:
        return '39_CODIGO_SQL_DATABASE'
    elif extensao in ['json', 'yaml', 'yml']:
        return '40_APIS_INTEGRACAO'
    elif extensao in ['md', 'txt', 'rst']:
        return '41_DOCUMENTACAO_TECNICA'
    elif extensao in ['zip', 'tar', 'gz', 'rar']:
        return '42_SISTEMAS_BACKUP'
    elif extensao in ['log', 'env', 'cfg', 'ini']:
        return '43_SISTEMAS_LOGS_CONFIGS'
    elif extensao in ['pdf']:
        return '03_DOCUMENTOS_EMPRESA'
    elif extensao in ['xlsx', 'xls', 'csv']:
        return '09_TABELAS_PRECOS'
    elif extensao in ['jpg', 'png', 'gif', 'heic']:
        return '01_INBOX'

    # Default
    return '01_INBOX'


def organizar_pasta(pasta_origem, dry_run=False):
    """Organiza arquivos de uma pasta para as 45 categorias"""
    print(f"\n🔄 Organizando: {pasta_origem}")

    if not os.path.exists(pasta_origem):
        print("   ERRO: Pasta nao encontrada")
        return

    arquivos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

    for arquivo in arquivos:
        if arquivo.startswith('.'):
            continue

        categoria = classificar_arquivo(arquivo)
        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(ENSIDE_MASTER, categoria, arquivo)

        if dry_run:
            print(f"   [SIM] {arquivo} -> {categoria}")
        else:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            shutil.move(origem, destino)
            print(f"   [OK] {arquivo} -> {categoria}")


def imprimir_resumo():
    """Imprime resumo visual do sistema"""
    print("\n" + "=" * 60)
    print("   ENSIDE MEGA - RESUMO DO SISTEMA")
    print("=" * 60)

    total_arquivos = 0
    total_tags = 0

    for cat_codigo, info in CATEGORIAS_COMPLETAS.items():
        pasta = os.path.join(ENSIDE_MASTER, cat_codigo)
        if os.path.exists(pasta):
            arquivos = len([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])
            total_arquivos += arquivos
        total_tags += len(info.get('tags', []))

    print(f"\n   📊 45 Categorias")
    print(f"   📄 {total_arquivos} Arquivos")
    print(f"   🏷️  {total_tags} Etiquetas")
    print(f"   🎨 45 Cores Gradientes")
    print(f"\n   📁 Local: {ENSIDE_MASTER}")
    print("\n" + "=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='TRIAGEM MEGA - 45 Categorias',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s --criar-estrutura    # Cria 45 pastas + arquivos exemplo
  %(prog)s ~/Downloads          # Organiza pasta
  %(prog)s ~/Downloads --dry-run # Simula organizacao
        """
    )

    parser.add_argument('pasta', nargs='?', help='Pasta para organizar')
    parser.add_argument('--criar-estrutura', action='store_true', help='Criar estrutura completa')
    parser.add_argument('--dry-run', action='store_true', help='Simular sem mover')
    parser.add_argument('--gerar-json', action='store_true', help='Gerar JSON')

    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("   🚀 ENSIDE MEGA ORGANIZACAO v4.0 - 45 CATEGORIAS")
    print("=" * 60)

    if args.criar_estrutura:
        criar_estrutura()
        criar_arquivos_exemplo()
        gerar_json_completo()
        imprimir_resumo()
        print("\n✅ SISTEMA MEGA PRONTO!")
        return

    if args.gerar_json:
        gerar_json_completo()
        return

    if args.pasta:
        organizar_pasta(args.pasta, dry_run=args.dry_run)
        gerar_json_completo()
        imprimir_resumo()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
