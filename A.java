import java.util.*; 
  
class Solution { 
       
    static boolean isPrime(int n) 
    { 
        if (n <= 1) 
            return false; 
       
        for (int i = 2; i < n; i++) 
            if (n % i == 0) 
                return false;
       
        return true; 
    } 

    public static void main(String[] args)  
    {
        Scanner scan=new Scanner(System.in);
        int t=scan.nextInt(); 
        ArrayList<Integer>n=new ArrayList<>();
        for(int i=0;i<t;i++){
            n.add(scan.nextInt());
            if(isPrime(n.get(i)))
                System.out.println("Prime");
            else
                System.out.println("Not prime");
        }
    } 
} 

