class Parent(object):
    
    def __init__(self, blood, lastname):
        self.blood = blood
        self.lastname = lastname

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):

    def __init__(self, blood, lastname, gender):
        super().__init__(blood, lastname)
        self.gender = gender

    def inheritance(self):
        print(f"""
        blood type : {self.blood}
        last name : {self.lastname}
        gender : {self.gender}
        """)

dad = Parent("A", "Kim")
son = Child("A", "Kim", "Male")

dad.implicit()
son.implicit()

son.inheritance()

