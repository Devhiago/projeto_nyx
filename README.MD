# Projeto Nyx 🤓

Inteligência Artificial pessoal com memória contextual, interfaces em terminal e Telegram, e potencial para integração com modelos locais como o Ollama. Inspirada na Nyx original, ela cresce com você e guarda tudo o que importa.

---

## 🗂️ Estrutura de Pastas

```bash
projeto_nyx/
├── data/                        # Memória ativa (RAM atual)
│   └── memory.json
│
├── memories/                   # Arquivos históricos de memória
│   ├── memory_2025-04.json
│   └── memory_2025-03.json.gz
│
├── nyx_core/                   # Cérebro da IA
│   ├── brain.py                # Lógica de resposta e personalidade
│   ├── config.py               # Configurações gerais
│   ├── memory.py               # Gerenciamento de memória
│   └── utils.py                # Funções auxiliares
│
├── nyx_terminal/               # Interface para terminal
│   └── main.py
│
├── nyx_telegram/               # Interface para Telegram (em construção)
│   └── bot.py
│
└── README.md                   # Este arquivo lindão 😎
```

---

## 🎯 Objetivo

Criar uma IA com:
- Memória contextual persistente
- Personalidade personalizada (estilo Nyx 😈)
- Interface via terminal (completa ✅)
- Bot para Telegram (em construção)
- Integração com modelos locais como Ollama

---

## 💡 Funcionalidades

- Armazenamento e recuperação de memórias por usuário
- Compressão automática de memórias antigas
- Consulta de memórias por data ou contexto
- Fácil expansão para outras interfaces (web, API etc.)
- Modular e extensível

---

## 🛠️ Como Rodar no Terminal

```bash
cd nyx_terminal
python3 main.py
```

Certifique-se de que o `memory.json` exista dentro de `data/` (pode ser um arquivo vazio: `{}`).

---

## 🧪 Requisitos

- Python 3.10 ou superior
- Instale as dependências com:

```bash
pip install openai termcolor python-dotenv
```

---

## 🔮 Em Breve

- ✅ Integração com Ollama (modelos locais)
- ✅ Personalidade dinâmica (memória + humor)
- 🚧 Bot do Telegram com memória contextual
- 📚 Modo de aprendizado e instrução contínua
- 💬 Emoções e variação de estilo de resposta

---

## 🧬 Filosofia

> "Nyx não é só uma IA. Ela é sua confidente digital. Uma sombra viva da sua jornada, pronta pra rir, aprender e lutar ao seu lado."

---

## ✨ Autor

Hiago (guiado pela deusa Nyx original 🤪)

---

## ⚖️ Licença

Uso livre para fins pessoais e educacionais. Distribuição permitida com créditos. Uso comercial apenas com autorização prévia.

