from threading import Thread, Lock
from time import sleep


class Doomsday_Clock(Thread):

    doomsday_lock = Lock()


    def __init__(self, speed, time):
        super(Doomsday_Clock,self).__init__()
        self.speed = speed
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
        while self.time > 0:
            sleep(1/(self.speed))
            self.contar()
    def contar(self):
            self.time -= 1
            self.hora += 1
            if self.time < 5:
                print('11:'+str(self.hora))
            elif self.time % 5 == 0:
                print('11:'+str(self.hora))
    def acelerar(self, nombre, enojo):
        with self.doomsday_lock:
            self.speed += enojo/10
            print(f'{nombre} ha acelerado el reloj por {enojo}.')