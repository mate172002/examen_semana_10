class NodoTarea:
    def __init__(self, nombre, estado="pendiente"):
        self.nombre = nombre
        self.estado = estado
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, estado)
        if not self.cabeza:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def listar_tareas(self):
        actual = self.cabeza
        while actual:
            print(f"Tarea: {actual.nombre}, Estado: {actual.estado}")
            actual = actual.siguiente

class NodoProyecto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.tareas = ListaTareas()
        self.siguiente = None

class ListaProyectos:
    def __init__(self):
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        nuevo_proyecto = NodoProyecto(id, nombre)
        if not self.cabeza:
            self.cabeza = nuevo_proyecto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto

    def listar_proyectos(self):
        actual = self.cabeza
        while actual:
            print(f"Proyecto ID: {actual.id}, Nombre: {actual.nombre}")
            actual.tareas.listar_tareas()
            actual = actual.siguiente

# Ejemplo breve de uso
proyectos = ListaProyectos()
proyectos.agregar_proyecto(1, "Proyecto Mateo")
proyectos.cabeza.tareas.agregar_tarea("Diseñar interfaz")

proyectos.listar_proyectos()
