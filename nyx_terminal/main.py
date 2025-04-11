import sys
import os
from datetime import datetime

# Garante que os módulos do projeto possam ser importados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nyx_core.memory import (
    carregar_memoria,
    salvar_memoria,
    verificar_e_comprimir,
    atualizar_memoria_com_mes,
    adicionar_conversa,
    buscar_contexto
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

    # Registra a entrada do usuário
    adicionar_conversa(nome_usuario, user_input)

    # Recupera o contexto e gera resposta
    contexto = buscar_contexto()
    resposta = responder_nyx(contexto)

    # Mostra resposta no terminal
    print(f"🤖 Nyx: {resposta}\n")

    # Registra resposta da Nyx
    adicionar_conversa("Nyx", resposta)

    # Carrega, atualiza e salva memória
    memoria = carregar_memoria()
    memoria["ultima_interacao"] = {
        "pergunta": user_input,
        "resposta": resposta,
        "data": str(datetime.now())
    }
    memoria = atualizar_memoria_com_mes(memoria)
    salvar_memoria(memoria)

    # Verifica se precisa comprimir a memória
    verificar_e_comprimir()
