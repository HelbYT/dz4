class Student():
    def init(self, name="None", age=18, iq=60, fakultet="None", fsubject="None", softskill="None"):
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

Oleh = Student("Oleh", 19, 100, "Pryrodnycji", "Biologia", "DoAll")
Oleh.printsomething("name")