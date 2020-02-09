class Parent(object):
    """A simple example class"""                # 클래스 정의 시작부분에 """...""" 도큐먼트 스트링

    def __init__(self):                         # 컨스트럭터 (생성자)
        self.name = "Kim"

    def override(self):                         # override() 메소드
        print("PARENT override()")

    def implicit(self):                         # implicit() 메소드
        print("PARENT implicit()")

    def altered(self):                          # altered() 메소드
        print("PARENT altered()")


class Child(Parent):

    def __init__(self):                         # 자식클래스 생성자
        super().__init__()                      # 부모클래스 생성자
        self.blood = "O"                        # blood 추가

    def override(self):
        print("CHILD override()")               # override() 메소드

    def altered(self):                          # altered() 메소드
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()            # super(자식클래스, self)로 부모클래스의 메서드 호출
        print("CHILD, AFTER PARENT altered()")


dad = Parent()                                  # 클래스의 인스턴스 생성
son = Child()                                   # 클래스의 인스턴스 생성

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

