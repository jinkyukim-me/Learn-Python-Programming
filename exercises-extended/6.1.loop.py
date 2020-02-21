# while
student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리한다")
    student += 1

# sum100
num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print("sum =", sum)

# sumodd
num = 151
sum = 0
while num <= 300:
    sum += num
    num += 2
print("sum =", sum)

# for
for student in [1, 2, 3, 4, 5]:
    print(student, "번 학생의 성적을 처리한다.")

# forsum
sum = 0
for num in range(1, 101):
    sum += num
print("sum = ", sum)

# forsum2
for num in range(2, 101, 2):
    sum += num
print("sum =", sum)

# iterations
for a in range(5):
    print("이 문장을 반복합니다.")

# ruler
for x in range(1, 51):
    if (x % 10 == 0):
        print('+', end= '')
    else:
        print('-', end= '')
print()

# ruler2
for x in range(1, 51):
    if (x % 10):
        print('-', end= '')
    else:
        print('+', end= '')
print()

# ruler3
for x in range(1, 6):
    print('-' * 9, end='')
    print('+', end= '')
print()

# ruler4
x = 1
while x < 51:
    if (x % 10):
        print('-', end='')
    else:
        print('+', end='')
    x += 1
print()

# ruler5
for x in range(1, 51):
    if (x % 5):
        print('-', end='')
    else:
        print('+', end='')    
print()

# break
score = [92, 86, 68, 120, 56]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print("성적 처리 끝")

# continue
socre = [92, 86, 68, -1, 56]
for s in score:
    if (s == -1):
        continue
    print(s)
print("성적 처리 끝")