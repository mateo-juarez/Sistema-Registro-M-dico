from src.dao.paciente_dao import PacienteDAO
from src.gui import MainUI
from src.model.entidades import Paciente

# Crear instancia de paciente
#nuevo_paciente = Paciente(id=None, nombre="Juan Perez", edad=30)

# Insertar paciente
#PacienteDAO.insertar_paciente(nuevo_paciente)


#dao = PacienteDAO()
#pacientes = dao.obtener_pacientes()

#print("Lista obtenida:")
#for paciente in pacientes:
    #print(f"ID: {paciente.id}, Nombre: {paciente.nombre}, Edad: {paciente.edad}")

app = MainUI()
app.mainloop()