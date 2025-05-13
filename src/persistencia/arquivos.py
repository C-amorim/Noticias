import os
import csv
from src.persistencia.log import logger

def salvar_resultados(resultados, caminho="resultados/resultados.csv"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    escrever_cabecalho = not os.path.exists(caminho)
    with open(caminho, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["hash", "noticia", "tema", "urgencia", "sugestao"])
        if escrever_cabecalho:
            writer.writeheader()
        for item in resultados:
            writer.writerow(item)
    logger.info(f"✅ {len(resultados)} resultados salvos em '{caminho}'.")
