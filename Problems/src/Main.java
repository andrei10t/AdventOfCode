import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static final String fileDay1 = "/Users/atoader/work/AdventOfCode2019/Problems/input_1.txt";

    public ArrayList<Integer> getAsArrayList(){

       ArrayList<Integer> input = new ArrayList<>();
        try {
            Scanner scanner = new Scanner(new File(fileDay1));
            while (scanner.hasNextLine()) {
                input.add(Integer.parseInt(scanner.nextLine()));
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return input;
    }


    public void solve1Day1(){
        ArrayList<Integer> input = getAsArrayList();
        Day1 day1 = new Day1();
        day1.computeSum(input);
        System.out.println(day1.result);
        day1.result=0;
        day1.recursiveComputing(input);
        System.out.println(day1.result);
    }



    public static void main(String[] args){
      Main solution = new Main();

      solution.solve1Day1();

    }

}
