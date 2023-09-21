class Student():
    def __init__(self, name="None", age=18, iq=60, fakultet="None", fsubject="None", softskill="None"):
        self.name = name
        self.age = age
        self.iq = iq
        self.fakultet = fakultet
        self.fsubject = fsubject
        self.softskill = softskill
        print(name, age, iq, fakultet, fsubject, softskill)

    def changeage(self, age):
        self.age = age

    def change(self, WannaChange, Whatchange):
        if Whatchange == "name":
            self.name = WannaChange
        elif Whatchange == "age":
            self.age = WannaChange
        elif Whatchange == "iq":
            self.iq = WannaChange
        elif Whatchange == "fakultet":
            self.fakultet = WannaChange
        elif Whatchange == "fsubject":
            self.fsubject = WannaChange
        elif Whatchange == "softskill":
            self.softskill = WannaChange
        else:
            print("Error with (PrintSome)")

    def printsomething(self, Whatprint):
        if Whatprint == "name":
            print("Name is " + self.name)
        elif Whatprint == "age":
            print("Age is " + str(self.age))
        elif Whatprint == "iq":
            print("IQ is " + str(self.iq))
        elif Whatprint == "fakultet":
            print("Fakultet is " + self.fakultet)
        elif Whatprint == "fsubject":
            print("Fsubject is " + self.fsubject)
        elif Whatprint == "softskill":
            print("Softskill is " + self.softskill)

class Group():
    def __init__(self, group):
        self.group = group
        self.students = []
    def addStudent (self, student): 
        self.students.append(student)
    def printall(self):
        if self.students != []: 
            print(f"Group {self.group} students:")
            for students in self.students:
                print(students.name)


Oleh = Student("Oleh", 19, 100, "Pryrodnycji", "Biologia", "DoAll")
Margaryta = Student("Margaryta", 18, 90, "Pryrodnycji", "Geografia", "Work in team")
Oleh.printsomething("name")
Group1 = Group("Groupy SS15")
Group1.addStudent(Oleh)
Group1.addStudent(Margaryta)
Group1c.printall()