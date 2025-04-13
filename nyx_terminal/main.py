# nyx_terminal/main.py

from nyx_core.brain import construir_resposta
from nyx_core.memory import carregar_memoria, registrar_conversa

def iniciar_nyx():
    print("Nyx Neural Iniciada! Pergunte algo:")
    memoria = carregar_memoria()

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Até logo! A Nyx Neural continuará aprendendo... 🧠")
            break

        resposta = construir_resposta(pergunta, memoria)
        print(f"Nyx: {resposta}")

        registrar_conversa(pergunta, resposta)

if __name__ == "__main__":
    iniciar_nyx()
