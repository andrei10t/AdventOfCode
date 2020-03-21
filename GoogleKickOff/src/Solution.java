import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class Solution {

    public int allocation(int B, LinkedList<Integer> housesPrice){
        Collections.sort(housesPrice);

        int contor=0;
        if(housesPrice.size()!=0) {
            while(B>0){
                B-=housesPrice.getFirst();
                housesPrice.removeFirst();
                contor++;
            }
        }
        return B<0 ? contor-1 : contor;
    }

    public void allocationMain(){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i=1;i<=T;i++) {

            int N = scanner.nextInt();
            int B = scanner.nextInt();
            LinkedList<Integer> housesPrice = new LinkedList<>();


            for(int j =0; j<N;j++){
                housesPrice.add(scanner.nextInt());
            }

            System.out.println("Case #"+i+": "+allocation(B,housesPrice));
        }

        scanner.close();
    }

    public static void main(String[] args){
        Solution problem =new Solution();
        problem.allocationMain();
    }
}
