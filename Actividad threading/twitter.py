from threading import Thread, Lock
from time import sleep
from tweets import tweet_dict
import random

class Lider_mundial(Thread):

    twitear_lock = Lock()


    def __init__(self, nombre, enojo, reloj):
        super(Lider_mundial,self).__init__()
        self.daemon = True
        self.nombre = nombre
        self._enojo = enojo
        self.reloj = reloj
        self.tweets = tweet_dict[self.nombre]
        self.kill = False
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
        while self.kill == False:
            sleep(1/self.enojo)
            self.twitear()
    def twitear(self):
        with self.twitear_lock:
                tweet = self.tweets.pop()
                print(f'{self.nombre}: {tweet[1]}')
                self.reloj.acelerar(self.nombre, int(tweet[0]))
                self.enojo += int(tweet[0])
                sleep(1)