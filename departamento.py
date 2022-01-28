#Nombre: Andrea Conde Pérez
#Materia: Estructura de datos
#Carrera: Ingeniería en software 3er nivel Aula - C1


class Departamento:
  secuencia=1
  departamentos = [{"departamento":1, "nombre":"Conserjeria" }]
  def __init__(self, descrip):
    Departamento.secuencia +=1
    self.codigo = Departamento.secuencia
    self.departamento = descrip
  def  registro(self):
    return {"departamento": self.codigo, "nombre": self.departamento}
