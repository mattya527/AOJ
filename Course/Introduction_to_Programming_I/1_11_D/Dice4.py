#回転
def operate(compass,dice):
    compass = list(compass)
    for way in compass:
        if way == 'W':
            temp = dice.data1
            dice.data1 = dice.data3
            dice.data3 = dice.data6
            dice.data6 = dice.data4
            dice.data4 = temp
        elif way=='N':
            temp = dice.data1
            dice.data1 = dice.data2
            dice.data2 = dice.data6
            dice.data6 = dice.data5
            dice.data5 = temp
        elif way == 'E':
            temp = dice.data1
            dice.data1 = dice.data4
            dice.data4 = dice.data6
            dice.data6 = dice.data3
            dice.data3 = temp
        else:
            temp = dice.data1
            dice.data1 = dice.data5
            dice.data5 = dice.data6
            dice.data6 = dice.data2
            dice.data2 = temp

#2つのdiceが同じものかどうか判定する関数
def CheckDice(dice1,dice2):
    for i in range(6):
        if i < 4:
            for j in range(4):
                if dice1.data1==dice2.data1 and dice1.data2==dice2.data2 and dice1.data3==dice2.data3 and dice1.data4==dice2.data4 and dice1.data5 ==dice2.data5 and dice1.data6==dice2.data6:
                    # print("No")
                    return 1
                else:
                    #W方向に回転
                    operate('W',dice2)
            #N方向に回転
            operate('N',dice2)
        elif i == 4:
            temp = dice2.data2
            dice2.data2 = dice2.data3
            dice2.data3 = dice2.data5
            dice2.data5 = dice2.data4
            dice2.data4 = temp
            for j in range(4):
                if dice1.data1==dice2.data1 and dice1.data2==dice2.data2 and dice1.data3==dice2.data3 and dice1.data4==dice2.data4 and dice1.data5 ==dice2.data5 and dice1.data6==dice2.data6:
                        # print("No")
                        return 1
                else:
                     operate('W',dice2)
            # operate('W', dice2)
        else:
            operate('N', dice2)
            operate('N', dice2)
            for j in range(4):
                if dice1.data1 == dice2.data1 and dice1.data2 == dice2.data2 and dice1.data3 == dice2.data3 and dice1.data4 == dice2.data4 and dice1.data5 == dice2.data5 and dice1.data6 == dice2.data6:
                    # print("No")
                    return 1
                else:
                    operate('W', dice2)
            
    # print("No")
    return 0 

class Dice():
    def __init__(self):
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0
        self.data4 = 0
        self.data5 = 0
        self.data6 = 0

n = int(input())
dice = {}
for i in range(n):
    dice[i] = Dice()
    dice[i].data1, dice[i].data2, dice[i].data3, dice[i].data4, dice[i].data5, dice[i].data6 = map(
    int, input().split())

for i in range(0,n-1):
    for j in range(i+1,n):
        flag = CheckDice(dice[i],dice[j])
        # print("{} {} {}".format(i,j,flag))
        if flag == 1:
            print("No")
            break

    if flag == 1:
        break
if flag == 0:
    print("Yes")

