import java.util.Arrays;
import java.util.Scanner;

public class Practice2019 {


    public static void guessNumber(Scanner scan, int A, int B) {

        final String CORRECT = "CORRECT";
        final String TOO_SMALL="TOO_SMALL";
        final String TOO_BIG="TOO_BIG";
        final String WRONG_ANSWER="WRONG_ANSWER";
        String ans="";
        int guess=(A+B)/2;
        System.out.println(guess);
        ans=scan.next();
        if(ans.equals(CORRECT)) {
            return;
        }
        else if(ans.equals(TOO_BIG)) {
            guessNumber(scan,A,guess-1);
        }
        else if(ans.equals(TOO_SMALL)) {
            guessNumber(scan,guess+1,B);
        }
        else {
            return;
        }
    }

    public static void guessNumberMain(){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for(int i =0;i<T;i++) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            int N = scanner.nextInt();
            guessNumber(scanner,A+1,B);
        }
        scanner.close();
    }

    public int mural(String wall){
        int[] beautyScoreStartingAt = new int[wall.length()];
        int sumHalf=0;
        int halfLength = (wall.length()+1)/2;
        int mid;
        if(wall.length()%2==0) {
             mid = (wall.length() / 2)+1;
        }
        else
            mid = (wall.length()+1)/2;
        for(int i=0;i< halfLength;i++){
                sumHalf+=Character.getNumericValue(wall.charAt(i));
        }

        beautyScoreStartingAt[0]=sumHalf;
        for(int i=1;i<mid;i++){
            sumHalf=sumHalf-Character.getNumericValue(wall.charAt(i-1))+Character.getNumericValue(wall.charAt(i+halfLength-1));
            beautyScoreStartingAt[i]=sumHalf;
        }

        return Arrays.stream(beautyScoreStartingAt).max().getAsInt();
    }

    public void muralMain(){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i =1;i<=T;i++) {
            if(i!=1){
                System.out.println();
            }
            int N = scanner.nextInt();
            String wall = scanner.next();
            System.out.print("Case #"+i+": "+mural(wall));
        }
    }


    public static void main(String[] args){
       // guessNumberMain();
        Practice2019 problem =new Practice2019();
        problem.muralMain();
    }
}
