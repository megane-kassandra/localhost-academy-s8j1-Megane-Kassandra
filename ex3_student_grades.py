class Student:
    
    def __init__(self,name):
        self.name = name
        self.grades = []
        
    def add_grade(self, grade):
        if grade < 0 or grade > 20 :
            print("Note invalide")
        else:
            self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            print("La liste de note est vide")
        else:
            sum = 0
            for grade in self.grades:
                sum += grade
                average = sum / len(self.grades)
            return average

student = Student("Samuel")

# student.add_grade(25)
# student.add_grade(-5)

student.add_grade(14)
student.add_grade(18)
student.add_grade(12)

print(student.grades)
print(f"Moyenne : {student.get_average():.2f}")