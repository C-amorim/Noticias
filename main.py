import os
import csv
from dotenv import load_dotenv
from src.persistencia.log import logger
from src.integracoes.gnews import buscar_noticias
from src.classificadores.classificador import Classificador
from src.persistencia.arquivos import salvar_resultados

load_dotenv()
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

def main():
    if not GNEWS_API_KEY:
        logger.error("Chave GNEWS_API_KEY não encontrada no .env.")
        return

    noticias = buscar_noticias(GNEWS_API_KEY)
    if not noticias:
        logger.warning("Nenhuma notícia retornada.")
        return

    clf = Classificador()
    resultados = []

    for noticia in noticias:
        titulo = noticia.get("title", "")
        descricao = noticia.get("description", "")
        conteudo = f"{titulo} {descricao}".strip()
        if not conteudo:
            continue

        tema = clf.detectar_tema(conteudo)
        urgencia = clf.detectar_urgencia(conteudo)
        sugestao = clf.gerar_politicas_publicas(conteudo, tema, urgencia)
        hash_ = clf.gerar_hash(conteudo)

        resultados.append({
            "hash": hash_,
            "noticia": conteudo,
            "tema": tema,
            "urgencia": urgencia,
            "sugestao": sugestao
        })

    salvar_resultados(resultados)

if __name__ == "__main__":
    main()
