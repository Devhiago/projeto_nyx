# nyx_core/memory.py

import json
import os
from datetime import datetime

CAMINHO_MEMORIA = os.path.join("data", "memory.json")

# Garante que o arquivo existe
if not os.path.exists(CAMINHO_MEMORIA):
    with open(CAMINHO_MEMORIA, "w") as f:
        json.dump([], f)

def carregar_memoria():
    if os.path.getsize(CAMINHO_MEMORIA) == 0:
        return []
    with open(CAMINHO_MEMORIA, "r") as f:
        return json.load(f)

def salvar_memoria(memoria):
    with open(CAMINHO_MEMORIA, "w") as f:
        json.dump(memoria, f, indent=2)

def adicionar_conversa(autor, mensagem):
    memoria = carregar_memoria()
    nova_entrada = {
        "autor": autor,
        "mensagem": mensagem,
        "timestamp": datetime.now().isoformat()
    }
    memoria.append(nova_entrada)
    salvar_memoria(memoria)

def buscar_contexto(limite=10):
    memoria = carregar_memoria()
    return memoria[-limite:] if len(memoria) > limite else memoria
