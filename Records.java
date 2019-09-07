import java.io.*;
import java.util.*;

public class Records {

    // Complete the breakingRecords function below.
    static int[] breakingRecords(int[] scores) {
        int[] breakingRecords = new int[2];
        breakingRecords[0]=0;
        breakingRecords[1]=0;
        int mi=scores[0];
        int ma=scores[0];
        for(int i=0;i<scores.length;i++){
            if(scores[i]>ma){
                breakingRecords[0]++;
                ma=scores[i];
            }
            else if(scores[i]<mi){
                breakingRecords[1]++;
                mi=scores[i];
            }
        }
        return breakingRecords;
    }
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] scores = new int[n];

        String[] scoresItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int scoresItem = Integer.parseInt(scoresItems[i]);
            scores[i] = scoresItem;
        }

        int[] result = breakingRecords(scores);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write(" ");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}