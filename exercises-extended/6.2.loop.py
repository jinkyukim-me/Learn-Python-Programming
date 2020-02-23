# 이중 루프

# gugudan
for dan in range(2, 10):
    print(dan, '단')
    for hang in range(2, 10):
        print(dan, '*', hang, '=', dan * hang)
    print()

# gugudanwhile
dan = 2
while dan <= 9:
    hang = 2
    print(dan, '단')
    while hang <= 9:
        print(dan, "*", hang, '=', dan * hang)
        hang += 1
    dan += 1
    print()

