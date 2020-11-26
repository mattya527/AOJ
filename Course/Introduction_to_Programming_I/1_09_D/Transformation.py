#print命令
def instPrint(word,a,b): #wordのa文字からb文字までを出力
    print('{}'.format(word[a:b+1]))

# instPrint('world',1,3) #ok
def instReverse(word,a,b): #wordのa文字からb文字までを逆順にする
    reword = word[a:b+1]
    reword = reword[::-1]
    listword = list(word)
    listreword = list(reword)
    j = 0
    for i in listreword:
        listword[a+j] = i
        j+=1
    return(''.join(listword))

# print(instReverse('world',1,5)) #ok

def instReplace(word,a,b,p): #wordのa文字からb文字までをpに変える
    listword = list(word)
    listp = list(p)
    j = 0
    for i in listp:
        listword[a+j] = i
        j+=1
    return("".join(listword))

# print(instReplace('world',1,3,'aaa')) #ok

#main
word = input()
q = int(input())
for i in range(q):
    inst = input().split()
    if inst[0] == "print":
        instPrint(word,int(inst[1]),int(inst[2]))
    elif inst[0] == "reverse":
        word = instReverse(word,int(inst[1]),int(inst[2]))
    elif inst[0] == "replace":
        word = instReplace(word,int(inst[1]),int(inst[2]),inst[3])
