def responder_nyx(contexto):
    if not contexto:
        return "Ainda não tenho contexto suficiente, me diga algo!"

    # Procura a última mensagem do usuário no contexto
    for item in reversed(contexto):
        if item["autor"].lower() != "nyx":
            return f"Recebi sua mensagem: '{item['mensagem']}' — em breve responderei com sabedoria cósmica."

    return "Não achei nenhuma mensagem sua recente, pode repetir?"
