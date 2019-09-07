import java.util.*;

class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;
	
	// Constructor
	Person(String firstName, String lastName, int identification){
		this.firstName = firstName;
		this.lastName = lastName;
		this.idNumber = identification;
	}
	
	// Print person data
	public void printPerson(){
		 System.out.println(
				"Name: " + lastName + ", " + firstName 
			+ 	"\nID: " + idNumber); 
	}
	 
}

class Student extends Person{
    private int[] testScores;
    private int a;
    private int sum=0;
    Student(String firstName, String lastName, int identification, int[] scores){
        super(firstName,lastName,identification); 
        this.testScores=scores;
    }
    public char calculate(){
        for(int i=0;i<testScores.length;i++){
            sum=sum+testScores[i];
        }
        a=sum/testScores.length;
        return ( a > 89 ? 'O' : a > 79 ? 'E' : a > 69 ? 'A' : a > 54 ? 'P' :a > 39 ? 'D' : 'T' );
    }
}
class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String firstName = scan.next();
		String lastName = scan.next();
		int id = scan.nextInt();
		int numScores = scan.nextInt();
		int[] testScores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			testScores[i] = scan.nextInt();
		}
		scan.close();
		
		Student s = new Student(firstName, lastName, id, testScores);
		s.printPerson();
		System.out.println("Grade: " + s.calculate() );
	}
}