from abc import ABC, abstractmethod

# Clase abstracta Ciclista
class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self._identificador = identificador
        self._nombre = nombre
        self._tiempo_acumulado = 0

    @abstractmethod
    def imprimir_tipo(self):
        pass

    def get_identificador(self):
        return self._identificador

    def set_identificador(self, identificador):
        self._identificador = identificador

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_tiempo_acumulado(self):
        return self._tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo_acumulado):
        self._tiempo_acumulado = tiempo_acumulado

    def imprimir(self):
        return (f"Identificador: {self._identificador}, Nombre: {self._nombre}, "
                f"Tiempo Acumulado: {self._tiempo_acumulado} minutos")

# Clase Velocista
class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self._potencia_promedio = potencia_promedio
        self._velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self):
        return self._potencia_promedio

    def set_potencia_promedio(self, potencia_promedio):
        self._potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self):
        return self._velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio):
        self._velocidad_promedio = velocidad_promedio

    def imprimir_tipo(self):
        return "Es un Velocista"

    def imprimir(self):
        return (super().imprimir() + f", Potencia Promedio: {self._potencia_promedio} W, "
                f"Velocidad Promedio: {self._velocidad_promedio} km/h")

# Clase Escalador
class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self._aceleracion_promedio = aceleracion_promedio
        self._grado_rampa = grado_rampa

    def get_aceleracion_promedio(self):
        return self._aceleracion_promedio

    def set_aceleracion_promedio(self, aceleracion_promedio):
        self._aceleracion_promedio = aceleracion_promedio

    def get_grado_rampa(self):
        return self._grado_rampa

    def set_grado_rampa(self, grado_rampa):
        self._grado_rampa = grado_rampa

    def imprimir_tipo(self):
        return "Es un Escalador"

    def imprimir(self):
        return (super().imprimir() + f", Aceleración Promedio: {self._aceleracion_promedio} m/s^2, "
                f"Grado de Rampa: {self._grado_rampa}°")

# Clase Contrarrelojista
class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self._velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def imprimir_tipo(self):
        return "Es un Contrarrelojista"

    def imprimir(self):
        return (super().imprimir() + f", Velocidad Máxima: {self._velocidad_maxima} km/h")

# Clase Equipo
class Equipo:
    _total_tiempo = 0  # Atributo estático

    def __init__(self, nombre, pais):
        self._nombre = nombre
        self._pais = pais
        self._ciclistas = []

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_pais(self):
        return self._pais

    def set_pais(self, pais):
        self._pais = pais

    def añadir_ciclista(self, ciclista):
        self._ciclistas.append(ciclista)

    def listar_equipo(self):
        return [ciclista.get_nombre() for ciclista in self._ciclistas]

    def buscar_ciclista(self, nombre):
        for ciclista in self._ciclistas:
            if ciclista.get_nombre() == nombre:
                return ciclista.imprimir()
        return "Ciclista no encontrado"

    def calcular_total_tiempo(self):
        Equipo._total_tiempo = sum(ciclista.get_tiempo_acumulado() for ciclista in self._ciclistas)
        return Equipo._total_tiempo

    def imprimir(self):
        return (f"Nombre del Equipo: {self._nombre}, País: {self._pais}, "
                f"Total Tiempo: {Equipo._total_tiempo} minutos")

# Clase Prueba
if __name__ == "__main__":
    equipo1 = Equipo("Sky", "Estados Unidos")

    velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
    escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
    contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)

    equipo1.añadir_ciclista(velocista1)
    equipo1.añadir_ciclista(escalador1)
    equipo1.añadir_ciclista(contrarrelojista1)

    velocista1.set_tiempo_acumulado(365)
    escalador1.set_tiempo_acumulado(385)
    contrarrelojista1.set_tiempo_acumulado(370)

    print(equipo1.imprimir())
    print("Ciclistas en el equipo:", equipo1.listar_equipo())
    print(equipo1.buscar_ciclista("Egan Bernal"))
    print("Total de tiempos del equipo:", equipo1.calcular_total_tiempo())
