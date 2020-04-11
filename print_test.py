# print("50" + "50")
# print(4 + 5)
# print("50", "50")
# print("50""50")


# a = 1 / 3
# print(f"fefe",a)


# print("숫자 : {:0.2f}".format(a))
# print(f"숫자 : {a:0.5f}")


name = 'decimal number'
num = 1234.567898765
print(name, 'is', num) 
# print(name + 'is' + num) <- 하나는 문자열이고, 다른 하나는 실수형이기 때문에 '+'는 사용할 수 없습니다.
print('%s is %d' % (name, num)) #%s
print('%s is %f'% (name, num))
print('{} is {:2.3f}'.format(name, num))
print(f'{name} is {num:0.3f}')

'''
%s : 문자열(string)
%d : 정수(Integer)
%f : 부동소수(floating point real number)
만약 포맷팅하고자 하는 데이터 타입이 다르면, 에러를 표시하게 됩니다.
'''
