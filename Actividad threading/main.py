from threading import Lock
from time import time
from twitter import Lider_mundial
from DoomsdayClock import Doomsday_Clock
import sys
class Simulacion:

    def __init__(self):

        self.kim = Lider_mundial('kim', 2)
        self.trump = Lider_mundial('trump', 3)
        self.doomsday_clock = Doomsday_Clock(1, 31)


    def comenzar(self):
    	self.kim.start()
    	self.trump.start()
    	self.doomsday_clock.start()
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
    
    