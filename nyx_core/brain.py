# nyx_core/brain.py

def construir_resposta(pergunta, memoria):
    # Exemplo simples de lógica neural baseada em palavras-chave
    if "seu nome" in pergunta.lower():
        return "Meu nome é Nyx Neural, prazer em te conhecer! 🤖"
    elif "quem é você" in pergunta.lower():
        return "Sou uma inteligência artificial em construção, feita para aprender com você."
    elif "livro" in pergunta.lower():
        return "Ainda não sei ler livros, mas logo vou aprender! 📚"
    else:
        return "Ainda estou aprendendo, pode me ensinar mais?"
