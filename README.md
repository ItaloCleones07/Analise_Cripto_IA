# 📊 Análise de Criptomoedas com IA

Sistema desenvolvido em Python que consulta dados atualizados do mercado de criptomoedas através da API do CoinGecko e utiliza inteligência artificial da Groq para gerar análises sobre o comportamento dos ativos.

O projeto também oferece um chat interativo, permitindo que o usuário faça perguntas adicionais à IA com base nos dados coletados e na análise inicial.

## 🚀 Funcionalidades

- **Consulta de mercado:** Obtém os preços do Bitcoin e Ethereum em reais (BRL) e dólares (USD).
- **Variação percentual:** Consulta a variação dos ativos nas últimas 24 horas.
- **Sistema de alertas:** Identifica movimentos de alta ou queda superiores a 3%.
- **Análise com IA:** Envia os dados coletados para a API da Groq, que gera uma análise textual do mercado.
- **Chat interativo:** Permite continuar a conversa com a IA, mantendo o histórico de mensagens.
- **Gerenciamento de credenciais:** Utiliza variáveis de ambiente para armazenar a chave de acesso à API.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Requests | Consumo de APIs HTTP |
| CoinGecko API | Consulta de dados do mercado cripto |
| Groq API | Processamento de linguagem natural com IA |
| python-dotenv | Gerenciamento de variáveis de ambiente |

## ⚙️ Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior.
- Pip (gerenciador de pacotes do Python).
- Uma chave de API da Groq.

## 📦 Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/Analise-Cripto-IA.git
```

**2. Entre na pasta do projeto**

```bash
cd Analise-Cripto-IA
```

**3. Instale as dependências**

```bash
pip install requests python-dotenv
```

## 🔑 Configuração das variáveis de ambiente

Crie um arquivo chamado `chave.env` na raiz do projeto e adicione sua chave de API da Groq:

```env
API_KEY=sua_chave_api_aqui
```

Para obter uma chave de API, acesse:

- [Groq Console](https://console.groq.com/)

**Importante:** Nunca compartilhe sua chave de API ou envie arquivos com credenciais para repositórios públicos.

Adicione o seguinte conteúdo ao arquivo `.gitignore`:

```gitignore
# Variáveis de ambiente
.env
chave.env

# Cache do Python
__pycache__/
*.py[cod]

# Ambientes virtuais
venv/
.venv/
```

## ▶️ Como executar

Após instalar as dependências e configurar sua chave de API, execute:

```bash
python main.py
```

O sistema realizará as seguintes operações:

1. Consultará os preços do Bitcoin e Ethereum na API do CoinGecko.
2. Identificará as variações percentuais das últimas 24 horas.
3. Gerará alertas conforme os limites definidos no código.
4. Enviará os dados para a Groq analisar.
5. Exibirá a análise gerada pela inteligência artificial.
6. Iniciará um chat interativo para perguntas adicionais.

## 💬 Chat interativo

Após a análise inicial, o usuário poderá conversar com a IA utilizando o terminal.

Exemplo:

```text
Chat iniciado! Responda às perguntas da IA ou digite 'sair' para encerrar.

Você: Qual das duas criptomoedas teve o melhor desempenho?

IA: Para determinar o melhor desempenho, podemos comparar
as variações percentuais das últimas 24 horas...
```

Para encerrar a aplicação, digite:

```text
sair
```

## 🚨 Regras de alertas

O sistema utiliza limites de variação percentual para identificar movimentos relevantes no mercado.

| Condição | Alerta |
|---|---|
| Variação inferior a -3% | Possível oportunidade de atenção |
| Variação superior a +3% | Movimento de alta |
| Entre -3% e +3% | Mercado relativamente estável |

Os alertas são informativos e não representam recomendações de investimento.

## 🔌 APIs utilizadas

**CoinGecko API**

Responsável por fornecer os dados de mercado, incluindo preços e variações percentuais das criptomoedas.

Documentação: https://docs.coingecko.com/

**Groq API**

Responsável por processar os dados coletados e gerar respostas utilizando um modelo de linguagem.

Documentação: https://console.groq.com/docs

## ⚠️ Observações

- É necessária uma conexão com a internet para consultar as APIs.
- A disponibilidade das consultas depende dos limites de utilização de cada serviço.
- A análise gerada pela IA pode conter imprecisões.
- Os dados representam informações de mercado no momento da consulta.
- O projeto possui finalidade educacional e experimental, não constituindo ferramenta de recomendação financeira.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de desenvolvimento em Python, consumo de APIs REST, manipulação de JSON, gerenciamento de variáveis de ambiente e integração com modelos de inteligência artificial.

Também explora a utilização de históricos de mensagens para construir uma experiência de chat contextualizada.

---

**Desenvolvido com Python 🐍 | Integração de APIs e Inteligência Artificial 🤖**
