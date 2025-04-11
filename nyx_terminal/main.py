import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nyx_core.memory import (
    adicionar_conversa,
    buscar_contexto,
    carregar_memoria,
    salvar_memoria,
    verificar_e_comprimir,
    atualizar_memoria_com_mes,
)
from nyx_core.brain import responder_nyx

print("🟣 Nyx Terminal - Protocolo Iniciado\nDigite 'sair' para encerrar.\n")

nome_usuario = input("👤 Qual seu nome? ")
print(f"\nOlá {nome_usuario}, estou pronta para te ouvir...\n")

while True:
    user_input = input("💬 Você: ")

    if user_input.lower() == "sair":
        print("👋 Encerrando... até logo!")
        break

    adicionar_conversa(nome_usuario, user_input)
    contexto = buscar_contexto()
    resposta = responder_nyx(contexto)

    print(f"🤖 Nyx: {resposta}\n")
    adicionar_conversa("Nyx", resposta)

    # Atualiza e salva memória
    memoria = carregar_memoria()
    memoria = atualizar_memoria_com_mes(memoria)
    salvar_memoria(memoria)
    verificar_e_comprimir()
