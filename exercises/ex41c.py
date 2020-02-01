import sys
from urllib.request import urlopen
lst = []
url = "https://github.com/jinkyukim-me/Learn-Python-Programming/blob/master/exercises/words.txt"

for word in urlopen(url).readlines():
    lst.append(str(word.strip(), encoding="utf-8"))
    
    #print(word)

if len(sys.argv) == 2 and sys.argv[1] == "english":
    print("Ok")
else:
    print("Bye")

#print(lst)

