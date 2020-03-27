from threading import Thread, Lock
from utils import reloj
from random import randint, uniform


class Excavador(Thread):

    excavar_lock = Lock() # Tienen que acceder a este para excavar

    def __init__(self, nombre, berlin, tunel):
        super().__init__()
        self.nombre = nombre
        self.berlin = berlin
        self.tunel = tunel
        print(f"Se ha creado el thread excavador {self.nombre}")

    def run(self):
        '''
        Funcionalidad de Excavador que crea x metros de tunel cada 10 min,
        cada iteracion chequea si se cumple que hay problema con la picota (10%)
        '''
        while self.tunel.metros_avanzados < self.tunel.largo:
            reloj(10)
            # Metros que avanza el thread
            self.avanzar(randint(50, 100))

            prob_picota = uniform(0, 1)
            if prob_picota < 0.1:
                print(f"{self.nombre}: Oh no! Se ha roto la picota")
                self.problema_picota()

    def problema_picota(self):
        '''
        Probabilida de problema con la picota de 10%
        Se llama a berlin para resolverlo
        '''
        with self.berlin:
            print(f'Berlin solucionando problema de {self.nombre}')
            reloj(5)
            print('Berlin: Problema solucionado!')

    def avanzar(self, metros):
        '''
        Usar este método para avanzar en la excavación del túnel
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param metros: int
        '''

        with self.excavar_lock:
            print(f'{self.nombre}: avanzando {metros} metros')
            self.tunel.metros_avanzados += metros
            print(f'Llevamos {self.tunel.metros_avanzados} metros')

            if self.tunel.metros_avanzados >= self.tunel.largo:
                print('Hemos terminado el tunel!')
                self.tunel.tunel_listo.set()
