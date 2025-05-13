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

## 📄 Licença (MIT)

```
MIT License

Copyright (c) 2025 Caio Amorim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included  
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

---

## ✉️ Contato

**Caio Amorim**  
🔗 [https://github.com/C-amorim](https://github.com/C-amorim)

> Feito com ❤️ por Caio e IA 🚀
