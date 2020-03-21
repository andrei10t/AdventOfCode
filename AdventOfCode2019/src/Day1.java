import java.util.ArrayList;
import java.util.function.Predicate;

public class Day1 {

     int result;


    public void computeSum(ArrayList<Integer> input) {
        result = input.stream().map(e->e/3-2).reduce(0,Integer::sum);
    }

    public ArrayList<Integer> computeSum2(ArrayList<Integer> input) {
        ArrayList<Integer> newList = new ArrayList<>();
        result = 0;
        input.stream().forEach(e ->
        {
            e = e / 3 - 2;
            if (e > 0) {
                result += e;
                newList.add(e);
            }
        });
        return newList;
    }

    public void recursiveComputing(ArrayList<Integer> input) {
        while(!input.isEmpty()) {
            input=computeSum2(input);
        }
    }

}
