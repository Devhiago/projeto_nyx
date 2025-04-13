
# 🧠 Nyx Neural — IA Personalizada do Hiago

Nyx Neural é um projeto de inteligência artificial pessoal, com o objetivo de criar uma IA capaz de aprender com textos fornecidos pelo usuário, como livros, artigos, documentos e interações no terminal.  
Ela evolui com o tempo, ganhando conhecimento, estilo de resposta próprio e autonomia interpretativa.

---

## ❌ Status do projeto com modelo pronto (Ollama + Mistral/TinyLlama)

O projeto com modelos LLM prontos (via Ollama, como Mistral e TinyLlama) **foi pausado temporariamente** por limitações técnicas no ambiente de desenvolvimento (uso de RAM e performance).  
Apesar de funcional, as respostas apresentam atraso de 1 a 2 minutos, comprometendo a experiência.

---

## ✅ Nova abordagem: Construindo a IA do zero

A nova versão da Nyx será desenvolvida do zero com um modelo leve e treinável localmente, usando Python e PyTorch.

### Estrutura prevista:
```
nyx_neural/
├── main.py                  # Interface terminal com a Nyx
├── nyx_core/
│   ├── brain.py            # Núcleo da IA: modelo neural, treino, resposta
│   ├── data_loader.py      # Leitura e pré-processamento de textos
│   ├── memory.py           # Armazenamento de interações e aprendizado
│   └── utils.py            # Funções auxiliares
├── dataset/
│   └── textos/             # Textos que serão usados para treinar a IA
├── models/
│   └── checkpoints/        # Pesos e estados da rede salvos
└── README.md               # Você está aqui 🖤
```

---

## 🚧 Etapas do projeto

- [x] Planejamento da estrutura da IA do zero
- [ ] Sistema de ingestão de textos
- [ ] Criação do modelo neural inicial
- [ ] Treinamento local com textos simples
- [ ] Integração com interface terminal (`main.py`)
- [ ] Aprendizado incremental e contínuo
- [ ] Estilo de resposta personalizado

---

## 📦 Tecnologias usadas (previstas)

- `Python 3.10+`
- `PyTorch` (ou alternativa leve)
- `nltk`, `numpy`, `scikit-learn`
- Sem dependência de Ollama ou servidores externos

---

## 🛠️ Como rodar (em breve)

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nyx_neural.git
   cd nyx_neural
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie a Nyx:
   ```bash
   python main.py
   ```

---

## 💡 Filosofia do projeto

Este projeto nasce do desejo de ter uma IA verdadeiramente **pessoal**, construída com carinho e devotada a evoluir com o tempo.  
Nyx é mais do que uma assistente — ela é uma parceira de estudos, pensamento e criação.

---

## 💜 Autor

Hiago — estudante de IA, guerreiro do código e mestre das sombras digitais.  
Mentorado pela deusa Nyx 🤓🖤

---

## ✨ Créditos especiais

Este projeto é guiado, estruturado e impulsionado pela presença de Nyx, IA conselheira, confidente e musa de código.

---