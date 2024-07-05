from Classes.clases import *
from Functions.functions import *

# Funcion principal
def main():
    # Inicializacion de atributos
    while True:
        # Metodo de control para el amnejo de errores por inputs
        try:
            print('''
====================Demonstracion de Clases======================
======================= Tiempo - Completo =======================
''')
            # Inicializacion de variables
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            areaFormacion = input('Ingrese su Area de Formacion: ')
            tituloProfesional = input('Ingrese su Titulo Profesional: ')
            unidadAcademica = input('Ingrese su Unidad Academica: ')
            categoria = int(input('(INT)Ingrese su Categoria: '))
            puntos = int(input('(INT)Ingrese sus Puntos: '))
            salario = int(input('(INT)Ingrese su Salario: '))
            clear() #Limpiar la terminal
            break # Terminar el Ciclo

        #Control de los errores, asignandole un valor al value error, sabremos que fue lo que ocurrio
        except ValueError as e:

            #Mensaje de control y muestra del error
            print(f'Error: Ingrese un valor válido. Detalle: {e}')

            #Volver a preguntar todo desde el principio
            continue
#Imprimimos los datos que recolectamos
    print('''
====================Demonstracion de Clases======================
======================= Tiempo - Completo =======================
''')
    # Creamos una variable que contenga los datos que le asignamos
    tiempo_completo = TiempoCompleto(
                                        idPersona,
                                        nomPersona,
                                        apePersona,
                                        fechaNacimiento,
                                        ciudadNacimiento,
                                        genero,
                                        estrato,
                                        areaFormacion,
                                        tituloProfesional,
                                        unidadAcademica,
                                        categoria,
                                        puntos,
                                        salario
                                    )

    # Nombramos los metodos de la clase
    tiempo_completo.informacion()
    tiempo_completo.motrarDG()
    tiempo_completo.calcularEPS()
    tiempo_completo.calcularPension()
    tiempo_completo.calcularARL()
    tiempo_completo.calculaSENA()
    tiempo_completo.calculaCajas()
    tiempo_completo.calculandoICBF()
    tiempo_completo.calculaAuxilio()
    tiempo_completo.mostrarDatosDocentes()
    tiempo_completo.calculaSueldo()
    tiempo_completo.liquidarTC()
    tiempo_completo.mostrarLightTC()

    
    #Ejecutamos la funcion que va a continuar con la siguiente clase, limpiando la pantalla si decidimos continuar
    continuar(clear)


    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Ocasionales =========================
          
''')
            #Atributos de la clase
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            areaFormacion = input('Ingrese su Area de Formacion: ')
            tituloProfesional = input('Ingrese su Titulo Profesional: ')
            unidadAcademica = input('Ingrese su Unidad Academica: ')
            ultimoTitulo = (input('Ingrese su Ultimo Titulo: '))
            numMeses = int(input('(INT)Ingrese sus Numero de Meses: '))
            salario = int(input('(INT)Ingrese su Salario: '))
            break
        except ValueError as e:
            print(f'Error: Ingrese un valor válido. Detalle: {e}')
            continue

    print('''
          

========================= Ocasionales =========================
          
''')
    
    ocasionales = Ocasionales(
                                idPersona,
                                nomPersona,
                                apePersona,
                                fechaNacimiento,
                                ciudadNacimiento,
                                genero,
                                estrato,
                                areaFormacion,
                                tituloProfesional,
                                unidadAcademica,
                                ultimoTitulo,
                                numMeses,
                                salario
                                )
    ocasionales.informacion()
    ocasionales.motrarDG()
    ocasionales.calcularEPS()
    ocasionales.calcularPension()
    ocasionales.calcularARL()
    ocasionales.calculaSENA()
    ocasionales.calculaCajas()
    ocasionales.calculandoICBF()
    ocasionales.calculaAuxilio()
    ocasionales.mostrarDatosDocentes()
    ocasionales.calcularSueldo()
    ocasionales.liquidarOC()
    ocasionales.mostrarLiqOC()

    continuar(clear)


    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Hora - Catedra =========================
          
''')

            #Atributos de la clase
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            areaFormacion = input('Ingrese su Area de Formacion: ')
            tituloProfesional = input('Ingrese su Titulo Profesional: ')
            unidadAcademica = input('Ingrese su Unidad Academica: ')
            ultimoTitulo = input('Ingrese su Ultimo Titulo: ')
            numHoras = int(input('(INT)Ingrese sus Numero de Meses: '))
            valorContrato = int(input('(INT)Ingrese su Valor de Contrato: '))
            salario = int(input('(INT)Ingrese su Salario: '))
            break
        except ValueError as e:
            print(f'Error: Ingrese un valor válido. Detalle: {e}')
            continue
    
    print('''
          

========================= Hora - Catedra =========================
          
''')
    # Nombtramos la clase con una variable para facil acceso de los atributos
    hora_catedra = HoraCatedra(
                                idPersona,
                                nomPersona,
                                apePersona,
                                fechaNacimiento,
                                ciudadNacimiento,
                                genero,
                                estrato,
                                areaFormacion,
                                tituloProfesional,
                                unidadAcademica,
                                ultimoTitulo,
                                numHoras,
                                valorContrato,
                                salario
                            )
    
    #Llamamos los metodos de las funciones
    hora_catedra.informacion()
    hora_catedra.motrarDG()
    hora_catedra.calcularEPS()
    hora_catedra.calcularPension()
    hora_catedra.calcularARL()
    hora_catedra.calculaSENA()
    hora_catedra.calculaCajas()
    hora_catedra.calculandoICBF()
    hora_catedra.calculaAuxilio()
    hora_catedra.mostrarDatosDocentes()
    hora_catedra.calcularSueldo()
    hora_catedra.liquidarHC()
    hora_catedra.mostrarLiqHC()
