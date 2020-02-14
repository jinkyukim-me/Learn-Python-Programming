# 변수의 타입 대입되는 값에 의해 결정됨

score = 87
print(score)

print('=' * 40)

score = 98
print(score)

print('=' * 40)

score = 55
print(score)

print('=' * 40)

# 실행 중에 변수의 타입을 바꿀 수 있는 특성 - 동적타입(Dynamic Typing)
score = 'high'
print(score)

print('=' * 40)

a = 1234
print(type(a))
a = 'string'
print(type(a))

print('=' * 40)

a = 1234
print(a)
del a
print(a)

