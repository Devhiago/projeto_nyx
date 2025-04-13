# nyx_core/memory.py

import json
import os

CAMINHO_MEMORIA = "nyx_data/memoria.json"

def carregar_memoria():
    if not os.path.exists(CAMINHO_MEMORIA):
        return {"conversas": []}
    
    with open(CAMINHO_MEMORIA, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_memoria(memoria):
    os.makedirs(os.path.dirname(CAMINHO_MEMORIA), exist_ok=True)
    with open(CAMINHO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=4, ensure_ascii=False)

def registrar_conversa(pergunta, resposta):
    memoria = carregar_memoria()
    memoria["conversas"].append({
        "pergunta": pergunta,
        "resposta": resposta
    })
    salvar_memoria(memoria)
