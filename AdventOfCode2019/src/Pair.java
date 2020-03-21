//used in day 3

public class Pair {
    int elem1;
    int elem2;

    public Pair(int x,int y){
        elem1 = x;
        elem2 = y;
    }

    public Pair(){

    }
    @Override
    public boolean equals(Object obj) {
        final Pair p= (Pair)obj;
        return this.elem2 == p.elem2 && this.elem1==p.elem1;
    }

    @Override
    public int hashCode() {
        return elem1*71+elem2;
    }

    public String toString(){
        String s = elem1+" "+elem2;
        return s;
    }
}
