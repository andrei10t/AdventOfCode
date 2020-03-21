import java.util.Scanner;

public class Task {
    public void allocationMain(){
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i=0;i<t;i++){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            if(a%b==0)
                System.out.println("YES");
            else
                System.out.println("NO");
        }

        scanner.close();
    }

    public static void main(String[] args){
        Task problem =new Task();
        problem.allocationMain();
    }
}
