class Car:
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


class Truck(Car):
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=100):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self.inital_load=0
       # self._is_engine_started=False
        if self._max_cargo_weight <0:
            raise ValueError('Invalid value for Max_cargo_weight')
        
    @property   
    def max_cargo_weight(self):
        return self._max_cargo_weight 
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    def sound_horn(self):
        if self._is_engine_started==True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
    
    def load(self,weight):
        if weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        else:
            if (self._is_engine_started == False or self._is_engine_started==True) and self._current_speed == 0 and (self.inital_load+weight <= self._max_cargo_weight) :
                self.inital_load+=weight
        
            elif self.inital_load + weight > self._max_cargo_weight:
                print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))
        
            elif self._is_engine_started==True and self._current_speed!=0:
                print('Cannot load cargo during motion')
    
            elif self._is_engine_started==False  and self._current_speed!=0:
                print('Cannot load cargo during motion')
                
            else:
                self.inital_load += weight
                
    def unload(self,weight):
        if weight <0:
            raise ValueError('Invalid value for cargo_weight')
        else:    
            if (self._is_engine_started == False or self.is_engine_started==True) and self._current_speed == 0:
                self.inital_load-=weight
            elif self._is_engine_started==True:
                print('Cannot unload cargo during motion')
