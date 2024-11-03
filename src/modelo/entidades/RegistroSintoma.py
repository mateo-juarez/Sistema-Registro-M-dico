from typing import Optional
from src.modelo.entidades import Paciente, Sintoma

class RegistroSintoma:
    def __init__(self, paciente: Paciente, sintoma: Sintoma, fecha: str,  observaciones: Optional[str] = None):
        self.paciente = paciente
        self.sintoma = sintoma
        self.fecha = fecha
        self.observaciones = observaciones

    def __str__(self):
        return f"{self.fecha} - {self.paciente.nombre}: {self.sintoma.nombre} ({self.observaciones})"
