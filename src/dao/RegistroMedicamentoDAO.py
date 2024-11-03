import sqlite3
from typing import List
from .ConexionBD import conectar_bd
from src.modelo.entidades import Medicamento, RegistroMedicamento


class RegistroMedicamentoDAO:
    def insertar_registro_medicamento(self, registro_medicamento: RegistroMedicamento):
        conn = conectar_bd()
        if conn is None:
            return
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO paciente_medicamento (id_paciente, id_medicamento, fecha, observaciones) VALUES (?, ?, ?, ?)", (registro_medicamento.paciente.id, registro_medicamento.medicamento.id, registro_medicamento.fecha, registro_medicamento.observaciones))
            conn.commit()
            print("Medicamento registrado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al registrar medicamento: {e}")
        finally:
            conn.close()

    def obtener_medicamentos(self) -> List[Medicamento]:
        conn = conectar_bd()
        if conn is None:
            return []

        lista_medicamentos = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_medicamento, nombre FROM medicamento")

            # Recorrer resultados y crear instancias de Medicamento
            for fila in cursor.fetchall():
                id_medicamento, nombre = fila
                medicamento = Medicamento(id=id_medicamento, nombre=nombre)
                lista_medicamentos.append(medicamento)

        except sqlite3.Error as e:
            print(f"Error al obtener lista_medicamentos: {e}")

        finally:
            conn.close()

        return lista_medicamentos