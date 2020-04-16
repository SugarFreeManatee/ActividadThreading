from threading import Thread, Lock
from time import sleep
import random

class LiderMundial(Thread):

    def __init__(self, nombre, tweets, enojo, reloj):
        # Completar
        pass

        # No borrar o modificar esto
        random.shuffle(self.tweets)

    @property
    def enojo(self):
        return self._enojo

    @enojo.setter
    def enojo(self,value):
        if value < 1:
            return 1
        self._enojo = value

    def run(self):
        # Completar o modificar si es necesario
        pass

    def twitear(self):
        # Completar o modificar si es necesario
        pass
