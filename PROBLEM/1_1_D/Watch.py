S=int(input())

if S<60:
  print("0:0:"+str(S))
elif S>=60 and S<3600:
  m=int(S/60)
  s=int(S%60)
  print("0:"+str(m)+":"+str(s))
elif S>=3600:
 h=int(S/3600)
 S=int(S-h*3600)
 m=int(S/60)
 s=int(S%60)
 print(str(h)+":"+str(m)+":"+str(s))
