import customtkinter as ctk
from src.dao import PacienteDAO
from src.model.entidades import Paciente

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# Clase de la aplicación principal
class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro Médico")
        self.geometry("725x550")

        # MENUUUU PRINCIPAAAAAL
        self.menu_principal = ctk.CTkFrame(self, height=50, corner_radius=0, fg_color="#d4d4d4")
        self.menu_principal.pack(side="top", fill="x")

        # BOTONESSS DEL MENUUUU
        self.btn_pacientes = ctk.CTkButton(self.menu_principal, text="Pacientes", command=self.ver_pantalla_pacientes)
        self.btn_pacientes.grid(row=0, column=0, padx=20, pady=10)

        self.btn_registro_sintomas = ctk.CTkButton(self.menu_principal, text="Registro Sintomas", command=self.ver_pantalla_registro_sintomas)
        self.btn_registro_sintomas.grid(row=0, column=1, padx=20, pady=10)

        self.btn_registro_medicamentos = ctk.CTkButton(self.menu_principal, text="Registro Medicamentos", command=self.ver_pantalla_registro_medicamentos)
        self.btn_registro_medicamentos.grid(row=0, column=2, padx=20, pady=10)

        self.btn_historial_paciente = ctk.CTkButton(self.menu_principal, text="Historial de Pacientes", command=self.ver_pantalla_historial_paciente)
        self.btn_historial_paciente.grid(row=0, column=3, padx=20, pady=10)

        # VENTANAAA PRINCIPAAAL
        self.ventana_principal = ctk.CTkFrame(self, corner_radius=10)
        self.ventana_principal.pack(fill="both", expand=True, padx=20, pady=20)

        # PANTALLA INICIALLL
        self.ver_pantalla_pacientes()

    def clear_main_frame(self):
        """Limpia el contenido actual de la ventana principal."""
        for widget in self.ventana_principal.winfo_children():
            widget.destroy()

    def ver_pantalla_pacientes(self):
        self.clear_main_frame()
        dao = PacienteDAO()
        lista_pacientes = dao.obtener_pacientes()

        # LABEL Y TXT PARA NOMBRE
        lbNombre = ctk.CTkLabel(self.ventana_principal, text="Ingrese el nombre:", font=("Arial", 16))
        txtNombre = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA NOMBRE
        lbNombre.pack(pady=(10, 0))
        txtNombre.pack(pady=(0, 20))

        # LABEL Y TXT PARA EDAD
        lbEdad = ctk.CTkLabel(self.ventana_principal, text="Ingrese la edad:", font=("Arial", 16))
        txtEdad = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA EDAD
        lbEdad.pack(pady=(10, 0))
        txtEdad.pack(pady=(0, 20))

        lbMensaje = ctk.CTkLabel(self.ventana_principal, text="", font=("Arial", 16))
        lbMensaje.pack(pady=(10, 0))

        btn_guardar_paciente = ctk.CTkButton(self.ventana_principal, text="Guardar Paciente", command=lambda: self.guardar_paciente(txtNombre, txtEdad, lbMensaje)) ## Uso de lambda para pasar los entries (txt) como argumentos
        btn_guardar_paciente.pack(pady=(10, 0))



        # Crear un Label por cada paciente
        #for i, paciente in enumerate(lista_pacientes, start=1):
            #label_text = f"Paciente N° {i} = nombre: {paciente.nombre}, edad: {paciente.edad}"
            #label = ctk.CTkLabel(self.ventana_principal, text=label_text, font=("Arial", 16))
            #label.pack(pady=5)

    def ver_pantalla_registro_sintomas(self):
        self.clear_main_frame()

    def ver_pantalla_registro_medicamentos(self):
        self.clear_main_frame()

    def ver_pantalla_historial_paciente(self):
        self.clear_main_frame()

    def guardar_paciente(self, txtNombre, txtEdad, lbMensaje):
        # Obtener los valores de los campos de entrada (txt)
        nombre = txtNombre.get()
        edad = txtEdad.get()

        # Verificar si la edad es un número y convertirla
        try:
            edad = int(edad)
        except ValueError:
            lbMensaje.configure(text="La edad debe ser un número válido.", text_color="red") # Mensaje de error
            return

        # Crear un nuevo paciente con los datos de los inputs
        nuevo_paciente = Paciente(id=None, nombre=nombre, edad=edad)

        # Crear una instancia del DAO
        dao = PacienteDAO()

        # Llamar al metodo insertar_paciente de la instancia de dao
        dao.insertar_paciente(nuevo_paciente)
        lbMensaje.configure(text="Paciente agregado correctamente.", text_color="green")  # Mensaje de éxito

        # Limpiar los campos de entrada después de guardar
        txtNombre.delete(0, 'end')
        txtEdad.delete(0, 'end')




