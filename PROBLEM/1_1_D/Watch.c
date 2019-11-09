#include<stdio.h>

int main(){
  /*h:時間,m:分,s:秒
  　Sを入力
  　Sが６０未満のときsは秒だけ
  　Sが３６００未満のとき分と秒
  　Sが３６００以上のとき時間が発生する
  　出力はh:m:sの形式*/
  int S,h,m,s;
  scanf("%d",&S);
  if(S<60){
    printf("0:0:%d\n",S);
  }else if(S>=60 && S<3600){
    m=S/60;
    s=S%60;
    printf("0:%d:%d\n",m,s);
  }else if(S>=3600){
    h=S/3600;
    S=S-h*3600;
    m=S/60;
    s=S%60;
    printf("%d:%d:%d\n",h,m,s);
  }
  return 0;
}
