import logging
import hashlib
import re
from transformers import pipeline

class Classificador:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.theme_clf = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.urgency_clf = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
        self.labels = [
            "Saúde", "Educação", "Segurança", "Economia",
            "Meio Ambiente", "Cultura", "Esporte",
            "Transportes", "Tecnologia", "Política", "Outros"
        ]

    def gerar_hash(self, texto: str) -> str:
        return hashlib.sha256(texto.encode("utf-8")).hexdigest()

    def detectar_tema(self, texto: str) -> str:
        out = self.theme_clf(texto, candidate_labels=self.labels)
        tema = out["labels"][0]
        self.logger.info(f"Tema: {tema}")
        return tema

    def detectar_urgencia(self, texto: str) -> str:
        out = self.urgency_clf(texto)[0]
        estrelas = int(out["label"][0])
        mapping = {1: "extremamente alta", 2: "alta", 3: "média", 4: "baixa", 5: "muito baixa"}
        urg = mapping.get(estrelas, "média")
        self.logger.info(f"Urgência: {urg}")
        return urg

    def gerar_politicas_publicas(self, texto: str, tema: str, urgencia: str) -> str:
        suggestions_map = {
            "Saúde": [
                "Intensificar campanhas de prevenção e educação em saúde pública.",
                "Ampliar a capacidade de atendimento e vigilância sanitária nas áreas críticas."
            ],
            "Educação": [
                "Investir em formação continuada de professores e infraestrutura escolar.",
                "Implementar programas de reforço escolar para alunos em vulnerabilidade."
            ],
            "Segurança": [
                "Reforçar policiamento comunitário nas regiões de maior incidência.",
                "Desenvolver projetos de ressocialização e inclusão social."
            ],
            "Economia": [
                "Oferecer incentivos fiscais para pequenos negócios locais.",
                "Criar linhas de crédito facilitadas para microempreendedores."
            ],
            "Meio Ambiente": [
                "Lançar campanhas de conscientização sobre reciclagem e descarte correto.",
                "Ampliar unidades de conservação e programas de reflorestamento."
            ],
            "Cultura": [
                "Financiar projetos culturais em comunidades periféricas.",
                "Criar editais de incentivo para artistas locais."
            ],
            "Esporte": [
                "Construir e reformar espaços esportivos comunitários.",
                "Implementar programas de esporte educacional em escolas."
            ],
            "Transportes": [
                "Ampliar linhas de transporte público em áreas desatendidas.",
                "Incentivar o uso de modais sustentáveis, como ciclovias."
            ],
            "Tecnologia": [
                "Oferecer cursos gratuitos de capacitação em TI.",
                "Criar incubadoras para startups de base tecnológica."
            ],
            "Política": [
                "Promover fóruns de debate com a sociedade civil.",
                "Aprimorar mecanismos de transparência e participação popular."
            ],
            "Outros": [
                "Monitorar indicadores para avaliação contínua das políticas.",
                "Estabelecer parcerias público-privadas para execução de projetos."
            ]
        }
        base = suggestions_map.get(tema, suggestions_map["Outros"])
        if urgencia in ("extremamente alta", "alta"):
            base[0] = "Priorizar: " + base[0][0].lower() + base[0][1:]
        elif urgencia in ("baixa", "muito baixa"):
            base[1] = "Planejar: " + base[1][0].lower() + base[1][1:]
        return f"1. {base[0]}\n2. {base[1]}"
