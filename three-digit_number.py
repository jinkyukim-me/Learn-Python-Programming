# # 변수 num을 선언하고, 숫자형으로 입력을 받습니다.
# num = int(input())

# # if-elif-else문을 이용해서 조건에 따라 출력합니다.
# # 왼쪽에 있는 조건에 따라 자리수를 출력해봅시다.
# if num <=9:
#     print("한 자리 숫자입니다.")
# elif num <=99:
#     print("두 자리 숫자입니다.")
# else: #num = 100~999
#     print("세 자리 숫자입니다.")

try:
    num_input = input("1~999까지의 숫자 중 하나를 입력해주세요 : ")
    num_int = int(num_input)
    try:
        if 1 <= num_int <= 10:
            print("한 자리 숫자입니다.")
        elif 10 <= num_int <= 99:
            print("두 자리 숫자입니다.")
        elif 100 <= num_int <= 999:
            print("세 자리 숫자입니다.")
        else:
            raise Exception
    except:
        print("숫자가 범위를 벗어났습니다.")   
except:
    # print("'%s'는 숫자가 아닙니다. 숫자를 입력해주세요." % num_input)
    # print("'{}'는 숫자가 아닙니다. 숫자를 입력해주세요.".format(num_input))
    print(f"'{num_input}'는 숫자가 아닙니다. 숫자를 입력해주세요.")



num = int(input("1~999까지의 숫자 중 하나를 입력해주세요 : "))
if 1 <= num <= 10:
    print("한 자리 숫자입니다.")
elif 10 <= num <= 99:
    print("두 자리 숫자입니다.")
elif 100 <= num <= 999:
    print("세 자리 숫자입니다.")
else:
    print("숫자가 범위를 벗어났습니다.")



while True:
    try:
        num_input = input("1~999까지의 숫자 중 하나를 입력해주세요 : ")
        num_int = int(num_input)
        try:
            if 1 <= num_int <= 10:
                print("한 자리 숫자입니다.")
                break
            elif 10 <= num_int <= 99:
                print("두 자리 숫자입니다.")
                break
            elif 100 <= num_int <= 999:
                print("세 자리 숫자입니다.")
                break
            else:
                raise Exception
        except:
            print("숫자가 범위를 벗어났습니다.")   
    except:
        # print("'%s'는 숫자가 아닙니다. 숫자를 입력해주세요." % num_input)
        # print("'{}'는 숫자가 아닙니다. 숫자를 입력해주세요.".format(num_input))
        print(f"'{num_input}'는 숫자가 아닙니다. 숫자를 입력해주세요.")
        continue

