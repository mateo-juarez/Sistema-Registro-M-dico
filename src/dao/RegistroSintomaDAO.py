import sqlite3
from typing import List
from .ConexionBD import conectar_bd
from src.modelo.entidades import Sintoma, RegistroSintoma


class RegistroSintomaDAO:
    def insertar_registro_sintoma(self, registro_sintoma: RegistroSintoma):
        conn = conectar_bd()
        if conn is None:
            return
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO paciente_sintoma (id_paciente, id_sintoma, fecha, observaciones) VALUES (?, ?, ?, ?)", (registro_sintoma.paciente.id, registro_sintoma.sintoma.id, registro_sintoma.fecha, registro_sintoma.observaciones))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al registrar síntoma: {e}")
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