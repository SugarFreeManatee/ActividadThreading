from threading import Thread, Lock
from time import sleep


class Doomsday_Clock(Thread):

    doomsday_lock = Lock()


    def __init__(self, speed, time):
        super(Doomsday_Clock,self).__init__()
        self.speed = speed
        self._time = time
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
            self.speed +=0.25
            if self.time < 5:
                print(self.time)
            elif self.time % 5 == 0:
                print(self.time)