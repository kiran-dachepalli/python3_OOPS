class Car(object):
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        if self._max_speed <0:
            raise ValueError('Invalid value for max_speed')
        self._acceleration=acceleration
        if self._acceleration <0:
            raise ValueError('Invalid value for acceleration')
        self._tyre_friction=tyre_friction
        if self._tyre_friction <0:
            raise ValueError('Invalid value for tyre_friction')
        self._is_engine_started=False
        self._current_speed=0
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def current_speed(self):
        return self._current_speed
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    
    def start_engine(self):
        self._is_engine_started=True
    
    def stop_engine(self):
        self._is_engine_started = False
        
    def accelerate(self):
        if self.is_engine_started == True:
            if self._current_speed+self.acceleration >= self.max_speed:
                self._current_speed = self.max_speed
            else:
                self._current_speed += self.acceleration
        else:
            print('Start the engine to accelerate')
        
    def apply_brakes(self):
        if self._current_speed-self.tyre_friction >= 0:
            self._current_speed -= self.tyre_friction
        else:
            self._current_speed = 0
            
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Beep Beep')
        else:
           print('Start the engine to sound_horn')
           
