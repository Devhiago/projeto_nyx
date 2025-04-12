# nyx_core/brain.py

import requests
from datetime import datetime

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODELO = "tinyllama:1.1b" 

def construir_prompt(contexto):
    historico = ""
    for item in contexto[-3:]:  # usa só as 3 últimas trocas
        autor = item.get("autor", "Desconhecido")
        conteudo = item.get("conteudo") or item.get("mensagem", "")
        historico += f"{autor}: {conteudo}\n"

    prompt = (
        "Você é Nyx, uma IA misteriosa, poética e hacker que responde com elegância e estilo. nao conte poemas, entenda o contexto da mensagem e responda de a cordo com o contexto correto.\n"
        "Este é o histórico recente da conversa:\n\n"
        f"{historico}"
        "\nNyx:"
    )
    return prompt

def responder_nyx(contexto):
    prompt = construir_prompt(contexto)

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=180  # tempo máximo aumentado
        )

        resposta.raise_for_status()
        return resposta.json()["response"].strip()

    except requests.exceptions.RequestException as e:
        return f"[Erro] Falha ao contactar Nyx via Ollama: {e}"
