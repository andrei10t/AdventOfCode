
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

       public static final String fileDay1 = "/Users/atoader/work/AdventOfCode2019/Problems/input_3.txt";

    public ArrayList<Integer> getAsArrayList() {

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

    public ArrayList<Integer> delimiter(){
        ArrayList<Integer> input = new ArrayList<>();
        try {
            Scanner scanner = new Scanner(new File(fileDay1));
            String[] stuff = scanner.nextLine().split(",");
            for (String s: stuff) {
                input.add(Integer.parseInt(s));
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return input;
    }

    public ArrayList<ArrayList<String>> delimiterString(){
        ArrayList<ArrayList<String>> input = new ArrayList<>();
        try {
            Scanner scanner = new Scanner(new File(fileDay1));
            while(scanner.hasNextLine()) {
                ArrayList<String> wire = new ArrayList<>();
                String[] stuff = scanner.nextLine().split(",");
                for (String s : stuff) {
                    wire.add(s);
                }
                input.add(wire);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return input;
    }


    public void solve1Day1() {
        ArrayList<Integer> input = getAsArrayList();
        Day1 day1 = new Day1();

        day1.computeSum(input);
        System.out.println(day1.result);

        day1.recursiveComputing(input);
        System.out.println(day1.result);
    }

    public void solveDay2(){
        ArrayList<Integer> input = delimiter();
        ArrayList<Integer> clone = new ArrayList<>(input);
        Day2 day2 = new Day2();

        day2.compute(input);
        day2.backtrack(clone);

    }

    public void solveDay3(){
        ArrayList<ArrayList<String>>input = delimiterString();
        Day3 day3 = new Day3();
        day3.solve(input);
    }

    public void solveDay4(){
        Day4 day4 = new Day4();
        day4.solve();
    }

    public static void main(String[] args) {
      Main solution = new Main();
      //solution.solve1Day1();
     // solution.solveDay2();
        //solution.solveDay3();
        solution.solveDay4();
    }
}
