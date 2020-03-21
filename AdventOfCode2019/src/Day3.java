import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Day3 {


    public void add_all(ArrayList<String> wire, Map<Pair,Integer> dict){
        int r = 0;
        int c = 0;
        int dist = 0;

        for (String s : wire) {
            String direction = s.substring(0, 1);
            int length = Integer.parseInt(s.substring(1));

            switch (direction) {
                case "R":
                    for (int i = 0; i < length; i++) {
                        c++;
                        dist++;
                        dict.put(new Pair(r, c), dist);
                    }
                    break;
                case "L":
                    for (int i = 0; i < length; i++) {
                        c--;
                        dist++;
                        dict.put(new Pair(r, c), dist);
                    }
                    break;
                case "D":
                    for (int i = 0; i < length; i++) {
                        r++;
                        dist++;
                        dict.put(new Pair(r, c), dist);
                    }
                    break;
                case "U":
                    for (int i = 0; i < length; i++) {
                        r--;
                        dist++;
                        dict.put(new Pair(r, c), dist);
                    }
                    break;
            }
        }
    }

    public void solve(ArrayList<ArrayList<String>> input){
        Map<Pair,Integer> dict1 = new HashMap<>();
        Map<Pair, Integer> dict2 = new HashMap<Pair,Integer>(){
            private static final long serialVersionUID = 1L;

            @Override
            public boolean containsKey(Object obj) {
                Pair  paar = (Pair) obj;
                for (Pair mad : this.keySet()) {
                    if (mad.equals(paar)) {
                        return true;
                    }
                }
                return false;
            }
        };

        add_all(input.get(0), dict1);
        add_all(input.get(1), dict2);

        int min = Integer.MAX_VALUE;
        int dist2 = Integer.MAX_VALUE;
        for(Pair p: dict1.keySet())
        {
            if(dict2.containsKey(p))
            {
                min=Math.min(Math.abs(p.elem1) + Math.abs(p.elem2), min);
                dist2=Math.min(dist2, dict1.get(p)+dict2.get(p));
            }
        }

        System.out.println(min);
        System.out.println(dist2);

    }
}

