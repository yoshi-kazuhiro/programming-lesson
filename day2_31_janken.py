import random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
END = '\033[0m'

f = random.random()
#print(str(f))

i = f * 1000
#print(str(i))

j = int(i)
#print(str(k))

k = j % 3
#print(str(j))

if (k == 2):
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
elif (k == 0):
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
elif (k == 1):
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
