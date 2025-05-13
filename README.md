# 📰 Notícias_IA

Projeto em Python que utiliza inteligência artificial para **classificar notícias por tema e urgência**, além de **gerar sugestões de políticas públicas** com base no conteúdo.

---

## 🚀 Visão Geral

O sistema consome notícias em tempo real via API da [GNews](https://gnews.io/), aplica classificações usando modelos de linguagem e gera respostas automatizadas que podem orientar decisões públicas.

---

## 🧠 Tecnologias Utilizadas

- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [Torch (PyTorch)](https://pytorch.org/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [GNews API](https://gnews.io/)

---

## 📁 Estrutura do Projeto

```bash
Noticias_IA/
├── main.py                      # Script principal
├── requirements.txt             # Dependências do projeto
├── .env.sample                  # Modelo para variáveis de ambiente
├── README.md                    # Documentação + Licença
└── src/
    ├── classificadores/         # Classificação e sugestões
    ├── integracoes/             # Consumo da API GNews
    └── persistencia/            # Salvamento de dados e logging
```

---

## ⚙️ Instalação

```bash
# 1. Clone o repositório:
git clone https://github.com/C-amorim/Noticias.git
cd Noticias

# 2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate  # No Windows

# 3. Instale as dependências:
pip install -r requirements.txt

# 4. Configure sua chave da API GNews:
cp .env.sample .env
# depois edite o arquivo .env e insira sua GNEWS_API_KEY
```

---

## ▶️ Como Executar

```bash
python main.py
```

As notícias serão analisadas, classificadas e as sugestões salvas automaticamente em:

```bash
resultados/resultados.csv
```

---

## 🛠️ Funcionalidades

- 🔍 Consome até 10 notícias em tempo real
- 📌 Classifica automaticamente o tema (ex: Saúde, Política, Tecnologia...)
- 🚨 Define a urgência com base no conteúdo
- 🧠 Gera sugestões de políticas públicas concretas
- 🗂️ Salva os resultados com hash e log

---

## 📊 Exemplo de saída (`resultados/resultados.csv`)

| hash       | noticia                       | tema   | urgencia           | sugestao                                |
|------------|-------------------------------|--------|---------------------|------------------------------------------|
| f01...ae44 | "Pesquisadores alertam..."    | Saúde  | extremamente alta  | 1. Intensificar... 2. Ampliar...         |

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir! Sugestões, issues e pull requests são bem-vindos.

---

📌 Direitos Autorais e Uso
Este projeto foi idealizado, desenvolvido e publicado por Caio Amorim em 2025.

Todo o código, estrutura e proposta do sistema Notícias_IA — incluindo o uso de IA para classificação temática e de urgência de notícias em tempo real, com geração automática de sugestões de políticas públicas — são de minha autoria original.

⚖️ Licença
Este projeto está licenciado sob os termos da Licença MIT.

📌 IMPORTANTE:
A utilização deste código, total ou parcial, exige obrigatoriamente a manutenção da autoria e do aviso de licença.

✅ É permitido:

Usar, modificar, redistribuir e integrar com outros projetos (inclusive comerciais)

❌ Não é permitido:

Remover os créditos ou distribuir o projeto como se fosse de outra autoria

Publicar sem menção clara a Caio Amorim como criador original

🧑‍💻 Autor
Caio Amorim
🔗 GitHub: github.com/C-amorim
📬 Contato profissional sob demanda
