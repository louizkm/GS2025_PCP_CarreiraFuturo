from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Carreira:
    """
    Representa uma carreira do futuro com:
    - nome
    - descrição
    - trilha de aprendizado sugerida (lista de passos)
    - competências relevantes (dict: nome_competencia -> peso)
    - foco_futuro (resumo curto do tipo de trabalho/impacto)
    """
    nome: str
    descricao: str
    trilha_aprendizado: List[str]
    competencias_relevantes: Dict[str, float]
    foco_futuro: str
