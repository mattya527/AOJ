#右の面を求める関数
def right_surface(dice,top,front):
    if top == dice.data1:
        if front == dice.data2:
            print(dice.data3)
        elif front ==dice.data3:
            print(dice.data5)
        elif front == dice.data5:
            print(dice.data4)
        else:
            print(dice.data2)
    elif top == dice.data2:
        if front == dice.data6:
            print(dice.data3)
        elif front == dice.data3:
            print(dice.data1)
        elif front == dice.data1:
            print(dice.data4)
        else:
            print(dice.data6)
    elif top == dice.data3:
        if front == dice.data6:
            print(dice.data5)
        elif front == dice.data5:
            print(dice.data1)
        elif front == dice.data1:
            print(dice.data2)
        else:
            print(dice.data6)
    elif top == dice.data4:
        if front == dice.data6:
            print(dice.data2)
        elif front == dice.data2:
            print(dice.data1)
        elif front == dice.data1:
            print(dice.data5)
        else:
            print(dice.data6)
    elif top == dice.data5:
        if front == dice.data1:
            print(dice.data3)
        elif front == dice.data3:
            print(dice.data6)
        elif front == dice.data6:
            print(dice.data4)
        else:
            print(dice.data1)
    else:
        if front == dice.data2:
            print(dice.data4)
        elif front == dice.data4:
            print(dice.data5)
        elif front == dice.data5:
            print(dice.data3)
        else:
            print(dice.data2)

class Dice():
    def __init__(self):
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0
        self.data4 = 0
        self.data5 = 0
        self.data6 = 0

dice = Dice()
dice.data1, dice.data2, dice.data3, dice.data4, dice.data5, dice.data6 = map(int, input().split())

q = int(input())
for i in range(q):
    top, front = map(int,input().split())
    right_surface(dice,top,front)
