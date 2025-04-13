import os
import json
import gzip
from datetime import datetime
from pathlib import Path

CAMINHO_MEMORIA_ATUAL = Path("data/memory.json")
PASTA_MEMORIAS_ANTIGAS = Path("memories")
PASTA_MEMORIAS_ANTIGAS.mkdir(exist_ok=True)

def carregar_memoria():
    if not CAMINHO_MEMORIA_ATUAL.exists():
        return {}
    with open(CAMINHO_MEMORIA_ATUAL, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_memoria(memoria: dict):
    with open(CAMINHO_MEMORIA_ATUAL, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

def comprimir_memoria_antiga():
    if not CAMINHO_MEMORIA_ATUAL.exists():
        return
    hoje = datetime.now()
    nome_arquivo = f"memory_{hoje.year}-{hoje.month:02}.json.gz"
    caminho_arquivo = PASTA_MEMORIAS_ANTIGAS / nome_arquivo

    with open(CAMINHO_MEMORIA_ATUAL, "r", encoding="utf-8") as f_in:
        with gzip.open(caminho_arquivo, "wt", encoding="utf-8") as f_out:
            f_out.write(f_in.read())

    CAMINHO_MEMORIA_ATUAL.unlink()
    print(f"[🗜️] Memória comprimida e salva em: {caminho_arquivo}")

MAX_MB = 1

def tamanho_memoria_mb():
    if CAMINHO_MEMORIA_ATUAL.exists():
        return CAMINHO_MEMORIA_ATUAL.stat().st_size / (1024 * 1024)
    return 0

def mes_ultima_memoria():
    if not CAMINHO_MEMORIA_ATUAL.exists():
        return None
    with open(CAMINHO_MEMORIA_ATUAL, "r", encoding="utf-8") as f:
        try:
            memoria = json.load(f)
            return memoria.get("_mes")
        except json.JSONDecodeError:
            return None

def atualizar_memoria_com_mes(memoria: dict):
    hoje = datetime.now()
    memoria["_mes"] = f"{hoje.year}-{hoje.month:02}"
    return memoria

def verificar_e_comprimir():
    memoria_atual = carregar_memoria()
    mes_atual = f"{datetime.now().year}-{datetime.now().month:02}"
    mes_passado = mes_ultima_memoria()
    tamanho = tamanho_memoria_mb()

    if mes_passado and mes_passado != mes_atual:
        print(f"[🗓️] Mês mudou: {mes_passado} → {mes_atual}")
        comprimir_memoria_antiga()
        salvar_memoria({})
    elif tamanho > MAX_MB:
        print(f"[📦] Memória excedeu {MAX_MB}MB (atual: {tamanho:.2f}MB)")
        comprimir_memoria_antiga()
        salvar_memoria({})

def adicionar_conversa(autor, conteudo):
    from datetime import datetime
    memoria = carregar_memoria()
    if "conversas" not in memoria or not isinstance(memoria["conversas"], list):
        memoria["conversas"] = []

    conversa = {
        "autor": autor,
        "mensagem": conteudo,
        "data": datetime.now().isoformat()
    }
    memoria["conversas"].append(conversa)
    salvar_memoria(memoria)


def buscar_contexto(limite=10):
    memoria = carregar_memoria()
    conversas = memoria.get("conversas", [])
    return conversas[-limite:] if len(conversas) > limite else conversas
