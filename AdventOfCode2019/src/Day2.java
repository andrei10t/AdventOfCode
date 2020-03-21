import java.util.ArrayList;

public class Day2 {
    int noun = 0;
    int verb = 0;
    boolean part2 = false;

    public void compute(ArrayList<Integer> input) {
        int index = 0;
        if(part2){
            input.set(1, noun);
            input.set(2, verb);
        }
        while (true) {
            if (input.get(index) == 1) {
                input.set(input.get(index + 3), input.get(input.get(index + 1)) + input.get(input.get(index + 2)));
            } else if (input.get(index) == 2) {
                input.set(input.get(index + 3), input.get(input.get(index + 1)) * input.get(input.get(index + 2)));
            } else if (input.get(index) == 99) {
                if(input.get(0)==19690720){
                    System.out.println(noun * 100+verb);
                }
                if(!part2)
                    System.out.println(input.get(0));
                return;
            }
            index += 4;
        }
    }

    public void backtrack(ArrayList<Integer> input) {
        part2 = true;
        for (int i = 0; i < 100; i++){
            for (int j = 0; j < 100; j++) {
                ArrayList<Integer> clonelist=new ArrayList<>(input);
                noun=i;
                verb=j;
                compute(clonelist);
            }
        }
    }
}
