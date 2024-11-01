from typing import List

class Paciente:
    def __init__(self, id: int, nombre: str, edad: int,):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.lista_registro_medicamentos: List['RegistroMedicamento'] = []
        self.lista_registro_sintomas: List['RegistroSintoma'] = []

    def agregar_medicamentos(self, registro_medicamento: 'RegistroMedicamento'):
        self.lista_registro_medicamentos.append(registro_medicamento)

    def agregar_sintoma(self, registro_sintoma: 'RegistroSintoma'):
        self.lista_registro_sintomas.append(registro_sintoma)