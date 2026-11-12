import requests
import os
from dotenv import load_dotenv

url = "https://api.coingecko.com/api/v3/simple/price"

parametros = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "brl,usd",
    "include_24hr_change": "true"
}

resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    relatorio = "Olá, IA! Aqui estão os dados mais recentes do mercado cripto:\n\n"

    for moeda, valor in dados.items():
        nome = moeda.upper()
        preco_brl = valor.get("brl", 0)
        preco_usd = valor.get("usd", 0)
        variacao_24h = valor.get("brl_24h_change", 0)

        relatorio += f"Moeda: {nome}\n"
        relatorio += f" Preço: R$ {preco_brl:.2f} | $ {preco_usd:.2f}\n"
        relatorio += f" Variação 24h: {variacao_24h:.2}%\n"

        if variacao_24h < -3:
            relatorio += f"  ⚠️  ALERTA: {nome} caiu mais de 3% nas últimas 24h! Possível oportunidade de compra.\n"
        elif variacao_24h > 3:
            relatorio += f"  🚀  ALERTA: {nome} subiu mais de 3% nas últimas 24h! Fique atento.\n"
        else:
            relatorio += f"  ⚖️  Mercado estável para {nome}.\n"

        relatorio += "-" * 30
        relatorio += "\n"

    print("--- RELATÓRIO PRONTO PARA A IA ---")
    print(relatorio)

    print("\nEnviando relatório para a Groq analisar...")

url_groq = "https://api.groq.com/openai/v1/chat/completions"

load_dotenv("chave.env")

api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("API_KEY não encontrado!")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

historico_mensagens = [
    {"role": "system", "content": "Você é um analista financeiro experiente, objetivo e interativo."},
    {"role": "user", "content": relatorio}
]

payload = {
    "model": "openai/gpt-oss-20b",
    "messages": historico_mensagens
}

resposta_ia = requests.post(url_groq, json=payload, headers=headers)

if resposta_ia.status_code == 200:
    dados_ia = resposta_ia.json()
    analise_final = dados_ia['choices'][0]['message']['content']

    print("\n--- ANÁLISE DA IA ---")
    print(analise_final)

    historico_mensagens.append({"role": "assistant", "content": analise_final})
else:
    print(f"Erro ao consultar a IA. Status: {resposta_ia.status_code}")
    exit()

print("\n" + "="*40)
print("Chat iniciado! Responda às perguntas da IA ou digite 'sair' para  encerrar.")
print("="*40 + "\n")

while True:
    pergunta_usuario = input("Você: ")

    if pergunta_usuario.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até logo!")
        break
    historico_mensagens.append({"role": "user", "content": pergunta_usuario})

    payload["messages"] = historico_mensagens

    resposta_ia = requests.post(url_groq, json=payload, headers=headers)

    if resposta_ia.status_code == 200:
        dados_ia = resposta_ia.json()
        resposta_assistente = dados_ia['choices'][0]['message']['content']

        print(f"\nIA: {resposta_assistente}\n")

        historico_mensagens.append({"role": "assistant", "content": resposta_assistente})
    else:
        print(f"Erro ao consultar a IA. Status: {resposta_ia.status_code}")
        break