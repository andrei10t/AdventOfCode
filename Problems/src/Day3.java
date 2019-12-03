import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import 

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
        Map<Pair, Integer> dict1 = new HashMap<>();
        Map<Pair, Integer> dict2 = new HashMap<>();
        add_all(input.get(0), dict1);
        add_all(input.get(0), dict2);
        Sets.Intersection

    }



}

//    int min=6000;
//    int curR=13000;
//    int curC=10000;
//
//    int sI=13000;
//    int sJ=10000;
//
//    int minCordI;
//    int minCordJ;
//
//
//
//
//    public void minDistance(int y1, int y2){
//        if(min> Math.abs(y1-sI) + Math.abs(y2-sJ)){
//            min=Math.abs(y1-sI) + Math.abs(y2-sJ);
//            minCordI=y1;
//            minCordJ=y2;
//        }
//    }
//
//
//    public void calculateDist2(){
//        int dist1;
//        int dist2;
//        int coordX=sI;
//        int coordY=sJ;
//
//    }
//
//
//    public void completeMatrix(int[][] matrix, String dir, int length,int color, int dist){
//        if(dir.equals("R")){
//            for(int i = curC+1; i<=curC+length;i++){
//                if(matrix[curR][i]!=0 && matrix[curR][i]!=color){
//                    minDistance(curR,i);
//                    dist++;
//                }
//                else{
//                    Coord c = new Coord(curR,i,color,++dist);
//                    matrix[curR][i]=color;
//                }
//            }
//            curC+=length;
//        }
//
//        if(dir.equals("L")){
//            for(int i = curC-1; i>=curC-length;i--){
//                if(matrix[curR][i]!=0 && matrix[curR][i]!=color){
//                    minDistance(curR,i);
//                    dist++;
//
//                }
//                else{
//                    matrix[curR][i]=color;
//                    Coord c = new Coord(curR,i,color,++dist);
//                }
//            }
//            curC-=length;
//        }
//
//        if(dir.equals("U")){
//            for(int i = curR-1; i>=curR-length;i--){
//                if(matrix[i][curC]!=0 && matrix[i][curC]!=color){
//                    minDistance(i,curC);
//                    dist++;
//                }
//                else{
//                    matrix[i][curC]=color;
//                    Coord c = new Coord(curR,i,color,++dist);
//                }
//            }
//            curR-=length;
//        }
//
//        if(dir.equals("D")){
//            for(int i = curR+1; i<=curR+length;i++){
//                if(matrix[i][curC]!=0 && matrix[i][curC]!=color){
//                    minDistance(i,curC);
//                    dist++;
//                }
//                else{
//                    matrix[i][curC]=color;
//                    Coord c = new Coord(curR,i,color,++dist);
//                }
//            }
//            curR+=length;
//        }
//
//    }
//
//    public void solve(ArrayList<ArrayList<String>> input) {
//        int[][] matrix = new int[20000][20000];
//        matrix[sI][sJ] = 0;
//        String direction;
//        int length;
//        int color = 1;
//
//        for (ArrayList<String> wire : input) {
//            curR = 13000;
//            curC = 10000;
//            int dist=0;
//            for (String s : wire) {
//                direction = s.substring(0, 1);
//                length = Integer.parseInt(s.substring(1));
//                completeMatrix(matrix, direction, length, color, dist);
//
//            }
//            color++;
//        }
//        System.out.println(min);
//        System.out.println();
//    }
//
//
//
//}
//
//class Coord{
//    int x;
//    int y;
//    int wire1Dist;
//    int wire2Dist;
//
//    public Coord(int x, int y, int color, int dist){
//        this.x=x;
//        this.y=y;
//        if(color==1){
//            this.wire1Dist=dist;
//        }
//        else{
//            this.wire2Dist=dist;
//        }
//    }
