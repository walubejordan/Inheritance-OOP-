class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
#display info
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

#Inheretance 1
class Student(Person):
    def __init__(self, name, age, accessNumber):
        super().__init__(name, age)
        self.accessNumber = accessNumber
    
    def display_info(self):
        super().display_info()
        print(f"Access Number: {self.accessNumber}")
        
Student = Student("Jordan", 20, "B24795")
Student.display_info()

#Inheretance 2 
class Staff(Student):
    def __init__(Self, name, age, staffId):
        super().__init__(name,age)
        Self.staffId = staffId
    
    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staffId}")

Staff = Staff("Simon", 30, 25791)
Staff.display_info()