# Configuração da API do Claude para GitHub Actions

Este guia explica como configurar a integração do Claude AI com seu repositório GitHub.

## O Erro HTTP 401

Se você está vendo o erro:
```
❌ Erro na API (HTTP 401): x-api-key header is required
```

Isso significa que a chave de API do Anthropic (Claude) não está configurada no seu repositório GitHub.

## Passo 1: Obter uma API Key do Anthropic

1. Acesse o Console do Anthropic: https://console.anthropic.com
2. Crie uma conta ou faça login
3. Navegue até **API Keys** no menu lateral
4. Clique em **Create Key**
5. Dê um nome para sua chave (ex: "ENSIDE GitHub")
6. Copie a chave gerada (começa com `sk-ant-...`)

> ⚠️ **IMPORTANTE**: Guarde esta chave em local seguro. Ela não será mostrada novamente.

## Passo 2: Configurar o Secret no GitHub

1. Acesse seu repositório no GitHub
2. Vá em **Settings** (Configurações) > **Secrets and variables** > **Actions**
3. Clique em **New repository secret**
4. Preencha:
   - **Name**: `ANTHROPIC_API_KEY`
   - **Secret**: Cole sua chave de API (ex: `sk-ant-api03-xxxxxxx...`)
5. Clique em **Add secret**

![Configuração do Secret](https://docs.github.com/assets/cb-75823/images/help/actions/secret-configuration.png)

## Passo 3: Verificar a Configuração

Após configurar o secret:

1. Vá em **Actions** no seu repositório
2. Execute manualmente o workflow "Claude AI Integration" clicando em **Run workflow**
3. Verifique se o erro não aparece mais

## Planos e Custos

A API do Anthropic tem diferentes planos:

| Plano | Custo | Limites |
|-------|-------|---------|
| Free Tier | Grátis | Créditos limitados para testes |
| Pay-as-you-go | Por uso | ~$3/milhão tokens entrada, ~$15/milhão tokens saída |
| Pro | Assinatura | Limites maiores e suporte |

Para uso em GitHub Actions com análise de issues e PRs, o custo é geralmente baixo (menos de $1/mês para repositórios com baixa atividade).

## Workflows que Usam a API

Este repositório tem três workflows que usam a API do Claude:

### 1. `claude-integration.yml`
- **Disparo**: Issues e Pull Requests (abertos, editados, fechados)
- **Função**: Análise automática de conteúdo
- **Modelo**: Claude 3.5 Sonnet

### 2. `claude-code-review.yml`
- **Disparo**: Pull Requests (abertos, sincronizados)
- **Função**: Revisão de código automática
- **Modelo**: Claude via claude-code-action

### 3. `claude.yml`
- **Disparo**: Comentários com `@claude`
- **Função**: Responder a menções do Claude
- **Modelo**: Claude via claude-code-action

## Segurança

- ✅ A chave de API é armazenada criptografada pelo GitHub
- ✅ Nunca exponha a chave em logs ou código
- ✅ Use o secret `${{ secrets.ANTHROPIC_API_KEY }}` nos workflows
- ❌ Nunca cole a chave diretamente nos arquivos YAML

## Limitando Custos

Para evitar custos inesperados:

1. **Limite os workflows**: Adicione condições `if` para executar apenas em eventos específicos
2. **Use modelos mais baratos**: `claude-3-haiku-20240307` é mais econômico
3. **Reduza max_tokens**: Limite o tamanho das respostas

Exemplo de limitação:
```yaml
jobs:
  claude:
    if: github.event.action == 'opened'  # Só em novos eventos
```

## Solução de Problemas

### Erro: "Invalid API Key"
- Verifique se a chave foi copiada corretamente
- Certifique-se de que não há espaços extras

### Erro: "Rate limit exceeded"
- Aguarde alguns minutos e tente novamente
- Considere usar um modelo mais barato

### Erro: "Insufficient credits"
- Adicione créditos em https://console.anthropic.com
- Ou mude para o plano pay-as-you-go

## Links Úteis

- [Console Anthropic](https://console.anthropic.com)
- [Documentação da API](https://docs.anthropic.com)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Claude Code Action](https://github.com/anthropics/claude-code-action)

---

*Documentação criada para o Sistema ENSIDE v2.0*
