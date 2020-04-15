from threading import Lock
from time import time
from twitter import Lider_mundial
from DoomsdayClock import Doomsday_Clock
import sys
class Simulacion:

    def __init__(self):

        self.doomsday_clock = Doomsday_Clock(0.25, 51)
        self.kim = Lider_mundial('Dr. Pin Tong-Un', 0.25, self.doomsday_clock)
        self.trump = Lider_mundial('Trumpzini', 0.25, self.doomsday_clock)
        


    def comenzar(self):
        self.doomsday_clock.start()
        self.kim.start()
        self.trump.start()
        self.doomsday_clock.join()
        self.kim.kill = True
        self.trump.kill = True
        print('''



                                               

                                 ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                        (/ / //  /|//||||\\  \ \  \ _)
    -------------------------------------------------------------------------------


            ''')
        sys.exit()


if __name__ == '__main__':

    simulacion = Simulacion()
    simulacion.comenzar()
    
    