from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

def testMetodosAsignatura():
    asignatura1 = Asignatura("Vision por Computador")
    asignatura2 = Asignatura("POO", "Salon 503B")

    ok = False
    if str(asignatura1) == "Vision por Computador remoto" and\
       str(asignatura2) == "POO Salon 503B":
        ok = True

    assert(ok)

def testMetodosAgregarGrupo():
    asignatura1 = Asignatura("Vision por Computador")
    asignatura2 = Asignatura("POO", "Salon 503B")

    grupo1 = Grupo()
    grupo2 = Grupo("Grupo 32")
    grupo3 = Grupo("Grupo 23", [asignatura1])
    grupo4 = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])

    grupo1.agregarAlumno("Alumno10")
    grupo2.agregarAlumno("Alumno20")
    grupo3.agregarAlumno("Alumno30")
    grupo4.agregarAlumno("Alumno40")

    grupo1.agregarAlumno("Alumno11")
    grupo2.agregarAlumno("Alumno21")
    grupo3.agregarAlumno("Alumno31")
    grupo4.agregarAlumno("Alumno41")

    grupo1.agregarAlumno("Alumno14", ["Alumno12", "Alumno13"])
    grupo2.agregarAlumno("Alumno24", ["Alumno22", "Alumno23"])
    grupo3.agregarAlumno("Alumno34", ["Alumno32", "Alumno33"])
    grupo4.agregarAlumno("Alumno44", ["Alumno42", "Alumno43"])

    ok = False
    if str(grupo1) == "Grupo de estudiantes: grupo predeterminado" and grupo1.listadoAlumnos == ["Alumno10", "Alumno11", "Alumno12", "Alumno13", "Alumno14"] and\
       str(grupo2) == "Grupo de estudiantes: Grupo 32" and grupo2.listadoAlumnos == ["Alumno20", "Alumno21", "Alumno22", "Alumno23", "Alumno24"] and \
       str(grupo3) == "Grupo de estudiantes: Grupo 23" and grupo3.listadoAlumnos == ["Alumno30", "Alumno31", "Alumno32", "Alumno33", "Alumno34"] and\
       str(grupo4) == "Grupo de estudiantes: Grupo 12" and grupo4.listadoAlumnos == ["Jaime", "David", "Oswaldo", "Alumno40", "Alumno41", "Alumno42", "Alumno43", "Alumno44"]:
        ok = True
    
    assert(ok)

def testMetodosListadoGrupo():
    asignatura1 = Asignatura("Vision por Computador")
    asignatura2 = Asignatura("POO", "Salon 503B")

    grupo = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])
    grupo.listadoAsignaturas(asignatura1="Fundamentos de programacion", 
                             asignatura2="Ecuaciones diferenciales", 
                             asignatura3="Inteligencia artificial")

    ok = False
    if grupo._asignaturas[0]._nombre == "Vision por Computador" and\
       grupo._asignaturas[1]._nombre == "POO" and\
       grupo._asignaturas[2]._nombre == "Fundamentos de programacion" and\
       grupo._asignaturas[3]._nombre == "Ecuaciones diferenciales" and\
       grupo._asignaturas[4]._nombre == "Inteligencia artificial":
        ok = True
    
    assert(ok)

def testMetodosAsignarGrupo():
    Grupo.asignarNombre()
    nombre1 = Grupo.grado

    Grupo.asignarNombre("Grado 34")
    nombre2 = Grupo.grado

    Grupo.asignarNombre("otra grado")
    
    ok = False
    if nombre1 == "Grado 6" and nombre2 == "Grado 34" and Grupo.grado == "otra grado":
        ok = True
    
    assert(ok)
