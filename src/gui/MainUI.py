import customtkinter as ctk
from src.dao import PacienteDAO
from src.model.entidades import Paciente

ctk.set_appearance_mode("Light")  # Establecemos el modo de apariencia en "Dark"
ctk.set_default_color_theme("green")

# Clase de la aplicación principal
class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro Médico")
        self.geometry("725x550")

        # Crear el frame del menú superior
        self.menu_principal = ctk.CTkFrame(self, height=50, corner_radius=0,
                                           fg_color="#d4d4d4")  # Fondo rojo en el menú superior
        self.menu_principal.pack(side="top", fill="x")

        # Crear los botones del menú superior
        self.btn_pacientes = ctk.CTkButton(self.menu_principal, text="Pacientes", command=self.ver_pantalla_pacientes)
        self.btn_pacientes.grid(row=0, column=0, padx=20, pady=10)

        self.btn_registro_sintomas = ctk.CTkButton(self.menu_principal, text="Registro Sintomas", command=self.ver_pantalla_registro_sintomas)
        self.btn_registro_sintomas.grid(row=0, column=1, padx=20, pady=10)

        self.btn_registro_medicamentos = ctk.CTkButton(self.menu_principal, text="Registro Medicamentos", command=self.ver_pantalla_registro_medicamentos)
        self.btn_registro_medicamentos.grid(row=0, column=2, padx=20, pady=10)

        self.btn_historial_paciente = ctk.CTkButton(self.menu_principal, text="Historial de Pacientes", command=self.ver_pantalla_historial_paciente)
        self.btn_historial_paciente.grid(row=0, column=3, padx=20, pady=10)

        # Crear el frame principal para el contenido
        self.ventana_principal = ctk.CTkFrame(self, corner_radius=10)
        self.ventana_principal.pack(fill="both", expand=True, padx=20, pady=20)


        # Llamar a la función para mostrar el contenido de inicio
        self.ver_pantalla_pacientes()

    def clear_main_frame(self):
        """Limpia el contenido actual de la ventana padre."""
        for widget in self.ventana_principal.winfo_children():
            widget.destroy()

    def ver_pantalla_pacientes(self):
        """Muestra el contenido de la pantalla de pacientes."""
        self.clear_main_frame()
        dao = PacienteDAO()

        # Obtener la lista de pacientes
        lista_pacientes = dao.obtener_pacientes()

        # Crear un label y un campo de entrada para el nombre
        lbNombre = ctk.CTkLabel(self.ventana_principal, text="Ingrese el nombre:", font=("Arial", 16))
        txtNombre = ctk.CTkEntry(self.ventana_principal, width=200)

        # Colocar el label y el entry en la parte superior
        lbNombre.pack(pady=(10, 0))  # Espaciado superior
        txtNombre.pack(pady=(0, 20))  # Espaciado inferior

        # Crear un label y un campo de entrada para la edad
        lbEdad = ctk.CTkLabel(self.ventana_principal, text="Ingrese la edad:", font=("Arial", 16))
        txtEdad = ctk.CTkEntry(self.ventana_principal, width=200)

        # Colocar el label y el entry en la parte superior
        lbEdad.pack(pady=(10, 0))  # Espaciado superior
        txtEdad.pack(pady=(0, 20))  # Espaciado inferior

        # Usar lambda para pasar los entries como argumentos
        btn_guardar_paciente = ctk.CTkButton(self.ventana_principal, text="Guardar Paciente",
                                             command=lambda: self.guardar_paciente(txtNombre, txtEdad))
        btn_guardar_paciente.pack(pady=(10, 0))

        # Crear un Label por cada paciente
        #for i, paciente in enumerate(lista_pacientes, start=1):
            #label_text = f"Paciente N° {i} = nombre: {paciente.nombre}, edad: {paciente.edad}"
            #label = ctk.CTkLabel(self.ventana_principal, text=label_text, font=("Arial", 16))
            #label.pack(pady=5)

    def ver_pantalla_registro_sintomas(self):
        """Muestra la pantalla de pacientes."""
        self.clear_main_frame()
        # Puedes agregar aquí el contenido relacionado con pacientes

    def ver_pantalla_registro_medicamentos(self):
        """Muestra la pantalla de medicamentos."""
        self.clear_main_frame()
        # Puedes agregar aquí el contenido relacionado con medicamentos

    def ver_pantalla_historial_paciente(self):
        """Muestra la pantalla de síntomas."""
        self.clear_main_frame()
        # Puedes agregar aquí el contenido relacionado con síntomas

    def guardar_paciente(self, txtNombre, txtEdad):
        # Obtener los valores de los campos de entrada
        nombre = txtNombre.get()  # Obtener el nombre desde el campo de entrada
        edad = txtEdad.get()  # Obtener la edad desde el campo de entrada

        # Verificar si la edad es un número y convertirla
        try:
            print("nombre: ", nombre)
            print("edad: ", edad)
            edad = int(edad)  # Convertir la edad a un entero
        except ValueError:
            print("La edad debe ser un número.")
            return

        # Crear un nuevo paciente con los datos de los inputs
        nuevo_paciente = Paciente(id=None, nombre=nombre, edad=edad)

        # Crear una instancia del DAO
        dao = PacienteDAO()

        # Llamar al método insertar_paciente de la instancia de dao
        dao.insertar_paciente(nuevo_paciente)

        # (Opcional) Limpiar los campos de entrada después de guardar
        txtNombre.delete(0, 'end')
        txtEdad.delete(0, 'end')




