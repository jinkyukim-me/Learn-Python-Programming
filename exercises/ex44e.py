class Other(object):

    def override(self):                         # override() 메소드
        print("OTHER override()")

    def implicit(self):                         # implicit() 메소드
        print("OTHER implicit()")

    def altered(self):                          # altered() 메소드
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):                         # implicit() 메소드
        self.other.implicit()

    def override(self):                         # override() 메소드
        print("CHILD override()")

    def altered(self):                          # altered() 메소드
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

