from typing import Optional
from src.modelo.entidades import Paciente, Medicamento

class RegistroMedicamento:
    def __init__(self, paciente: Paciente, medicamento: Medicamento, fecha: str,  observaciones: Optional[str] = None):
        self.paciente = paciente
        self.medicamento = medicamento
        self.fecha = fecha
        self.observaciones = observaciones

        # Relación bidireccional
        #paciente.agregar_ingesta(self)