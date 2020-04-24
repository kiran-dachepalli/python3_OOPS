class Animals:
    animal_sound_making=None
    food_to_animal=0
    def __init__(self,age_in_months=1,breed=None,required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
        if self._age_in_months !=1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        if self._required_food_in_kgs <=0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
            
    @property    
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property    
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod    
    def make_sound(cls):
        print(cls.animal_sound_making)
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.food_to_animal
        
class WaterAnimals:
    animals_breath=None
    def __init__(self):
        pass
    @classmethod
    def breathe(cls):
        print(cls.animals_breath)
        
class LandAnimals:
    animals_breath=None
    def __init__(self):
        pass
    @classmethod
    def breathe(cls):
        print(cls.animals_breath)
        

class Hunting:
    hunt_animal=''
    def hunt(self,zoo_animals):
        count=0
        for animal in zoo_animals.add_animals_list:
            if type(animal).__name__== self.hunt_animal[0]:
                zoo_animals.add_animals_list.remove(animal)
                count+=1
                break
        if count==0:
            print(f'No {self.hunt_animal[1]} to hunt')
                
 
class Deer(Animals,LandAnimals):
    animal_sound_making='Buck Buck'
    food_to_animal=2
    animals_breath='Breathe in air'
    
class Lion(Animals,LandAnimals,Hunting):
    animal_sound_making='Roar Roar'
    food_to_animal=4
    animals_breath='Breathe in air'
    hunt_animal=['Deer','deers']
    
class Shark(Animals,WaterAnimals,Hunting):
    animal_sound_making='Shark Sound'
    food_to_animal=8
    animals_breath='Breathe oxygen from water'
    hunt_animal=['GoldFish','GoldFish']
    
class GoldFish(Animals,WaterAnimals):
    animal_sound_making='Hum Hum'
    food_to_animal=0.2
    animals_breath='Breathe oxygen from water'
    
class Snake(Animals,LandAnimals,Hunting):
    animal_sound_making='Hiss Hiss'
    food_to_animal=0.5
    animals_breath='Breathe in air'
    hunt_animal=['Deer','deers']
    
class Zoo:
    all_animals_list=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.add_animals_list=[]
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,other):
        self.add_animals_list.append(other)
        Zoo.all_animals_list.append(other)
        
    def feed(self,animal):
        if self._reserved_food_in_kgs==0:
            return
        else:
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
        
        animal.grow()
        return self._reserved_food_in_kgs
        
    def count_animals(self):
        return len(self.add_animals_list)
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.all_animals_list)
        
    @staticmethod
    def count_animals_in_given_zoos(animal_object):
        count=0
        for i in animal_object:
            count+=i.count_animals()
        return count
        
""" 
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
print(deer.age_in_months)
print(deer.required_food_in_kgs)
deer.breathe()
deer.grow()
print(deer.age_in_months)
print(deer.required_food_in_kgs)
"""

#Zoo.count_animals_in_given_zoos([zoo])
