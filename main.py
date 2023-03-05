from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1)
    print(grupo1)
    print(grupo1.grado)

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

    grupo3 = Grupo()
    grupo4 = Grupo()
    grupo5 = Grupo()
    grupo3.agregarAlumno("Kelly")
    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
    grupo5.agregarAlumno("Javier")

    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)
    print(grupo5.listadoAlumnos)

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
    print(len(grupo3._asignaturas))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)
    Grupo.asignarNombre()
    print(Grupo.grado)
