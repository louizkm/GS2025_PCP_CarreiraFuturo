from dataclasses import dataclass, field
from typing import Dict, List

from .perfil import Perfil
from .carreira import Carreira


@dataclass
class Recomendador:
    """
    Sistema de recomendação simples baseado em "matching" de competências
    entre um perfil e um conjunto de carreiras do futuro.
    """
    carreiras: List[Carreira] = field(default_factory=list)

    def _score_para_carreira(self, perfil: Perfil, carreira: Carreira) -> Dict:
        """
        Calcula um score de aderência entre 0 e 1 com base nas competências relevantes.
        Também identifica gaps (competências que podem ser fortalecidas).
        """
        soma_pesos = 0.0
        soma_ponderada = 0.0
        gaps = {}

        for comp, peso in carreira.competencias_relevantes.items():
            soma_pesos += peso
            nivel = perfil.obter_nivel_competencia(comp)  # 0 a 10
            # Normaliza para 0-1
            nivel_normalizado = nivel / 10.0
            soma_ponderada += nivel_normalizado * peso

            if nivel < 7:  # abaixo de 7 consideramos que precisa de desenvolvimento
                gaps[comp] = 8.0  # nível alvo aproximado

        if soma_pesos == 0:
            return {"carreira": carreira, "score": 0.0, "competencias_a_desenvolver": gaps}

        score = soma_ponderada / soma_pesos  # 0 a 1
        return {
            "carreira": carreira,
            "score": score,
            "score_normalizado": score * 100,
            "competencias_a_desenvolver": gaps,
        }

    def recomendar(self, perfil: Perfil, limite: int = 5) -> List[Dict]:
        """
        Retorna uma lista de dicionários com as melhores carreiras para o perfil.
        """
        resultados = []
        for carreira in self.carreiras:
            resultado = self._score_para_carreira(perfil, carreira)
            resultados.append(resultado)

        resultados.sort(key=lambda x: x["score"], reverse=True)
        return resultados[:limite]
