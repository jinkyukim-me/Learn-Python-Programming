# if문
age = int(input("나이가 어떻게 되세요?"))
if age < 19:
    print("미성년자는 접근할 수 없습니다.")
if age >= 19:print("성인입니다.")

# 비교연산자
num = int(input("숫자를 입력해주세요 : "))
if num == 3:
    print("3이다")
if num > 5:
    print("5보다 크다")
if num < 5:
    print("5보다 작다")

country = input("둘 중에 하나를 입력하세요(Korea/korea) : ")
if country == "Korea":
    print("한국입니다.")
if country == "korea":
    print("대한민국입니다.")

# a보다는 b가 더 큰 문자, 사전의 뒤쪽에 나오는 문자열을 더 큰 것으로 평가
if ("korea" > "japan"):
    print("한국이 더 크다")
if ("korea" < "japan"):
    print("일본이 더 크다")
if ("Korea" < "japan"):
    print("대소문자의 비교 - 소문자")
if ("Korea" > "japan"):
    print("대소문자의 비교 - 대문자")

# 조건문에 비교 연산식 대신 변수를 바로 사용
# 변수 자체가 논리식이 됨
# 숫자 - 참(0이 아닌 숫자) - 거짓(0)
# 문자열 - 참(비어 있지 않은 상태) - 거짓("")
# 리스트, 튜플, 딕셔너리 - 참(비어 있지 않은 상태) - 거짓(빈 상태)

# 변수자체를 논리식에 사용하면 0만 아니면 모두 참
# 1, 2, -1도 참

input_num = int(input("숫자를 적어주세요 : "))
if input_num: # if input_num != 0: 비교 연산식을 적는 것이 명확
    print("True")
else:
    print("False")

input_string = input("문자를 입력하세요 : ")
if input_string:
    print("입력해주셔서 감사합니다.")
else:
    print("아무것도 입력하지 않으셨네요.")

# 논리 연산자
# and 두 조건이 모두 참
# or 두 조건 중 하나라도 참
# nor 조건을 반대로 뒤집는다

a = 3
b = 5
if a == 3 and b == 4:
    print("and is OK")
if a == 3 or b == 4:
    print("or is OK")

a = 7
if a > 5 and a < 10:
    print("range is OK")
if 5 < a < 10:
    print("range is OK!")



    




