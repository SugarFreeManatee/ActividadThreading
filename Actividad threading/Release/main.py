import os
import sys
from parametros import bomba_nuclear
from cargar_tweets import cargar_tweets
from lideres import LiderMundial
from DoomsdayClock import Doomsday_Clock

class Simulacion:

    def __init__(self, tweets_pinto, tweets_trumpzini):
        self.doomsday_clock = Doomsday_Clock(0.25, 51)
        self.dr_pinto = LiderMundial('Dr. Pin Tong-Un', tweets_pinto, 0.25, self.doomsday_clock)
        self.trumpzini = LiderMundial('Trumpzini',tweets_trumpzini, 0.25, self.doomsday_clock)

    def comenzar(self):
        # Completar
        pass





if __name__ == "__main__":
    # No modificar
    
    tweets_pinto = cargar_tweets(os.path.join('datos', 'pin_tweets.csv'))
    tweets_trumpzini = cargar_tweets(os.path.join('datos', 'trumpzini_tweets.csv'))

    simulacion = Simulacion(tweets_pinto, tweets_trumpzini)
    simulacion.comenzar()

    print(bomba_nuclear)
    sys.exit()
