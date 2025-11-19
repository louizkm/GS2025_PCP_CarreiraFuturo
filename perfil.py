from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Perfil:
    """
    Representa um perfil profissional do futuro, com nome, RM e
    um conjunto de competências avaliadas de 0 a 10.
    """
    nome: str
    rm: str = ""
    competencias: Dict[str, float] = field(default_factory=dict)

    def obter_nivel_competencia(self, chave: str) -> float:
        """Retorna o valor da competência, ou 0 se não existir."""
        return float(self.competencias.get(chave, 0.0))
