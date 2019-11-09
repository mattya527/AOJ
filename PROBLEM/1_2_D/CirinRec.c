#include<stdio.h>

int main(){
  int W,H,x,y,r,f=0;
  scanf("%d%d%d%d%d",&W,&H,&x,&y,&r);
  if(x+r>W) f=1;
  if(y+r>H) f=1;
  if(r>x) f=1;
  if(r>y) f=1;
  if(f==0) printf("Yes\n");
  else printf("No\n");
  return 0;
}
