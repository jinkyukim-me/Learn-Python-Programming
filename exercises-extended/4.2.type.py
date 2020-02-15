# 문자열 연산

s1 = "대한민국"
s2 = "만세"
print(s1 + s2)
print(s1 * 5)

# 정수와 문자열
try:
    print("korea" + 2002) # 에러
except:
    print("Error")
print("korea" + str(2002)) # korea2002

try:
    print(10 + "22")
except:
    print("Error")
print(10 + int("22"))
print('=' * 40)

# int함수의 두 번재 인수로 진법을 지정
print(int("1a", 16))
print(int("15", 8))

# 실수의 변환
print(10 + float("22.5"))
print(10 + float("314e-2"))
print(10 + int(22.5))
print(10 + int(float("22.5"))) # int("22.5")는 에러
# 문자열에 저장된 실수를 정수로 바꿀 때는
# 일단 float함수로 문자열을 실수로 바꾸고
# 다시 int함수를 사용하여 정수로 바꾼다
print('=' * 40)

print(int(2.54))
print(round(2.54))
print(round(2.5))
print(round(3.5))
print(round(2.54214, 1))
print(round(2.54214, 2))
print(round(123456, -3))
print(round(123456, -1))
print(round(123456, -2))



