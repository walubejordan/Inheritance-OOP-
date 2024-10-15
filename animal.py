class Animal:
    def __init__(self, name):
        self.name =name
        
    def make_sound(self):
        print(f"{self.name} cries")
        
    def make_sound(self):
        super().display_info()
        print(f"self.sound")
        
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def make_sound(self):
        super().display_info()
        print(f"self.sound")
        
            
class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
        
    def make_sound(self):
        super().display_info()
        print(f"self.sound")