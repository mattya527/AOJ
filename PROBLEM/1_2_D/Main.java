import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int W = scan.nextInt();
    int H = scan.nextInt();
    int x = scan.nextInt();
    int y = scan.nextInt();
    int r = scan.nextInt();
    int f = 0;
    if(x+r>W) f=1;
    if(y+r>H) f=1;
    if(r>x) f=1;
    if(r>y) f=1;
    if(f==0) System.out.println("Yes");
    else System.out.println("No");
  }
}
