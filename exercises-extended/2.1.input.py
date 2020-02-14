# 변수 = input('질문 내용')

age = input("몇 살이세요?")         # input함수로 입력받은 값은 항상 문자열
print(age)

print('=' * 40)

price = input('가격을 입력하세요 : ')
num = input('개수를 입력하세요 : ')
sum = int(price) * int(num)
print('총액은', sum, '원입니다')

print('=' * 40)

# 변수 = int(input('질문 내용'))

price = int(input('가격을 입력하세요 : '))
num = int(input('개수를 입력하세요 : '))
sum = price * num
print('총액은', sum, '원입니다')

print('=' * 40)

name = input('이름을 입력하세요 : ')
print('안녕하세요', name, '님')


