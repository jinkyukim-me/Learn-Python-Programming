# 점수를 입력받은 후 80점이상이면 합격, 80점 미만이면 불합격 출력
num = int(input("점수입력 [0-100] : "))
if num >= 80:
    print("합격")
else:
    print("불합격")

# 한국의 수도는 어디인지 질문에 대한 대답을 입력받아
# 정답이면 정답이라는 메세지 출력하고 출하한다는 메세지도 같이 출력
# 정답이 아니면 아무것도 하지 않는다
capital = input("한국의 수도는? ")
if capital == "서울":
    print("정답")
    print("축하한다")

# age와 height 변수가 주어졌을 때 8세 이상이고, 키 100 이상인 경우만
# 놀이기구를 탈수 있다는 조건문
age = int(input("나이는? "))
height = int(input("키는? "))
if age >= 8 and height >= 100:
    print("놀이기구를 탈 수 있어요!")
else:
    print("아쉽지만, 놀이기구를 탈 수가 없어요")

# dir 변수에는 '동','서','남','북' 넷 중 하나의 방향 값이 들어감
# 이 변수의 값에 따라 서울에서 각 방향에 있는 도시 하나를 출력하는 프로그램을 작성
# 그 외 값은 에러 처리
dir = input("어떤 방향인가요? [동/서/남/북]")
if dir == "동":
    print("잠실")
elif dir == "서":
    print("목동")
elif dir == "남":
    print("분당")
elif dir == "북":
    print("광화문")
else:
    print("잘못 입력하셨습니다")


# 정수 하나를 입력받아 5의 배수인지 조사하여 결과를 출력
num = int(input("정수를 입력하세요 : "))
if num % 5 == 0:
    print("5의 배수입니다")
else:
    print("5의 배수가 아닙니다")


# 서울우유는 1리터에 2500원 매일우유는 1.8리터에 4200원
# 용량대비 어떤 우유가 더 싼지 계산 및 판단하여 결과를 출력
seoulMilk = 2500 / 1
maeilMilk = 4200 / 1.8
if seoulMilk > maeilMilk:
    print(f"용량대비 서울우유는 {seoulMilk}원이고 매일우유는 {maeilMilk:.1f}원 이니까 서울우유가 비쌈")
else:
    print(f"용량대비 서울우유는 {seoulMilk}원이고 매일우유는 {maeilMilk:.1f}원 이니까 매일우유가 비쌈")


