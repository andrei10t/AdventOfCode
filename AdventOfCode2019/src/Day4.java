public class Day4 {
    int left = 158888;
    int right = 624574;

    public boolean checkNumber(int aux){
        int last=10;
        int cnt=0;
        int[] appar= new int[10];
        boolean doubleDigits=false;
        while(aux!=0){
            int curr = aux%10;
            if(curr>last)
                return false;
            appar[curr]++;
            aux/=10;
            last=curr;
        }
        for(int i=1;i<=9;i++){
            if(appar[i]==2){   //>=2 for part  1
                doubleDigits=true;
            }
        }
        return doubleDigits;
    }

    public void solve(){
        int result=0;
        for(int i = left; i<=right;i++){
            if(checkNumber(i))
                result++;
        }
        System.out.println(result);

    }

}
