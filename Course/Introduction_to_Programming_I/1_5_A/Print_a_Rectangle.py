while  True:
    a,b = map(int,input().split())
    if a==0 and b ==0: break
    for i in range(a):
        for j in range(b):
            print(r"#",end="")
        print()
    print("")
