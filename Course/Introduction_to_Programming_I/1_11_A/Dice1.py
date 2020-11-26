#操作の関数
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
    return(dice)

class Dice():
    def __init__(self):
        self.data1 =0
        self.data2 =0
        self.data3 =0
        self.data4 =0
        self.data5 =0
        self.data6 =0 

dice = Dice()
dice.data1,dice.data2,dice.data3,dice.data4,dice.data5,dice.data6 = map(int,input().split())
# print("{} {} {} {} {} {}".format(dice.data1,dice.data2,dice.data3,dice.data4,dice.data5,dice.data6))
compass = input()
operate(compass,dice)
print("{}".format(dice.data1))
