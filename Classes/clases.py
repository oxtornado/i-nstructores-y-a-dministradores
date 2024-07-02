# from colorama import Fore, Back

class Persona:
    # Creacion de atributos de la clase Persona
    def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato):
        self.__idPersona = idPersona
        self.__nomPersona = nomPersona
        self.__apePersona = apePersona
        self.__fechaNacimiento = fechaNacimiento
        self.__ciudadNacimiento = ciudadNacimiento
        self.__genero = genero
        self.__estrato = estrato

    #def set_ (self, value):
    #   self.__ = value 
    def set_idPersona (self, value):
      self.__idPersona = value
    def set_nomPersona (self, value):
      self.__nomPersona = value
    def set_apePersona (self, value):
      self.__apePersona = value
    def set_fechaNacimiento (self, value):
      self.__fechaNacimiento = value
    def set_ciudadNacimiento (self, value):
      self.__ciudadNacimiento = value
    def set_ (self, value):
      self.__ = value
    def set_estrato (self, value):
      self.__estrato = value

    # def get_ (self):
    #   return self.__
    def get_idPersona (self):
      return self.__idPersona
    def get_nomPersona (self):
      return self.__nomPersona
    def get_apePersona (self):
      return self.__apePersona
    def get_fechaNacimiento (self):
      return self.__fechaNacimiento
    def get_ciudadNacimiento (self):
      return self.__ciudadNacimiento
    def get_genero (self):
      return self.__genero
    def get_estrato (self):
      return self.__estrato
    
    # Creacion de metodos
    def motrarDG(self):
      print('''
|   Calculando su mostrarDG... 
''')
    def calcularEPS(self):
      print('''
|   Calculando su calcularEPS...
''')
    def calcularPension(self):
      print('''
|   Calculando su calcularPension...
''')
    def calcularARL(self):
      print('''
|   Calculando su calcularARL...
''')
    def calculaSENA(self):
      print('''
|   Calculando su calculaSENA...
''')
    def calculaCajas(self):
      print('''
|   Calculando su calculaCajas...
''')
    def calculandoICBF(self):
      print('''
|   Calculando su calculandoICBF...
''')
    def calculaAuxilio(self):
      print('''
|   Calculando su calculaAuxilio...
''')


class Docentes(Persona):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato)
    self.__areaFormacion = areaFormacion
    self.__tituloProfesional = tituloProfesional
    self.__unidadAcademica = unidadAcademica

    #def set_ (self, value):
    #   self.__ = value
  def set_areaFormacion (self, value):
    self.__areaFormacion = value
  def set_tituloProfesional (self, value):
    self.__tituloProfesional = value
  def set_unidadAcademica (self, value):
    self.__unidadAcademica = value


    # def get_ (self):
    #   return self.__
  def get_areaFormacion (self):
    return self.__areaFormacion
  def get_tituloProfesional (self):
    return self.__tituloProfesional
  def get_unidadAcademica (self):
    return self.__unidadAcademica
    
    # Creacion de metodos
  def mostrarDatosDocentes(self):
      print('''
|   Calculando su calculaAuxilio...
''')

class TiempoCompleto(Docentes):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica, categoria, puntos, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica)
    self.__categoria = categoria
    self.__puntos = puntos
    self.__salario = salario
    #def set_ (self, value):
    #   self.__ = value
  def set_categoria (self, value):
    self.__categoria = value
  def set_puntos (self, value):
    self.__puntos = value
  def set_salario (self, value):
    self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_categoria (self):
    return self.__categoria
  def get_puntos (self):
    return self.__puntos
  def get_salario (self):
    return self.__salario
    
    # Creacion de metodos
  def calculaSueldo(self):
    print('''
|   Calculando su calculaSueldo...
''')
  def liquidarTC(self):
    print('''
|   Calculando su liquidarTC...
''')
  def mostrarLightTC(self):
      print('''
|   Calculando su LightTC...
''')
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Area de Formacion',
          'Titulo Profesional',
          'Unidad Academica',
          'Categoria',
          'Puntos',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_areaFormacion(),
              self.get_tituloProfesional(),
              self.get_unidadAcademica(),
              str(self.get_categoria()),  # Convert categoria and puntos to string
              str(self.get_puntos()),
              str(self.get_salario())
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

