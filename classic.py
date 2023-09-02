class staff:
    def __init__(self, name, age, yoe, kpi, gender, email):
        self.name = name
        self.age = age
        self.yoe = yoe
        self.kpi = kpi
        self.gender = gender
        self.email = email
    
    def great_staff(self):
        if self.kpi >= 3.0:
            return True
        else:
            False


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt 
        self.answer = answer
        
class Teacher:
    def counsel(self):
        print("This person can counsel")

    def discipline(self):
        print("This individual can discipline")

    def teach(self):
        print("This person can teach")

    def learner(self):
        print("This person teaches pupils")

class Lecturer(Teacher):
    def learner(self):
        print("This person teaches student")