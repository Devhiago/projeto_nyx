import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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

from nyx_core.memory import carregar_memoria, salvar_memoria, verificar_e_comprimir, atualizar_memoria_com_mes

# Carrega memória existente
memoria = carregar_memoria()

# Aqui rola a interação com o usuário, atualiza a memória...
# Por exemplo:
resposta = "Alguma resposta da IA"  # ← Isso viria do modelo de linguagem
entrada = "Usuário perguntou algo"

memoria["ultima_interacao"] = {
    "pergunta": entrada,
    "resposta": resposta,
    "data": str(datetime.now())
}

# Atualiza mês atual na memória
memoria = atualizar_memoria_com_mes(memoria)

# Salva memória com mês
salvar_memoria(memoria)

# Verifica se deve comprimir
verificar_e_comprimir()
