# coding : utf-8

# 오버라이드(override)는 무시하다라는 의미로
# 부모클래스의 메서드를 무시하고 자식클래스에서 
# 새로운 생성자, 메서드를 정의

class Parent(object):   # 부모클래스 선언

    def __init__(self, blood, eye_color, last_name, first_name, age):
        self.blood = blood
        self.eye_color = eye_color
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def showID(self):
        print(f"boold : {self.blood}")
        print(f"eye_color : {self.eye_color}")
        print(f"last name : {self.last_name}")
        print(f"first name : {self.first_name}")
        print(f"age : {self.age}")

    # 중복되는 기능은 부모클래스를 사용
    def greeting(self):
        print("안녕하세요.")


class Son(Parent):    # 키의 정보가 있는 자식클래스 선언
    # 키의 정보를 추가적으로 받아들일 수 있는 생성자 오버라이딩
    def __init__(self, blood, eye_color, last_name, first_name, age, height):
        # super().__init__(부모클래스 생성자의 매개변수)
        # 부모클래스의 생성자를 호출, 인스턴스 변수들이 생성
        super().__init__(blood, eye_color, last_name, first_name, age)
        self.height = height

    def showID(self):
        # super()를 사용
        # 부모클래스의 오버라이딩된 메소드를 호출
        super().showID()
        print(f"저의 키는 {self.height}cm 입니다.")

    def greeting(self):
        super().greeting()  # 부모클래스의 메서드 호출, 중복 줄임
        print("저를 소개합니다.")


class Daughter(Parent):     # 음식의 정보가 있는 자식클래스 선언
    # 음식의 정보를 추가적으로 받아들일 수 있는 생성자 오버라이딩
    def __init__(self, blood, eye_color, last_name, first_name, age, food):
        # super().__init__(부모클래스 생성자의 매개변수)
        # 부모클래스의 생성자를 호출, 인스턴스 변수들이 생성
        super().__init__(blood, eye_color, last_name, first_name, age)
        self.food = food

    def showID(self):
        # super()를 이용
        # 부모클래스의 오버라이딩된 메소드를 호출
        super().showID()
        print(f"제가 좋아하는 음식은 {self.food}입니다.")

    def greeting(self):
        super().greeting()  # 부모클래스의 메소드 호출, 중복 줄임
        print("저를 소개해드리겠습니다.")



son = Son("O", "Black", "Kim", "Kyukyu", 30, 180)
son.greeting()
son.showID()

daughter = Daughter("A", "DarkBrown", "Kim", "Kyujin", 30, "Pizza")
daughter.greeting()
daughter.showID()

# Son과 Daughter의 greeting에서 super().greeting()으로 Parent의 greeting을 호출
# 중복되는 기능은 자식 클래스에서 또 만들필요 없음
# 부모 클래스의 기능을 사용
# 메서드 오버라이딩은 기능을 유지하면서 새로운 기능을 추가할 때 사용





