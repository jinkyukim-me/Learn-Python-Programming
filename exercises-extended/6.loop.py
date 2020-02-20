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

