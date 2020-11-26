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