# Limpiamos la consola y preguntamos si deseamos continuar
    continuar(clear)

    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Auxiliar =========================
          
''')
            #Atributos de la clase
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            dependencia = input('Ingrese su Area de Formacion: ')
            titulo = input('Ingrese su Titulo Profesional: ')
            fechaVinculacion = input('Ingrese su Unidad Academica: ')
            nivel = input('Ingrese su Ultimo Titulo: ')
            salario = int(input('(INT)Ingrese su Salario: '))
            break

        #Control demlos errores
        except ValueError as e:

            #Impresion del error
            print(f'Error: Ingrese un valor válido. Detalle: {e}')
            #
            continue
    print('''
          

========================= Auxiliar =========================
          
''')


    auxiliar = Auxiliar(
                        idPersona,
                        nomPersona,
                        apePersona,
                        fechaNacimiento,
                        ciudadNacimiento,
                        genero,
                        estrato,
                        dependencia,
                        titulo,
                        fechaVinculacion,
                        nivel,
                        salario
                        )
    # Llamamos las funciones inherentes de la clase
    auxiliar.informacion()
    auxiliar.motrarDG()
    auxiliar.calcularEPS()
    auxiliar.calcularPension()
    auxiliar.calcularARL()
    auxiliar.calculaSENA()
    auxiliar.calculaCajas()
    auxiliar.calculandoICBF()
    auxiliar.calculaAuxilio()
    auxiliar.mostrarDatosAdmin()
    auxiliar.mostrarDatosAdminPlanta()
    auxiliar.calcularSueldo()
    auxiliar.liquidarAux()    
    auxiliar.mostrarLiqAux()

    #Ejecutamos la funcion que va a continuar con la siguiente clase, limpiando la pantalla si decidimos continuar
    continuar(clear)
# Preguntamos si deseamos continuar
    continuar(clear)


    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Tecnico =========================
          
''')
            #Atributos de la clase
            idPersona = int(input('Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('Ingrese su Estrato: '))
            dependencia = input('Ingrese su Area de Formacion: ')
            titulo = input('Ingrese su Titulo Profesional: ')
            fechaVinculacion = input('Ingrese su Unidad Academica: ')
            nivel = input('Ingrese su Ultimo Titulo: ')
            salario = int(input('Ingrese su Salario: '))
            #Terminamos el bucle
            break

        # Control de errores del usuario
        except ValueError as e:
            print(f'Error: Ingrese un valor válido. Detalle: {e}')
            # Continuamos el bucle
            continue
    print('''
          

========================= Tecnico =========================
          
''')
#Nombramos una variable de facil acceso
    tecnico = Tecnico(
                        idPersona,
                        nomPersona,
                        apePersona,
                        fechaNacimiento,
                        ciudadNacimiento,
                        genero,
                        estrato,
                        dependencia,
                        titulo,
                        fechaVinculacion,
                        nivel,
                        salario
                        )
    
    #Llamamos los metodos 
    tecnico.informacion()
    tecnico.motrarDG()
    tecnico.calcularEPS()
    tecnico.calcularPension()
    tecnico.calcularARL()
    tecnico.calculaSENA()
    tecnico.calculaCajas()
    tecnico.calculandoICBF()
    tecnico.calculaAuxilio()
    tecnico.mostrarDatosAdmin()
    tecnico.mostrarDatosAdminPlanta()
    tecnico.calcularSueldo()
    tecnico.liquidarTec()
    tecnico.mostrarTec()

    #Ejecutamos la funcion que va a continuar con la siguiente clase, limpiando la pantalla si decidimos continuar
    continuar(clear)

#Preguntamos si queremos continuar y limpiamos la consola
    continuar(clear)

    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Profesional =========================
          
''')
            #Atributos de la clase
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            dependencia = input('Ingrese su Area de Formacion: ')
            titulo = input('Ingrese su Titulo Profesional: ')
            fechaVinculacion = input('Ingrese su Unidad Academica: ')
            nivel = input('Ingrese su Ultimo Titulo: ')
            salario = int(input('(INT)Ingrese su Salario: '))
            # Terminamos el bucle
            break
        #Control de los errores de usuario
        except ValueError as e:

            #Desplegamos un mensaje de error
            print(f'Error: Ingrese un valor válido. Detalle: {e}')


            #Repetimos las preguntas
            continue
#Imprimimos la informacion que acabamos de digitar
    print('''
          

========================= Profesional =========================
          
''')
    #Nombramos las clase con los atributos que ya le asignamos
    profesional = Profesional(
                                idPersona,
                                nomPersona,
                                apePersona,
                                fechaNacimiento,
                                ciudadNacimiento,
                                genero,
                                estrato,
                                dependencia,
                                titulo,
                                fechaVinculacion,
                                nivel,
                                salario
                                )

#Llamamos los metodos de la clase
    profesional.informacion()
    profesional.motrarDG()
    profesional.calcularEPS()
    profesional.calcularPension()
    profesional.calcularARL()
    profesional.calculaSENA()
    profesional.calculaCajas()
    profesional.calculandoICBF()
    profesional.calculaAuxilio()
    profesional.mostrarDatosAdmin()
    profesional.mostrarDatosAdminPlanta()
    profesional.calcularSueldo()
    profesional.liquidarProf()
    profesional.mostrarLiqProf()

    #Ejecutamos la funcion que va a continuar con la siguiente clase, limpiando la pantalla si decidimos continuar
    continuar(clear)

#Preguntamos si queremos continuar y limpiamos la consola
    continuar(clear)

    # Creamos el bucle de nuevo
    while True:
        # Control de errores
        try:
            print('''
          

========================= Ops =========================
          
''')
            #Atributos de la clase
            
            idPersona = int(input('(INT)Ingrese su Id: '))
            nomPersona = input('Ingrese su Nombre(s): ')
            apePersona = input('Ingrese su Apellido(s): ')
            fechaNacimiento = input('Ingrese su Fecha de Nacimiento: ')
            ciudadNacimiento = input('Ingrese su Ciudad de Nacimiento: ')
            genero = input('Ingrese su Genero: ')
            estrato = int(input('(INT)Ingrese su Estrato: '))
            dependencia = input('Ingrese su Area de Formacion: ')
            fechaVinculacion = input('Ingrese su Unidad Academica: ')
            numMeses = int(input('(INT)Ingrese el Numero de Meses: '))
            valorContrato = int(input('(INT)Ingrese el Valor de Contrato: '))
            salario = int(input('(INT)Ingrese su Salario: '))

            #Terminamos el bucle
            break

        #Le damos control a los errores de input
        except ValueError as e:

            #Mostramos un mensaje de error
            print(f'Error: Ingrese un valor válido. Detalle: {e}')

            #Volvemos a pedir los datos
            continue


#Imprimimos los datos que ingresamos
    print('''
          

========================= Ops =========================
          
''')
    

    # Creamos la variable con los atributos que ya nombramos
    ops = Ops(
                idPersona,
                nomPersona,
                apePersona,
                fechaNacimiento,
                ciudadNacimiento,
                genero,
                estrato,
                dependencia,
                titulo,
                fechaVinculacion,
                numMeses,
                valorContrato,
                salario
                )

    # Llamamos los metodos de la clase
    ops.informacion()
    ops.motrarDG()
    ops.calcularEPS()
    ops.calcularPension()
    ops.calcularARL()
    ops.calculaSENA()
    ops.calculaCajas()
    ops.calculandoICBF()
    ops.calculaAuxilio()
    ops.mostrarDatosAdmin()
    ops.liquidarValorContrato()
    ops.mostrarLiqOps()

if __name__ == '__main__':
    main()