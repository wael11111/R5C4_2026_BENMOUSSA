from dataclasses import dataclass


@dataclass
class PartieDTO:
    id: int
    serveur_id: int
    file_id: int
    debut: str
    attente_secondes: int
    duree_minutes: float | None