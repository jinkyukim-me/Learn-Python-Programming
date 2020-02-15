# 문자열

print("Welcome to Korea")
words = "Korea 서울 12345"
print(words)
print('I say "Hello" to you')
print('=' * 40)

# 확장열 escape sequece
# \n \t \" \' \\
print("Apple\nBanana\tOrange\"Tangerine\'Grape\\")
print("c:\temp\test.txt")
print("c:\\temp\\test.txt")
print(r"c:\temp\test.txt") # r접두가 있으면 문자열 내의 확장열을 적용하지 않고 있는 그대로(raw)
# 파일의 경로 문자열을 표기할 떄는 이 방법이 편리
print('=' * 40)

# 긴 문자열
s1 = '''파이썬은 네덜란드의 귀도 반 로섬(Guido van Rossum)이 
1989년 크리스마스에 취미 삼아 만들기 시작하여 1991년 2월에
발표했다. 파이썬의 이름은 그 당시 즐겨 보던 코미디 쇼에서
즉흥적으로 따온 것이다.'''
s2 = """신화 속의 비단뱁이라는 뜻이며, 그래서 파이썬의 아이콘으로
    흔히 뱀을 사용한다. 결국 파이썬이라는 이름 자체에는 별다른 뜻이
없는 셈이다."""
print(s1)
print(s2)
print('=' * 40)

# 행 끝에 \를 붙이면 다음 줄까지 하나로 합쳐짐
s1 = '''파이썬은 네덜란드의 귀도 반 로섬(Guido van Rossum)이 \
1989년 크리스마스에 취미 삼아 만들기 시작하여 1991년 2월에 \
발표했다. 파이썬의 이름은 그 당시 즐겨 보던 코미디 쇼에서
즉흥적으로 따온 것이다.'''
print(s1)
# 코드가 길어진다면 행 끝에 \를 둠
totalsec = 365 * 24 * \
        60 * 60
print(totalsec)
print('=' * 40)

s = "korea" "japan" "2020"
print(s)
s = ("korea"
    "japan"
    "2002")
print(s)

# 문자는 내부적으로 문자 코드에 저장됨
# ord함수는 문자의 코드를 조사하고 chr함수는 코드로부터 문자를 구함
print(ord('a'))
print(chr(97))
for c in range(ord('A'), ord('Z') + 1):
    print(chr(c), end='')
print()
print('=' * 40)


    
