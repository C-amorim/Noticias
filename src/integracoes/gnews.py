import requests
from src.persistencia.log import logger

def buscar_noticias(api_key, max_noticias=10):
    url = f"https://gnews.io/api/v4/top-headlines?lang=pt&country=br&max={max_noticias}&token={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            noticias = response.json().get("articles", [])
            logger.info(f"🗞️ {len(noticias)} notícias carregadas da GNews.")
            return noticias
        else:
            logger.error(f"Erro ao buscar notícias: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logger.error(f"Erro de conexão com GNews: {e}")
        return []
