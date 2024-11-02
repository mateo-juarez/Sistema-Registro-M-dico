import sqlite3
from typing import List
from .ConexionBD import conectar_bd
from src.modelo.entidades import Paciente, Sintoma


class RegistroSintomaDAO:
    def insertar_paciente(self, paciente: Paciente):
        conn = conectar_bd()
        if conn is None:
            return
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO paciente (nombre, edad) VALUES (?, ?)", (paciente.nombre, paciente.edad))
            conn.commit()
            print("Paciente insertado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar paciente: {e}")
        finally:
            conn.close()

    def obtener_sintomas(self) -> List[Sintoma]:
        conn = conectar_bd()
        if conn is None:
            return []

        lista_sintomas = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_sintoma, nombre FROM sintoma")

            # Recorrer resultados y crear instancias de Sintoma
            for fila in cursor.fetchall():
                id_sintoma, nombre = fila
                sintoma = Sintoma(id=id_sintoma, nombre=nombre)
                lista_sintomas.append(sintoma)

        except sqlite3.Error as e:
            print(f"Error al obtener lista_sintomas: {e}")

        finally:
            conn.close()

        return lista_sintomas