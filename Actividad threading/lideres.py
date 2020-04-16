from threading import Thread, Lock
from time import sleep
import random

class LiderMundial(Thread):

    twitear_lock = Lock()

    def __init__(self, nombre, tweets, enojo, reloj):
        super().__init__()
        self.daemon = True
        self.nombre = nombre
        self._enojo = enojo
        self.reloj = reloj
        self.tweets = tweets
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
            print(f'{self.nombre}: {tweet.texto}')
            self.reloj.acelerar(self.nombre, tweet.enojo)
            self.enojo += tweet.enojo
            sleep(1)
