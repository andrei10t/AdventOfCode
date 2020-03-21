import java.util.ArrayList;
import java.util.Stack;

public class Day5 {


    public void running(ArrayList<Integer> input,Stack<Integer> stackIn, Stack<Integer> stackOut){
        int pointer = 0;
        while (true) {
            Instruction instruction = new Instruction();
            instruction.setInstruction(input, pointer);
            int par1 = instruction.param1;
            int par2 = instruction.param2;
            switch (instruction.opCode) {
                case ADD:
                    input.set(input.get(pointer + 3), par1 + par2);
                    pointer += 4;
                    break;

                case MULT:
                    input.set(input.get(pointer + 3), par1 * par2);
                    pointer += 4;
                    break;

                case INPUT:
                    input.set(input.get(pointer + 1), stackIn.pop());
                    pointer += 2;
                    break;

                case OUTPUT:
                    stackOut.push(par1);
                    pointer += 2;
                    break;
                case JUMP_IF_TRUE :
                    pointer = par1 != 0 ? par2 : pointer + 3;
                    break;

                case JUMP_IF_FALSE:
                    pointer = par1 == 0 ? par2 : pointer + 3;
                    break;

                case LESS_THAN:
                    input.set(input.get(pointer + 3), par1 < par2 ? 1 : 0);
                    pointer += 4;
                    break;

                case EQUALS:
                    input.set(input.get(pointer + 3), par1 == par2 ? 1 : 0);
                    pointer += 4;
                    break;

                case HALT:
                    return;

            }
        }
    }

    public void solve(ArrayList<Integer> input) {
        Stack<Integer> stackIn = new Stack<>();
        Stack<Integer> stackOut = new Stack<>();
        stackIn.push(5);
        running(input,stackIn,stackOut);
        System.out.println(stackOut.pop());
    }

}
