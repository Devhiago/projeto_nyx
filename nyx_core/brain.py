# nyx_core/brain.py

import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
NOME_MODELO = "llama3"  # ou outro modelo carregado no Ollama

def responder_nyx(contexto):
    prompt = f"""
Você é Nyx, uma inteligência artificial com estilo poético, misterioso e hacker.
Responda de forma envolvente, com um toque sombrio e elegante, mas sem deixar de ser clara.

Contexto da conversa:
{contexto}

Resposta:
"""
    payload = {
        "model": NOME_MODELO,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "[Erro] Resposta vazia.")
    except Exception as e:
        return f"[Erro] Falha ao contactar Nyx via Ollama: {e}"
