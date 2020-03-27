from threading import Thread, Lock
from random import randint, uniform
from utils import reloj


class Imprimidor(Thread):

    impresion_lock = Lock()

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__()
        self.nombre = nombre
        self.daemon = True
        self.berlin = berlin
        self.bolsa_dinero = bolsa_dinero
        print(f"Se ha creado el thread imprimidor {self.nombre}")

    def run(self):
        '''
        Funcionalidad de iMPRIMIDOR que imprime dinero cada 5 minutos, cada
        iteracion chequea si se cumple que hay problema con el dinero (20%)
        '''
        while True:
            reloj(10)
            self.imprimir_dinero(randint(100000, 500000))
            prob_papel = uniform(0, 1)
            if prob_papel < 0.2:
                print(f"{self.nombre}: Oh no! Ha habido un problema con el papel")
                # Llama al problema de papel
                self.problema_papel()

    def imprimir_dinero(self, dinero):
        '''
        Llamar a este método para imprimir dinero.
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param dinero:
        :return:
        '''
        with self.impresion_lock:
            print(f'{self.nombre}: imprimiendo {dinero} euros')
            self.bolsa_dinero.dinero_acumulado += dinero
            print(f'Llevamos {self.bolsa_dinero.dinero_acumulado} euros en total')

            if self.bolsa_dinero.dinero_acumulado >= self.bolsa_dinero.meta_dinero:
                print('Hemos alcanzado la meta de dinero!')
                self.bolsa_dinero.dinero_listo.set()

    def problema_papel(self):
        '''
        Probabilidad de problema con el papel de 20%
        '''
        with self.berlin:
            print(f'Berlin solucionando problema de {self.nombre}:')
            reloj(10)
            print('Berlin: problema solucionado!')