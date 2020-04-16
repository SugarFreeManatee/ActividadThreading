import os
import sys
from parametros import bomba_nuclear
from cargar_tweets import cargar_tweets
from twitter import Lider_mundial
from DoomsdayClock import Doomsday_Clock

class Simulacion:

    def __init__(self, tweets_pinto, tweets_trumpzini):
        self.doomsday_clock = Doomsday_Clock(0.25, 51)
        self.dr_pinto = Lider_mundial('Dr. Pin Tong-Un', tweets_pinto, 0.25, self.doomsday_clock)
        self.trumpzini = Lider_mundial('Trumpzini',tweets_trumpzini, 0.25, self.doomsday_clock)

    def comenzar(self):
        self.doomsday_clock.start()
        self.dr_pinto.start()
        self.trumpzini.start()
        self.doomsday_clock.join()
        print(bomba_nuclear)
        sys.exit()

if __name__ == "__main__":
    tweets_pinto = cargar_tweets(os.path.join('datos', 'pin_tweets.csv'))
    tweets_trumpzini = cargar_tweets(os.path.join('datos', 'trumpzini_tweets.csv'))

    simulacion = Simulacion(tweets_pinto, tweets_trumpzini)
    simulacion.comenzar()
