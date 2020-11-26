import sys

cnt = {}

for line in sys.stdin:
  for l in line:
    if l.isalpha():
      c = l.lower()
      cnt[c] = cnt.get(c,0)+1

for i in range(26):
  c = chr(ord('a')+i)
  print( c, " : ", cnt.get(c,0), sep = '' )
