#命令の関数の作成
def print_ab(pstr,a,b): #print命令
    str_list = list(pstr)
    str_list =  str_list[a:b+1]
    pstr = ''.join(str_list)
    return pstr

def reverse_ab(pstr,a,b): #reverse命令
    str_list = list(pstr)
    str_list2 = str_list[a:b+1]
    str_list2 = list(reversed(str_list2))

i_str = input() #文字列strの入力
q_n = int(input()) #命令数

for i in range(q_n):
    q = input().split() #命令の入力