#-------------------------------------------------
class Ocasionales(Docentes):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica, ultimoTitulo, numMeses, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica)
    self.__ultimoTitulo = ultimoTitulo
    self.__numMeses = numMeses
    self.__salario = salario

    #def set_ (self, value):
    #   self.__ = value
  def set_ultimoTitulo (self, value):
    self.__ultimoTitulo = value
  def set_numMeses (self, value):
    self.__numMeses = value
  def set_salario (self, value):
    self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_ultimoTitulo (self):
    return self.__ultimoTitulo
  def get_numMeses (self):
    return self.__numMeses
  def get_salario (self):
    return self.__salario
    
    # Creacion de metodos
  def calcularSueldo(self):
      print('''
|   Calculando su calcularSueldo...
''')
  def liquidarOC(self):
      print('''
|   Calculando su liquidarOC...
''')

  def mostrarLiqOC(self):
      print('''
|   Calculando su mostrarLiqOC...
''')
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Area de Formacion',
          'Titulo Profesional',
          'Unidad Academica',
          'Ultimo Titulo',
          'Numero de Meses',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_areaFormacion(),
              self.get_tituloProfesional(),
              self.get_unidadAcademica(),
              str(self.get_ultimoTitulo()),  # Convert categoria and puntos to string
              str(self.get_numMeses()),
              str(self.get_salario())
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

class HoraCatedra(Docentes):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica, ultimoTitulo, numHoras, valorContrato, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, areaFormacion, tituloProfesional, unidadAcademica)
    self.__ultimoTitulo = ultimoTitulo
    self.__numHoras = numHoras
    self.__valorContrato = valorContrato
    self.__salario = salario
    #def set_ (self, value):
    #   self.__ = value
  def set_ultimoTitulo (self, value):
    self.__ultimoTitulo = value
  def set_numHoras (self, value):
    self.__numHoras = value
  def set_valorContrato (self, value):
    self.__valorContrato = value
  def set_salario (self, value):
    self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_ultimoTitulo (self):
    return self.__ultimoTitulo
  def get_numHoras (self):
    return self.__numHoras
  def get_valorContrato (self):
    return self.__valorContrato
  def get_salario (self):
    return self.__salario
    
    # Creacion de metodos
  def calcularSueldo(self):
      print('''
|   Calculando su calcularSueldo...
''')
  def liquidarHC(self):
      print('''
|   Calculando su liquidarHC...
''')
  def mostrarLiqHC(self):
      print('''
|   Calculando su mostrarLiqHC...
''')
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Area de Formacion',
          'Titulo Profesional',
          'Unidad Academica',
          'Ultimo Titulo',
          'Numero de Horas',
          'Valor de Contrato',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_areaFormacion(),
              self.get_tituloProfesional(),
              self.get_unidadAcademica(),
              str(self.get_ultimoTitulo()),  # Convert categoria and puntos to string
              str(self.get_numHoras()),
              str(self.get_valorContrato()),
              str(self.get_salario())
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

class Administrativos(Persona):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato)
    self.__dependencia = dependencia
    self.__titulo = titulo

    #def set_ (self, value):
    #   self.__ = value
  def set_dependencia (self, value):
    self.__dependencia = value    
  def set_titulo (self, value):
    self.__titulo = value

    # def get_ (self):
    #   return self.__
  def get_dependencia (self):
      return self.__dependencia
  def get_titulo (self):
      return self.__titulo
    
    # Creacion de metodos
  def mostrarDatosAdmin(self):
      print('''
|   Calculando su mostrarDatosAdmin...
''')

class Planta(Administrativos):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)
    self.__fechaVinculacion = fechaVinculacion

    #def set_ (self, value):
    #   self.__ = value
  def set_fechaVinculacion (self, value):
      self.__fechaVinculacion = value


    # def get_ (self):
    #   return self.__
  def get_fechaVinculacion (self):
    return self.__fechaVinculacion
    
    # Creacion de metodos
  def mostrarDatosAdminPlanta(self):
      print('''
|   Calculando su mostrarDatosAdminPlanta...
''')

class Auxiliar(Planta):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion, nivel, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)
    self.__nivel = nivel
    self.__salario = salario

    #def set_ (self, value):
    #   self.__ = value
  def set_nivel (self, value):
    self.__nivel = value
  def set_salario (self, value):
    self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_nivel (self):
    return self.__nivel
  def get_salario (self):
    return self.__salario
    
    # Creacion de metodos

#     def (self):
#       print('''
# |   Calculando su ...
# ''')
    
  def calcularSueldo(self):
      print('''
|   Calculando su calcularSueldo...
''')
  def liquidarAux(self):
      print('''
|   Calculando su liquidarAux...
''')
  def mostrarLiqAux(self):
      print('''
|   Calculando su mostrarLiqAux...
''')
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Dependencia',
          'Titulo',
          'Fecha de Vinculacion',
          'Nivel',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_dependencia(),
              self.get_titulo(),
              self.get_fechaVinculacion(),
              str(self.get_nivel()),  # Convert categoria and puntos to string
              str(self.get_salario()),
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))


