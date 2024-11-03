import sqlite3
from typing import List
from .ConexionBD import conectar_bd
from src.modelo.entidades import Paciente, Sintoma, Medicamento, RegistroSintoma, RegistroMedicamento

class PacienteDAO:
    def insertar_paciente(self, paciente: Paciente):
        conn = conectar_bd()
        if conn is None:
            return
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO paciente (nombre, edad) VALUES (?, ?)", (paciente.nombre, paciente.edad))
            conn.commit()
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

    def cargar_registros_sintomas_a_paciente(self, paciente: Paciente):
        conn = conectar_bd()
        if conn is None:
            return []
        try:
            cursor = conn.cursor()
            query = """
                SELECT ps.fecha, ps.observaciones,
                       s.id_sintoma, s.nombre AS nombre_sintoma
                FROM paciente_sintoma ps
                INNER JOIN sintoma s ON s.id_sintoma = ps.id_sintoma
                WHERE ps.id_paciente = ?
            """
            cursor.execute(query, (paciente.id,))
            registros = cursor.fetchall()

            # Crear instancias de RegistroSintoma y Sintoma
            for registro in registros:
                fecha, observaciones, id_sintoma, nombre_sintoma= registro
                # Crear el objeto Sintoma
                sintoma = Sintoma(id=id_sintoma, nombre=nombre_sintoma)
                # Crear el objeto RegistroSintoma y asignarle el sintoma
                registro_sintoma = RegistroSintoma(
                    paciente=paciente,
                    sintoma=sintoma,
                    fecha=fecha,
                    observaciones=observaciones
                )
                paciente.agregar_sintoma(registro_sintoma)
        except sqlite3.Error as e:
            print(f"Error al cargar los registros de síntomas: {e}")
        finally:
            conn.close()

    def cargar_registros_medicamentos_a_paciente(self, paciente: Paciente):
        conn = conectar_bd()
        if conn is None:
            return []
        try:
            cursor = conn.cursor()
            query = """
                SELECT pm.fecha, pm.observaciones,
                       m.id_medicamento, m.nombre AS nombre_medicamento
                FROM paciente_medicamento pm
                INNER JOIN medicamento m ON m.id_medicamento = pm.id_medicamento
                WHERE pm.id_paciente = ?
            """
            cursor.execute(query, (paciente.id,))
            registros = cursor.fetchall()
            for registro in registros:
                fecha, observaciones, id_medicamento, nombre_medicamento= registro
                medicamento = Medicamento(id=id_medicamento, nombre=nombre_medicamento)
                registro_medicamento = RegistroMedicamento(
                    paciente=paciente,
                    medicamento=medicamento,
                    fecha=fecha,
                    observaciones=observaciones
                )
                paciente.agregar_medicamentos(registro_medicamento)
        except sqlite3.Error as e:
            print(f"Error al cargar los registros de medicamentos: {e}")
        finally:
            conn.close()



