class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def afficher_infos(self):
        return f"Nom : {self.name} - Age : {self.age}"
    
        
student1 = Student("Alice", 20)
student2 = Student("Marc", 24)
student3 = Student("Sarah", 19)
# student1.name
# student1.age
print(student1.afficher_infos())
print(student2.afficher_infos())
print(student3.afficher_infos())


# La classe Student est 
# L'objet sutdent1 est une instance de la classe student