# 블록 구조
# 한꺼번에 실행되는 명령의 묶음 - 블록

age = 16
if age < 19:
    print("미성년자는")
    print("출입 금지입니다.")

age = 22
if age < 19:
    print("미성년자는")
print("출입 금지입니다.")

'''
에외처리 되지 않는 에러
try:
    if age > 19:
        print("a")
            print("b")
except Exception as ex:
    print("에러가 발생 했습니다.", ex)
'''

age = 22
if age < 19:
    print("출입 금지")
else:
    print("접근 허가")



# if 조건이 만족하지 않을 때 elif문의 다른 세부 조건을 점검
age = 23
if age < 19:
    print("출입 금지")
elif age < 25:
    print("대학생입니다.")
else:
    print("접근 허가")

# 위의 코드는 다음과 같음
age = 23
if age < 19:
    print("출입 금지")
else:
    if age < 25:
        print("대학생이니다.")
    else:
        print("접근 허가")

# 조건을 위에서 부터 차례대로 점검함
input_money = int(input("얼마있어?"))
if input_money >= 20000:
    print("탕수육을 먹는다")
elif input_money >= 10000:
    print("쟁반 짜장을 먹는다")
elif input_money >= 4000:
    print("짬뽕을 먹는다")
elif input_money >= 6000:
    print("짜장면을 먹는다")
else:
    print("편의점을 간다")

# 조건을 위에서 부터 점점하면서 내려오기 때문에 
# 대소에 따른 조건을 사용할때는 크기에 주의해야함



# if문 중첩
# 똑같은 종류의 명령끼리 겹치는 현상을 중첩(Nesting)
man = True
age = 22
if man == True:
    if age >= 19:
        print("성인 남자입니다.")



