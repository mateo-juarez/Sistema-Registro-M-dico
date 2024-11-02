import sqlite3
import os

# Ruta a la base de datos
base_dir = os.path.dirname(os.path.dirname(__file__))
CONN_STRING = os.path.join(base_dir, "bd", "bd_sistema_registro_medico.db")

def conectar_bd():
    try:
        # Establecer la conexión
        conn = sqlite3.connect(CONN_STRING)
        print("Conexión a la base de datos establecida.")
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None