from threading import Thread, Lock
from time import sleep


class Lider_mundial(Thread):

    twitear_lock = Lock()


    def __init__(self, nombre, enojo,):
        super(Lider_mundial,self).__init__()
        self.daemon = True
        self.nombre = nombre
        self._enojo = enojo
        self.kill = False
        print(self.nombre)
    @property
    def enojo(self):
        return self._enojo
    @enojo.setter
    def enojo(self,value):
        if value < 1:
            return 1
        self._enojo = value
    
    def run(self):
        while self.kill == False:
            sleep(self.enojo)
            self.twitear()
    def twitear(self):
        with self.twitear_lock:
                print(self.nombre) 
                self.enojo -= 1
    def kill(self):
        self.kill = True