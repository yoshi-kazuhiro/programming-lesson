import random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
END = '\033[0m'

f = random.random()
#print(str(f))

i = f * 1000
#print(str(i))

j = i % 3
#print(str(j))

k = int(j)
#print(str(k))

if (k == 0):
    print(RED)
    print("パー")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print("□ □ □ □ □ ■ □ □ □ □ □ ")
    print("□ □ □ ■ □ ■ □ ■ □ □ □ ")
    print("□ □ □ ■ □ ■ □ ■ □ □ □ ")
    print("□ □ □ ■ □ ■ □ ■ □ ■ □ ")
    print("■ □ □ ■ □ ■ □ ■ □ ■ □ ")
    print("□ ■ □ ■ □ ■ □ ■ □ ■ □ ")
    print("□ ■ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print(END)
elif (k == 1):
    print(GREEN)
    print("グー")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print("□ □ □ ■ □ ■ □ ■ □ □ □ ")
    print("□ ■ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ ■ □ ■ □ ■ □ ■ □ ■ □ ")
    print("□ □ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print(END)
elif (k == 2):
    print(BLUE)
    print("チョキ")
    print("□ □ ■ □ □ ■ □ □ □ □ □ ")
    print("□ □ ■ □ □ ■ □ □ □ □ □ ")
    print("□ □ ■ □ □ ■ □ □ □ □ □ ")
    print("□ □ ■ □ ■ □ □ □ □ □ □ ")
    print("□ □ □ ■ □ ■ □ ■ □ □ □ ")
    print("□ ■ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ ■ □ ■ □ ■ □ ■ □ ■ □ ")
    print("□ □ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ ■ ■ ■ ■ ■ ■ ■ □ □ ")
    print("□ □ □ □ □ □ □ □ □ □ □ ")
    print(END)