class Tecnico(Planta):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion, nivel, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)
    self.__nivel = nivel
    self.__salario = salario

    #def set_ (self, value):
    #   self.__ = value
  def set_nivel (self, value):
    self.__nivel = value
  def set_salario (self, value):
      self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_nivel (self):
    return self.__nivel
  def get_salario (self):
      return self.__salario

      # Creacion de metodos

  #     def (self):
  #       print('''
  # |   Calculando su ...
  # ''')

  def liquidarTec(self):
      print('''
|   Calculando su liquidarTec...
''')
      
  def calcularSueldo(self):
      print('''
|   Calculando su calcularSueldo...
''')
  def mostrarTec(self):
      print('''
|   Calculando su mostrarTec...
''') 
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Dependencia',
          'Titulo',
          'Fecha de Vinculacion',
          'Nivel',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_dependencia(),
              self.get_titulo(),
              self.get_fechaVinculacion(),
              str(self.get_nivel()),  # Convert categoria and puntos to string
              str(self.get_salario()),
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

class Profesional(Planta):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion, nivel, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)
    self.__nivel = nivel
    self.__salario = salario

    #def set_ (self, value):
    #   self.__ = value
  def set_nivel (self, value):
    self.__nivel = value
  def set_ (self, value):
      self.__ = value

    # def get_ (self):
    #   return self.__
  def get_nivel (self):
    return self.__nivel
  def get_salario (self):
      return self.__salario

    # Creacion de metodos

#     def (self):
#       print('''
# |   Calculando su ...
# ''')
  def calcularSueldo(self):
      print('''
|   Calculando su calcularSueldo...
''')
  def liquidarProf(self):
      print('''
|   Calculando su liquidarProf...
''')
  def mostrarLiqProf(self):
      print('''
|   Calculando su mostrarLiqProf...
''')
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Dependencia',
          'Titulo',
          'Fecha de Vinculacion',
          'Nivel',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_dependencia(),
              self.get_titulo(),
              self.get_fechaVinculacion(),
              str(self.get_nivel()),  # Convert categoria and puntos to string
              str(self.get_salario()),
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
      
class Ops(Administrativos):
  def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion, numMeses, valorContrato, salario):
    super().__init__(idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)
    self.__fechaVinculacion = fechaVinculacion
    self.__numMeses = numMeses
    self.__valorContrato = valorContrato
    self.__salario = salario

    #def set_ (self, value):
    #   self.__ = value
  def set_fechaVinculacion (self, value):
    self.__fechaVinculacion = value
  def set_numMeses (self, value):
    self.__numMeses = value
  def set_valorContrato (self, value):
    self.__valorContrato = value
  def set_salario (self, value):
    self.__salario = value

    # def get_ (self):
    #   return self.__
  def get_fechaVinculacion (self):
    return self.__fechaVinculacion
  def get_numMeses (self):
    return self.__numMeses
  def get_valorContrato (self):
    return self.__valorContrato
  def get_salario (self):
    return self.__salario


    # Creacion de metodos

#     def (self):
#       print('''
# |   Calculando su ...
# ''')
  def liquidarValorContrato(self):
    print('''
|   Calculando su liquidarValorContrato...
''')
  def mostrarLiqOps(self):
    print('''
|   Calculando su mostrarLiqOps...
''')
  def informacion(self):
    print(f'''

''')
    
  def informacion(self):
      headers = [
          'Id',
          'Nombre(s)',
          'Apellido(s)',
          'Fecha de Nacimiento',
          'Ciudad de Nacimiento',
          'Genero',
          'Estrato',
          'Dependencia',
          'Titulo',
          'Fecha de Vinculacion',
          'Numero de Meses',
          'Valor de Contrato',
          'Salario'
      ]
      # Construct rows as a list of tuples
      rows = [
          (
              self.get_idPersona(),
              self.get_nomPersona(),
              self.get_apePersona(),
              self.get_fechaNacimiento(),
              self.get_ciudadNacimiento(),
              self.get_genero(),
              str(self.get_estrato()),  # Convert estrato to string for consistency
              self.get_dependencia(),
              self.get_titulo(),
              self.get_fechaVinculacion(),
              str(self.get_numMeses()),  # Convert categoria and puntos to string
              str(self.get_valorContrato()),
              str(self.get_salario())
          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
      max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

      # Print headers
      print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))

      # Print separator
      print('-+-'.join('-' * length for length in max_lengths))

      # Print rows
      for row in rows:
          print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))