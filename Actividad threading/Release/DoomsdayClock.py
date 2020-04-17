from threading import Thread, Lock
from time import sleep


class Doomsday_Clock:

    def __init__(self, speed, time):
        # Completar

        # No modificar
        self._time = time
        self.hora = 60 - self._time

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self,value):
        if value < 1:
            quit()
        self._time = value

    def run(self):
        # Completar o modificar si es necesario
        pass

    def contar(self):
        self.time -= 1
        self.hora += 1
        if self.time < 5:
            print('11:'+str(self.hora))
        elif self.time % 5 == 0:
            print('11:'+str(self.hora))

    def acelerar(self, nombre, enojo):
        # Completar o modificar si es necesario
        pass
