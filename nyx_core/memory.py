import json
import os

MEMORY_PATH = "data/memory.json"

# verifica se existe o arquivo data.json
if not os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "w") as f:
        json.dump({"conversas": []}, f)

def carregar_memoria():
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def salvar_memoria(dados):
    with open(MEMORY_PATH, "w") as f:
        json.dump(dados, f, indent=4)
        
def adicionar_conversa(usuario, mensagem):
    dados = carregar_memoria()
    dados["conversas"].append({"usuario": usuario, "mensagem": mensagem})
    salvar_memoria(dados)
    
def buscar_contexto(quantidade=5):
    dados = carregar_memoria()
    return dados["conversas"][-quantidade:]