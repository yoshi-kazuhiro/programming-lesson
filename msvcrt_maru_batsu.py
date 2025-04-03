import time
import msvcrt
import random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
END = '\033[0m'
CLR = '\033[2J'
RST = '\033[0;0H'

board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_user = 1
cursor_i = 0
cursor_j = 0

def print_board(): 
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                print("□ ", end="")
            elif board[i][j] == 1:
                print("〇 ", end="")
            elif board[i][j] == 2:
                print("× ", end="")
            else:
                print("？ ", end="")
        print("")

def print_board_index():
    ## 画面クリア
    print(CLR, end="")
    ## カーソルを0行、0桁目へ移動
    print(RST, end="")

    print("ゲームをやめる：q")
    print("O/Xを置く：space")
    
    if (current_user == 1):
        print(RED)
        print("先攻の番です")
    else:
        print(BLUE)
        print("後攻の番です")
    print(END)
    
    for i in range(0, 3):
        for j in range(0, 3):
            if (i == cursor_i and j == cursor_j):
                if (current_user == 1):
                    print(RED, end="")
                else:
                    print(BLUE, end="")
                print("[", end="")
                print(END, end="")
            else:
                print(" ", end="")
            if board[i][j] == 0:
                print(" □ ", end="")
            elif board[i][j] == 1:
                print(RED, end="")
                print(" O ", end="")
                print(END, end="")
            elif board[i][j] == 2:
                print(BLUE, end="")
                print(" X ", end="")
                print(END, end="")
            else:
                print(GREEN, end="")
                print(" ？ ", end="")
                print(END, end="")
            if (i == cursor_i and j == cursor_j):
                if (current_user == 1):
                    print(RED, end="")
                else:
                    print(BLUE, end="")
                print("]", end="")
                print(END, end="")
            else:
                print(" ", end="")
        print("")


def check_input(i, j, v):
    try: 
        I = int(i)
        J = int(j)
        V = int(v)

        if board[I][J] != 0:
            print("すでに置かれています！スキップ！")
            time.sleep(1)
        else:
            board[I][J] = V
    except:
        print("間違った入力です！スキップ！")
        time.sleep(1)

def check_game():
    ## 先攻勝敗チェック
    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or \
        (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or \
        (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or \
        (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or \
        (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or \
        (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or \
        (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or \
        (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1): 
            print(RED)
            print("===先攻の勝ち！===")
            print(END)
            return -1
    ## 後攻勝敗チェック
    if (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2) or \
        (board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2) or \
        (board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2) or \
        (board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2) or \
        (board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2) or \
        (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2) or \
        (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2) or \
        (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2): 
            print(BLUE)
            print("===後攻の勝ち！===")
            print(END)
            return -1
    ## 継続/引き分けチェック
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                count = count + 1
    if count != 0:
        #print("===継続！===")
        pass
    else:
        print(GREEN)
        print("===引き分け！===")
        print(END)
        return -1
    return 0

def getKey():
    global cursor_i
    global cursor_j
    flag = 0
    ## キー入力を受け取る
    key = ord(msvcrt.getch())
    #print("key: " + str(key))
    if key == 113:
        #print("quit")
        flag = -1
    elif key == 72:
        #print("up")
        cursor_i = cursor_i - 1
    elif key == 80:
        #print("down")
        cursor_i = cursor_i + 1
    elif key == 75:
        #print("left")
        cursor_j = cursor_j - 1
    elif key == 77:
        #print("right")
        cursor_j = cursor_j + 1
    elif key == 32:
        #print("space")
        flag = 1
    else:
        flag = 0
    ## カーソルをボード内に収める
    if cursor_i < 0:
        cursor_i= 0
    elif cursor_i >= 3:
        cursor_i = 2
    if cursor_j < 0:
        cursor_j = 0
    elif cursor_j >= 3:
        cursor_j = 2
    ## チェック結果を返す
    return flag


## プログラム開始
print(GREEN)
print("ゲームスタート！")
print(END)
time.sleep(1)
## ボードを表示する
print_board_index()

while True:
    ## キー入力
    flag = getKey()
    if flag == 0 or flag == 1:
        pass
    else:
        break
    ## spaceが入力されたらO/Xを置く
    if flag == 1:
        i = cursor_i
        j = cursor_j
        print("i: " + str(i) + ", j: " +str(j))
        check_input(i, j, current_user)
        if current_user == 1:
            current_user = 2
        else:
            current_user = 1
    ## O/X/カーソルの最新状態を表示する
    print_board_index()
    ## 勝敗をチェックする
    flag = check_game()
    if flag == 0 or flag == 1:
        pass
    else:
        break
