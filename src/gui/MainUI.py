import customtkinter as ctk
from tkcalendar import DateEntry
from src.dao import PacienteDAO, RegistroSintomaDAO
from src.modelo.entidades import Paciente, RegistroSintoma

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# Clase de la aplicación principal
class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.PacienteDAO = PacienteDAO()
        self.RegistroSintomaDAO = RegistroSintomaDAO()

        self.title("Sistema de Registro Médico")
        self.geometry("730x650")

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
        lb_nombre = ctk.CTkLabel(self.ventana_principal, text="Ingrese el nombre:", font=("Arial", 16))
        self.txt_nombre = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA NOMBRE
        lb_nombre.pack(pady=(10, 0))
        self.txt_nombre.pack(pady=(0, 20))

        # LABEL Y TXT PARA EDAD
        lb_edad = ctk.CTkLabel(self.ventana_principal, text="Ingrese la edad:", font=("Arial", 16))
        self.txt_edad = ctk.CTkEntry(self.ventana_principal, width=200)

        # UBICACION DE LABEL Y TXT PARA EDAD
        lb_edad.pack(pady=(10, 0))
        self.txt_edad.pack(pady=(0, 20))

        self.lb_mensaje = ctk.CTkLabel(self.ventana_principal, text="", font=("Arial", 16))
        self.lb_mensaje.pack(pady=(10, 0))

        btn_guardar_paciente = ctk.CTkButton(self.ventana_principal, text="Guardar Paciente", command=self.guardar_paciente)
        btn_guardar_paciente.pack(pady=(10, 20))

        self.textbox_pacientes = ctk.CTkTextbox(self.ventana_principal, width=500, height=500, font=("Arial", 16, "bold"))
        self.textbox_pacientes.pack(pady=(10, 20))

        self.cargar_textbox_pacientes()


    def ver_pantalla_registro_sintomas(self):
        self.limpiar_ventana_principal()

        lb_paciente = ctk.CTkLabel(self.ventana_principal, text="Seleccione un paciente:", font=("Arial", 16))
        lb_paciente.pack(pady=(10, 0))
        self.lista_pacientes = self.PacienteDAO.obtener_pacientes()
        self.cbo_pacientes = ctk.CTkComboBox(self.ventana_principal, values=[paciente.nombre for paciente in self.lista_pacientes], font=("Arial", 16)) # cbo = COMBOBOX
        self.cbo_pacientes.pack(pady=(0, 20))

        lb_sintoma = ctk.CTkLabel(self.ventana_principal, text="Seleccione un síntoma:", font=("Arial", 16))
        lb_sintoma.pack(pady=(10, 0))
        self.lista_sintomas = self.RegistroSintomaDAO.obtener_sintomas()
        self.cbo_sintomas = ctk.CTkComboBox(self.ventana_principal, values=[sintoma.nombre for sintoma in self.lista_sintomas], font=("Arial", 16))
        self.cbo_sintomas.pack(pady=(0, 20))

        lb_fecha = ctk.CTkLabel(self.ventana_principal, text="Ingrese una fecha:", font=("Arial", 16))
        lb_fecha.pack(pady=(10, 0))
        self.txt_fecha = DateEntry(self.ventana_principal, width=12, background='#4c684a', foreground='white', borderwidth=2)
        self.txt_fecha.pack(pady=(0, 20))

        lb_hora = ctk.CTkLabel(self.ventana_principal, text="Ingrese la hora:", font=("Arial", 16))
        self.txt_hora = ctk.CTkEntry(self.ventana_principal, width=200, placeholder_text="00")
        lb_hora.pack(pady=(10, 0))
        self.txt_hora.pack(pady=(0, 20))

        lb_observaciones = ctk.CTkLabel(self.ventana_principal, text="Ingrese observaciones:", font=("Arial", 16))
        self.txt_observaciones = ctk.CTkEntry(self.ventana_principal, width=200)
        lb_observaciones.pack(pady=(10, 0))
        self.txt_observaciones.pack(pady=(0, 20))

        self.lb_mensaje = ctk.CTkLabel(self.ventana_principal, text="", font=("Arial", 16))
        self.lb_mensaje.pack(pady=(10, 0))

        btn_registrar_sintoma = ctk.CTkButton(self.ventana_principal, text="Registrar Síntoma", command=self.registrar_sintoma)
        btn_registrar_sintoma.pack(pady=(0, 20))


    def ver_pantalla_registro_medicamentos(self):
        self.limpiar_ventana_principal()

    def ver_pantalla_historial_paciente(self):
        self.limpiar_ventana_principal()

    # ____________________ PACIENTES ______________________
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
        nombre = self.txt_nombre.get()
        edad = self.txt_edad.get()

        # Verificar si la edad es un número y convertirla
        try:
            edad = int(edad)
        except ValueError:
            self.lb_mensaje.configure(text="La edad debe ser un número válido.", text_color="red") # Mensaje de error
            return

        # Crear un nuevo paciente con los datos de los inputs
        nuevo_paciente = Paciente(id=None, nombre=nombre, edad=edad)

        # Llamar al metodo insertar_paciente de la instancia de PacienteDAO
        self.PacienteDAO.insertar_paciente(nuevo_paciente)
        self.lb_mensaje.configure(text="Paciente agregado correctamente.", text_color="green")  # Mensaje de éxito

        # Limpiar los campos de entrada después de guardar
        self.txt_nombre.delete(0, 'end')
        self.txt_edad.delete(0, 'end')

        self.cargar_textbox_pacientes()
    # ____________________ PACIENTES ______________________

    # ____________________ REGISTRO SINTOMA ______________________
    def registrar_sintoma(self):
        nombre_paciente = self.cbo_pacientes.get()
        nombre_sintoma = self.cbo_sintomas.get()

        index_paciente = [paciente.nombre for paciente in self.lista_pacientes].index(nombre_paciente)
        index_sintoma = [sintoma.nombre for sintoma in self.lista_sintomas].index(nombre_sintoma)

        # Obtener el objeto completo usando el índice
        paciente_seleccionado = self.lista_pacientes[index_paciente]
        sintoma_seleccionado = self.lista_sintomas[index_sintoma]

        fecha_seleccionada = self.txt_fecha.get()
        hora_ingresada = self.txt_hora.get()
        observaciones = self.txt_observaciones.get()

        try:
            # Verificar que sea un número
            hora_ingresada = int(hora_ingresada)

            # Verificar que tenga un máximo de 2 dígitos (0-24)
            if hora_ingresada < 0 or hora_ingresada > 24:
                raise ValueError("La hora debe estar entre 0 y 24.")

            # Formatear la hora a dos dígitos
            hora_ingresada = f"{hora_ingresada:02}"  # Esto agrega un cero a la izquierda si la hora tiene un solo digito

        except ValueError as e:
            self.lb_mensaje.configure(text=f"La hora ingresada es inválida: {e}", text_color="red")
            return

        # Combinar fecha y hora en un string
        fecha_hora = f"{fecha_seleccionada} {hora_ingresada}:00"

        print("fecha completa: ", fecha_hora)

        nuevo_registro_sintoma = RegistroSintoma(paciente_seleccionado, sintoma_seleccionado, fecha_hora, observaciones)


        self.RegistroSintomaDAO.insertar_registro_sintoma(nuevo_registro_sintoma)

        # Mostrar un mensaje de éxito y limpiar el campo de mensaje después de un momento
        self.lb_mensaje.configure(
            text=f"Se ha registrado correctamente el síntoma {sintoma_seleccionado.nombre} al paciente {paciente_seleccionado.nombre}",
            text_color="green"
        )

        self.after(8000, lambda: self.lb_mensaje.configure(text=""))  # Limpia el mensaje después de 8 segundos



