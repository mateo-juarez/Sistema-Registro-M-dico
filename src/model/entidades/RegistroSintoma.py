from typing import Optional
from src.model.entidades import Paciente, Sintoma

class RegistroSintoma:
    def __init__(self, paciente: Paciente, sintoma: Sintoma, fecha: str,  observaciones: Optional[str] = None):
        self.paciente = paciente
        self.sintoma = sintoma
        self.fecha = fecha
        self.observaciones = observaciones

        # Relación bidireccional
        #paciente.agregar_ingesta(self)