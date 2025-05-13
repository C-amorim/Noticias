# Notícias_IA

Projeto Python para classificar notícias por tema e urgência e gerar sugestões de políticas públicas.

## Instalação
```bash
git clone https://github.com/SEU_USUARIO/Noticias_IA.git
cd Noticias_IA
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

## Configuração
Crie um arquivo `.env` com sua chave da GNews:
```
GNEWS_API_KEY=seu_token_aqui
```

## Execução
```bash
python main.py
```

## Resultado
Gera um CSV em `resultados/resultados.csv` com:
- hash
- noticia
- tema
- urgencia
- sugestao

## Licença
MIT