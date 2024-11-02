import sqlite3
from typing import List
from .ConexionBD import conectar_bd
from src.modelo.entidades import Paciente

class PacienteDAO:
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

    def obtener_pacientes(self) -> List[Paciente]:
        conn = conectar_bd()
        if conn is None:
            return []

        lista_pacientes = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_paciente, nombre, edad FROM paciente")

            # Recorrer resultados y crear instancias de Paciente
            for fila in cursor.fetchall():
                id_paciente, nombre, edad = fila
                paciente = Paciente(id=id_paciente, nombre=nombre, edad=edad)
                lista_pacientes.append(paciente)

        except sqlite3.Error as e:
            print(f"Error al obtener lista_pacientes: {e}")

        finally:
            conn.close()

        return lista_pacientes

    """
    def obtener_paciente_por_id(self, id_paciente: int) -> Paciente:
        conn = conectar_bd()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_paciente, nombre, edad FROM paciente WHERE id_paciente = ?", (id_paciente,))
            fila = cursor.fetchone()

            if fila:
                id_paciente, nombre, edad = fila
                return Paciente(id=id_paciente, nombre=nombre, edad=edad)
            else:
                print(f"No se encontró un paciente con ID: {id_paciente}")
                return None

        except sqlite3.Error as e:
            print(f"Error al obtener paciente por ID: {e}")
            return None

        finally:
            conn.close()
        """


