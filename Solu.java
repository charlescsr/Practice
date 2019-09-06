import java.util.*;
public class Solu {

    public static void main(String[] args) {
        int t;
        Scanner scan=new Scanner(System.in);
        List<String> l=new ArrayList<>();
        List<String> t1=new ArrayList<>();
        List<String> o=new ArrayList<>();
        int n=scan.nextInt();
        for(int i=0;i<n;i++){
            l.add(i,scan.next());
        }
        t=scan.nextInt();
        for(int j=0;j<t;j++){
            t1.add(j,scan.nextLine());
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<t;j++){
                if(l.get(i) == null ? t1.get(j) == null : l.get(i).equals(t1.get(j))){
                    o.add(j,t1.get(j));
                }
            }
        }
        for(int i=0;i<t;i++){
            System.out.println(o.get(i));
        }   
    }
}