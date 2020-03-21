import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Day6 {


    public void solve(ArrayList<String> input){
        Graph<String> graph = new Graph<>();
        Set<String> set = new HashSet<>();
        for(int i=0;i<input.size();i+=2){
            String orbited = input.get(i);
            String orbiter = input.get(i+1);
            if(!set.contains(orbited)){
                Graph.Node n = g.newNode(orbited);
                n.children.add(g.newNode(orbiter));
                set.add(orbited);
                set.add(orbiter);
            }
            else if(!set.contains(orbiter)){

            }
        }

        System.out.println(solarSystem.values().stream().reduce(0, (a,b) -> a+b));

    }
}
