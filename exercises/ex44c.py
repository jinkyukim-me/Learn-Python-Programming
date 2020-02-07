# coding : utf-8

# 클래스 class
# 인스턴스 instance
# 메서드 method
# 속성 attribute

class Parent(object):   # 부모클래스 선언

    def altered(self):
        print("PARENT altered()")


class Child(Parent):    # 부모클래스를 상속받는 자식클래스 선언

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(child, self).altered()
        print("CHILD, AFTER PARENT altered()")


# 인스턴스 = 클래스()
# 클래스는 특정 개념 표현
# 클래스를 사용하려면 인스턴스 생성

dad = Parent()  
# dad는 Parent의 인스턴스(instance)

son = Child()
# son은 Child의 인스턴스(instance)

# 메서드 호출
# 인스턴스.메서드()
dad.altered()
son.altered()

