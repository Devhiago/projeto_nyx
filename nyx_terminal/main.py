# -*- coding: utf-8 -*-

from nyx_core.memory import adicionar_conversa, buscar_contexto
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
