import jdk.nashorn.internal.runtime.regexp.joni.constants.OPCode;

import javax.management.openmbean.OpenDataException;
import java.util.ArrayList;

//used in day 5
public class Instruction {
    OpCode opCode;
    int param1;
    int param2;
    int param3;

    public Instruction(OpCode opCode, int param1, int param2, int param3){
        this.opCode=opCode;
        this.param1=param1;
        this.param2=param2;
        this.param3=param3;
    }

    public Instruction(){

    }

    public void setInstruction(ArrayList<Integer> input, int pointer){
        int code = input.get(pointer);
        this.opCode = OpCode.getValue(code%100);
        this.param1 = getValueOfParameter(input, pointer+1, Mode.getMode((code/100)%2));
        this.param2 = getValueOfParameter(input, pointer+2, Mode.getMode((code/1000)%2));
        this.param3 = getValueOfParameter(input, pointer+3, Mode.getMode((code/10000)%2));
    }

    public int getValueOfParameter(ArrayList<Integer> input, int pointer, Mode mode){
        if(pointer>=input.size())
            return 0;
        int result =  input.get(pointer);
        if(Mode.IMMEDIATE.equals(mode)){
            return result;
        }
        else{
            return result>=0 && result < input.size() ? input.get(result) : 0;
        }
    }




    enum Mode {
        POSITION,
        IMMEDIATE;

         static Mode getMode(int code) {
            switch (code) {
                case 0:
                    return POSITION;
                case 1:
                    return IMMEDIATE;
                default:
                    throw new UnsupportedOperationException();
            }
        }
    }


    enum OpCode{
        ADD, MULT, INPUT, OUTPUT, HALT, JUMP_IF_TRUE, JUMP_IF_FALSE, LESS_THAN, EQUALS;

        static OpCode getValue(int code){
            switch (code){
                case 1:
                    return ADD;
                case 2:
                    return MULT;
                case 3:
                    return INPUT;
                case 4:
                    return OUTPUT;
                case 5:
                    return JUMP_IF_TRUE;
                case 6:
                    return JUMP_IF_FALSE;
                case 7:
                    return LESS_THAN;
                case 8:
                    return EQUALS;
                case 99:
                    return HALT;
                default:
                    throw new UnsupportedOperationException();
            }
        }

    }

}



