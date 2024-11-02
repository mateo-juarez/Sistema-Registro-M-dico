import customtkinter as ctk
#from tkcalendar import DateEntry
from src.dao import PacienteDAO, RegistroSintomaDAO
from src.modelo.entidades import Paciente

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# Clase de la aplicación principal
class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.PacienteDAO = PacienteDAO()
        self.RegistroSintomaDAO = RegistroSintomaDAO()

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

    def limpiar_ventana_principal(self):
        """Limpia el contenido actual de la ventana principal."""
        for widget in self.ventana_principal.winfo_children():
            widget.destroy()

    def ver_pantalla_pacientes(self):
        self.limpiar_ventana_principal()

        # LABEL Y TXT PARA NOMBRE
        lbNombre = ctk.CTkLabel(self.ventana_principal, text="Ingrese el nombre:", font=("Arial", 16))
        self.txtNombre = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA NOMBRE
        lbNombre.pack(pady=(10, 0))
        self.txtNombre.pack(pady=(0, 20))

        # LABEL Y TXT PARA EDAD
        lbEdad = ctk.CTkLabel(self.ventana_principal, text="Ingrese la edad:", font=("Arial", 16))
        self.txtEdad = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA EDAD
        lbEdad.pack(pady=(10, 0))
        self.txtEdad.pack(pady=(0, 20))

        self.lbMensaje = ctk.CTkLabel(self.ventana_principal, text="", font=("Arial", 16))
        self.lbMensaje.pack(pady=(10, 0))

        btn_guardar_paciente = ctk.CTkButton(self.ventana_principal, text="Guardar Paciente", command=self.guardar_paciente)
        btn_guardar_paciente.pack(pady=(10, 20))

        self.textbox_pacientes = ctk.CTkTextbox(self.ventana_principal, width=500, height=500, font=("Arial", 16, "bold"))
        self.textbox_pacientes.pack(pady=(10, 20))

        self.cargar_textbox_pacientes()


    def ver_pantalla_registro_sintomas(self):
        self.limpiar_ventana_principal()

        lbPaciente = ctk.CTkLabel(self.ventana_principal, text="Seleccione un paciente:", font=("Arial", 16))
        lbPaciente.pack(pady=(10, 0))
        self.cbo_pacientes = ctk.CTkComboBox(self.ventana_principal, values=[paciente.nombre for paciente in self.PacienteDAO.obtener_pacientes()], font=("Arial", 16)) # cbo = COMBOBOX
        self.cbo_pacientes.pack(pady=(0, 20))

        lbSintoma = ctk.CTkLabel(self.ventana_principal, text="Seleccione un síntoma:", font=("Arial", 16))
        lbSintoma.pack(pady=(10, 0))
        self.cbo_sintomas = ctk.CTkComboBox(self.ventana_principal, values=[sintoma.nombre for sintoma in self.RegistroSintomaDAO.obtener_sintomas()], font=("Arial", 16))
        self.cbo_sintomas.pack(pady=(0, 20))

        #lb_fecha = ctk.CTkLabel(self.ventana_principal, text="Ingrese una fecha:", font=("Arial", 16))
        #lb_fecha.pack(pady=(10, 0))
        #self.txt_fecha = DateEntry(self.ventana_principal, width=12, background='darkblue', foreground='white', borderwidth=2)
        #self.txt_fecha.pack(pady=(0, 20))


    def ver_pantalla_registro_medicamentos(self):
        self.limpiar_ventana_principal()

    def ver_pantalla_historial_paciente(self):
        self.limpiar_ventana_principal()

    def cargar_textbox_pacientes(self):
        self.textbox_pacientes.configure(state="normal") # Habilitar edicion del textbox
        lista_pacientes = self.PacienteDAO.obtener_pacientes()

        # Limpiar el contenido del textbox antes de insertar los datos
        self.textbox_pacientes.delete("1.0", "end")
        # Agregar cada paciente de la lista al textbox
        for i, paciente in enumerate(lista_pacientes, start=1):
            texto_paciente = f"Paciente N° {i}   =   Nombre: {paciente.nombre},  Edad: {paciente.edad}\n"
            self.textbox_pacientes.insert("end", texto_paciente)

        self.textbox_pacientes.configure(state="disabled") # Evitar que el usuario edite el textbox

    def guardar_paciente(self):
        # Obtener los valores de los campos de entrada (txt)
        nombre = self.txtNombre.get()
        edad = self.txtEdad.get()

        # Verificar si la edad es un número y convertirla
        try:
            edad = int(edad)
        except ValueError:
            self.lbMensaje.configure(text="La edad debe ser un número válido.", text_color="red") # Mensaje de error
            return

        # Crear un nuevo paciente con los datos de los inputs
        nuevo_paciente = Paciente(id=None, nombre=nombre, edad=edad)

        # Llamar al metodo insertar_paciente de la instancia de PacienteDAO
        self.PacienteDAO.insertar_paciente(nuevo_paciente)
        self.lbMensaje.configure(text="Paciente agregado correctamente.", text_color="green")  # Mensaje de éxito

        # Limpiar los campos de entrada después de guardar
        self.txtNombre.delete(0, 'end')
        self.txtEdad.delete(0, 'end')

        self.cargar_textbox_pacientes()





