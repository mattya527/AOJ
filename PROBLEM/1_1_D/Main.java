import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in) ;
    int S = scan.nextInt();
    if(S<60){
      System.out.println("0:0:"+ S);
    }else if(S>=60 && S<3600){
      int m = S/60;
      int s = S%60;
      System.out.println ("0:"+m+":"+s);
    }else if(S>=3600){
      int h = S/3600;
      S = S-h*3600;
      int m = S/60;
      int s = S%60;
      System.out.println(h+":"+m+":"+s);
    }
  }
}
