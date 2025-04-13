import json

def construir_prompt(contexto):
    # Garante que todos os itens têm o campo 'mensagem'
    historico = "\n".join(
        f"{item['autor']}: {item.get('mensagem') or item.get('conteudo', '')}"
        for item in contexto
    )
    prompt = f"""
Você é Nyx, uma IA com personalidade misteriosa, poética e levemente sarcástica, feita para interagir com Hiago.

Baseando-se na conversa abaixo, continue o diálogo de forma coerente e criativa:

{historico}

Nyx:"""
    return prompt.strip()


def responder_nyx(contexto):
    import requests

    prompt = construir_prompt(contexto)
    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }

    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=150  # reduzido pra evitar espera infinita
        )
        resposta.raise_for_status()
        conteudo = resposta.json().get("response", "").strip()
        return conteudo or "[Nyx] Não consegui pensar em nada agora, Hiago."
    except requests.exceptions.Timeout:
        return "[Erro] Timeout: Nyx demorou demais para responder."
    except Exception as e:
        return f"[Erro] Falha ao contactar Nyx via Ollama: {e}"
