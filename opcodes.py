from microassembler import Opcode


Opcode.NoOperation(Extended=False)
Opcode.ExtendOpcode(Extended=False)

Opcode.Halt(Extended=True)

Opcode.SetCarry(Extended=False)
Opcode.ClearCarry(Extended=False)

Opcode.EnableInterrupts(Extended=True)
Opcode.DisableInterrupts(Extended=True)

Opcode.EnableBankRegister(Extended=True)
Opcode.DisableBankRegister(Extended=True)

Opcode.MoveBRtoA(Extended=True)
Opcode.MoveAtoBR(Extended=True)

Opcode.MoveAtoB(Extended=False)
Opcode.MoveAtoC(Extended=False)
Opcode.MoveAtoD(Extended=False)

Opcode.MoveBtoA(Extended=False)
Opcode.MoveBtoC(Extended=False)
Opcode.MoveBtoD(Extended=False)

Opcode.MoveCtoA(Extended=False)
Opcode.MoveCtoB(Extended=False)
Opcode.MoveCtoD(Extended=False)

Opcode.MoveDtoA(Extended=False)
Opcode.MoveDtoB(Extended=False)
Opcode.MoveDtoC(Extended=False)

# Input Modes:
#    - Port: Zero Page IO Address.
#    - Offset: Immediate value.
#    - Index: Dynamic offset from GPR.
#    - GPR: A, B, C, D
#    - Pointer: X, Y
#
# 1. Input from a Port to GPR.
# 2. Input from Pointer + Offset to GPR.
# 3. Input from Pointer + Index to GPR.

Opcode.InputPortToA(Extended=False)
Opcode.InputXOffsetToA(Extended=False)
Opcode.InputYOffsetToA(Extended=False)

Opcode.InputXIndexAToA(Extended=True)
Opcode.InputXIndexBToA(Extended=True)
Opcode.InputXIndexCToA(Extended=True)
Opcode.InputXIndexDToA(Extended=True)

Opcode.InputYIndexAToA(Extended=True)
Opcode.InputYIndexBToA(Extended=True)
Opcode.InputYIndexCToA(Extended=True)
Opcode.InputYIndexDToA(Extended=True)

Opcode.IN_B_PORT(Extended=False)
Opcode.IN_B_X_IDX(Extended=False)
Opcode.IN_B_X_A(Extended=True)
Opcode.IN_B_X_B(Extended=True)
Opcode.IN_B_X_C(Extended=True)
Opcode.IN_B_X_D(Extended=True)
Opcode.IN_B_Y_IDX(Extended=False)
Opcode.IN_B_Y_A(Extended=True)
Opcode.IN_B_Y_B(Extended=True)
Opcode.IN_B_Y_C(Extended=True)
Opcode.IN_B_Y_D(Extended=True)
Opcode.IN_C_PORT(Extended=False)
Opcode.IN_C_X_IDX(Extended=False)
Opcode.IN_C_X_A(Extended=True)
Opcode.IN_C_X_B(Extended=True)
Opcode.IN_C_X_C(Extended=True)
Opcode.IN_C_X_D(Extended=True)
Opcode.IN_C_Y_IDX(Extended=False)
Opcode.IN_C_Y_A(Extended=True)
Opcode.IN_C_Y_B(Extended=True)
Opcode.IN_C_Y_C(Extended=True)
Opcode.IN_C_Y_D(Extended=True)
Opcode.IN_D_PORT(Extended=False)
Opcode.IN_D_X_IDX(Extended=False)
Opcode.IN_D_X_A(Extended=True)
Opcode.IN_D_X_B(Extended=True)
Opcode.IN_D_X_C(Extended=True)
Opcode.IN_D_X_D(Extended=True)
Opcode.IN_D_Y_IDX(Extended=False)
Opcode.IN_D_Y_A(Extended=True)
Opcode.IN_D_Y_B(Extended=True)
Opcode.IN_D_Y_C(Extended=True)
Opcode.IN_D_Y_D(Extended=True)
Opcode.OUT_IMM(Extended=True)
Opcode.OUT_A_PORT(Extended=False)
Opcode.OUT_A_X_IDX(Extended=False)
Opcode.OUT_A_X_A(Extended=True)
Opcode.OUT_A_X_B(Extended=True)
Opcode.OUT_A_X_C(Extended=True)
Opcode.OUT_A_X_D(Extended=True)
Opcode.OUT_A_Y_IDX(Extended=False)
Opcode.OUT_A_Y_A(Extended=True)
Opcode.OUT_A_Y_B(Extended=True)
Opcode.OUT_A_Y_C(Extended=True)
Opcode.OUT_A_Y_D(Extended=True)
Opcode.OUT_B_PORT(Extended=False)
Opcode.OUT_B_X_IDX(Extended=False)
Opcode.OUT_B_X_A(Extended=True)
Opcode.OUT_B_X_B(Extended=True)
Opcode.OUT_B_X_C(Extended=True)
Opcode.OUT_B_X_D(Extended=True)
Opcode.OUT_B_Y_IDX(Extended=False)
Opcode.OUT_B_Y_A(Extended=True)
Opcode.OUT_B_Y_B(Extended=True)
Opcode.OUT_B_Y_C(Extended=True)
Opcode.OUT_B_Y_D(Extended=True)
Opcode.OUT_C_PORT(Extended=False)
Opcode.OUT_C_X_IDX(Extended=False)
Opcode.OUT_C_X_A(Extended=True)
Opcode.OUT_C_X_B(Extended=True)
Opcode.OUT_C_X_C(Extended=True)
Opcode.OUT_C_X_D(Extended=True)
Opcode.OUT_C_Y_IDX(Extended=False)
Opcode.OUT_C_Y_A(Extended=True)
Opcode.OUT_C_Y_B(Extended=True)
Opcode.OUT_C_Y_C(Extended=True)
Opcode.OUT_C_Y_D(Extended=True)
Opcode.OUT_D_PORT(Extended=False)
Opcode.OUT_D_X_IDX(Extended=False)
Opcode.OUT_D_X_A(Extended=True)
Opcode.OUT_D_X_B(Extended=True)
Opcode.OUT_D_X_C(Extended=True)
Opcode.OUT_D_X_D(Extended=True)
Opcode.OUT_D_Y_IDX(Extended=False)
Opcode.OUT_D_Y_A(Extended=True)
Opcode.OUT_D_Y_B(Extended=True)
Opcode.OUT_D_Y_C(Extended=True)
Opcode.OUT_D_Y_D(Extended=True)
Opcode.LOAD_A_IMM(Extended=False)
Opcode.LOAD_A_ABS(Extended=False)
Opcode.LOAD_A_X_IDX(Extended=False)
Opcode.LOAD_A_X_A(Extended=False)
Opcode.LOAD_A_X_B(Extended=False)
Opcode.LOAD_A_X_C(Extended=False)
Opcode.LOAD_A_X_D(Extended=False)
Opcode.LOAD_A_Y_IDX(Extended=False)
Opcode.LOAD_A_Y_A(Extended=False)
Opcode.LOAD_A_Y_B(Extended=False)
Opcode.LOAD_A_Y_C(Extended=False)
Opcode.LOAD_A_Y_D(Extended=False)
Opcode.LOAD_A_SP_IDX(Extended=False)
Opcode.LOAD_A_SP_A(Extended=False)
Opcode.LOAD_A_SP_B(Extended=False)
Opcode.LOAD_A_SP_C(Extended=False)
Opcode.LOAD_A_SP_D(Extended=False)
Opcode.LOAD_B_IMM(Extended=False)
Opcode.LOAD_B_ABS(Extended=False)
Opcode.LOAD_B_X_IDX(Extended=False)
Opcode.LOAD_B_X_A(Extended=False)
Opcode.LOAD_B_X_B(Extended=False)
Opcode.LOAD_B_X_C(Extended=False)
Opcode.LOAD_B_X_D(Extended=False)
Opcode.LOAD_B_Y_IDX(Extended=False)
Opcode.LOAD_B_Y_A(Extended=False)
Opcode.LOAD_B_Y_B(Extended=False)
Opcode.LOAD_B_Y_C(Extended=False)
Opcode.LOAD_B_Y_D(Extended=False)
Opcode.LOAD_B_SP_IDX(Extended=False)
Opcode.LOAD_B_SP_A(Extended=False)
Opcode.LOAD_B_SP_B(Extended=False)
Opcode.LOAD_B_SP_C(Extended=False)
Opcode.LOAD_B_SP_D(Extended=False)
Opcode.LOAD_C_IMM(Extended=False)
Opcode.LOAD_C_ABS(Extended=False)
Opcode.LOAD_C_X_IDX(Extended=False)
Opcode.LOAD_C_X_A(Extended=False)
Opcode.LOAD_C_X_B(Extended=False)
Opcode.LOAD_C_X_C(Extended=False)
Opcode.LOAD_C_X_D(Extended=False)
Opcode.LOAD_C_Y_IDX(Extended=False)
Opcode.LOAD_C_Y_A(Extended=False)
Opcode.LOAD_C_Y_B(Extended=False)
Opcode.LOAD_C_Y_C(Extended=False)
Opcode.LOAD_C_Y_D(Extended=False)
Opcode.LOAD_C_SP_IDX(Extended=False)
Opcode.LOAD_C_SP_A(Extended=False)
Opcode.LOAD_C_SP_B(Extended=False)
Opcode.LOAD_C_SP_C(Extended=False)
Opcode.LOAD_C_SP_D(Extended=False)
Opcode.LOAD_D_IMM(Extended=False)
Opcode.LOAD_D_ABS(Extended=False)
Opcode.LOAD_D_X_IDX(Extended=False)
Opcode.LOAD_D_X_A(Extended=False)
Opcode.LOAD_D_X_B(Extended=False)
Opcode.LOAD_D_X_C(Extended=False)
Opcode.LOAD_D_X_D(Extended=False)
Opcode.LOAD_D_Y_IDX(Extended=False)
Opcode.LOAD_D_Y_A(Extended=False)
Opcode.LOAD_D_Y_B(Extended=False)
Opcode.LOAD_D_Y_C(Extended=False)
Opcode.LOAD_D_Y_D(Extended=False)
Opcode.LOAD_D_SP_IDX(Extended=False)
Opcode.LOAD_D_SP_A(Extended=False)
Opcode.LOAD_D_SP_B(Extended=False)
Opcode.LOAD_D_SP_C(Extended=False)
Opcode.LOAD_D_SP_D(Extended=False)
Opcode.STORE_A_ABS(Extended=False)
Opcode.STORE_A_X_IDX(Extended=False)
Opcode.STORE_A_X_A(Extended=False)
Opcode.STORE_A_X_B(Extended=False)
Opcode.STORE_A_X_C(Extended=False)
Opcode.STORE_A_X_D(Extended=False)
Opcode.STORE_A_Y_IDX(Extended=False)
Opcode.STORE_A_Y_A(Extended=False)
Opcode.STORE_A_Y_B(Extended=False)
Opcode.STORE_A_Y_C(Extended=False)
Opcode.STORE_A_Y_D(Extended=False)
Opcode.STORE_A_SP_IDX(Extended=False)
Opcode.STORE_A_SP_A(Extended=False)
Opcode.STORE_A_SP_B(Extended=False)
Opcode.STORE_A_SP_C(Extended=False)
Opcode.STORE_A_SP_D(Extended=False)
Opcode.STORE_B_ABS(Extended=False)
Opcode.STORE_B_X_IDX(Extended=False)
Opcode.STORE_B_X_A(Extended=False)
Opcode.STORE_B_X_B(Extended=False)
Opcode.STORE_B_X_C(Extended=False)
Opcode.STORE_B_X_D(Extended=False)
Opcode.STORE_B_Y_IDX(Extended=False)
Opcode.STORE_B_Y_A(Extended=False)
Opcode.STORE_B_Y_B(Extended=False)
Opcode.STORE_B_Y_C(Extended=False)
Opcode.STORE_B_Y_D(Extended=False)
Opcode.STORE_B_SP_IDX(Extended=False)
Opcode.STORE_B_SP_A(Extended=False)
Opcode.STORE_B_SP_B(Extended=False)
Opcode.STORE_B_SP_C(Extended=False)
Opcode.STORE_B_SP_D(Extended=False)
Opcode.STORE_C_ABS(Extended=False)
Opcode.STORE_C_X_IDX(Extended=False)
Opcode.STORE_C_X_A(Extended=False)
Opcode.STORE_C_X_B(Extended=False)
Opcode.STORE_C_X_C(Extended=False)
Opcode.STORE_C_X_D(Extended=False)
Opcode.STORE_C_Y_IDX(Extended=False)
Opcode.STORE_C_Y_A(Extended=False)
Opcode.STORE_C_Y_B(Extended=False)
Opcode.STORE_C_Y_C(Extended=False)
Opcode.STORE_C_Y_D(Extended=False)
Opcode.STORE_C_SP_IDX(Extended=False)
Opcode.STORE_C_SP_A(Extended=False)
Opcode.STORE_C_SP_B(Extended=False)
Opcode.STORE_C_SP_C(Extended=False)
Opcode.STORE_C_SP_D(Extended=False)
Opcode.STORE_D_ABS(Extended=False)
Opcode.STORE_D_X_IDX(Extended=False)
Opcode.STORE_D_X_A(Extended=False)
Opcode.STORE_D_X_B(Extended=False)
Opcode.STORE_D_X_C(Extended=False)
Opcode.STORE_D_X_D(Extended=False)
Opcode.STORE_D_Y_IDX(Extended=False)
Opcode.STORE_D_Y_A(Extended=False)
Opcode.STORE_D_Y_B(Extended=False)
Opcode.STORE_D_Y_C(Extended=False)
Opcode.STORE_D_Y_D(Extended=False)
Opcode.STORE_D_SP_IDX(Extended=False)
Opcode.STORE_D_SP_A(Extended=False)
Opcode.STORE_D_SP_B(Extended=False)
Opcode.STORE_D_SP_C(Extended=False)
Opcode.STORE_D_SP_D(Extended=False)
Opcode.MOV_X_Y(Extended=False)
Opcode.MOV_X_AB(Extended=False)
Opcode.MOV_X_CD(Extended=False)
Opcode.MOV_Y_X(Extended=False)
Opcode.MOV_Y_AB(Extended=False)
Opcode.MOV_Y_CD(Extended=False)
Opcode.MOV_AB_X(Extended=False)
Opcode.MOV_AB_Y(Extended=False)
Opcode.MOV_CD_X(Extended=False)
Opcode.MOV_CD_Y(Extended=False)
Opcode.MOV_SP_X(Extended=True)
Opcode.MOV_X_SP(Extended=True)
Opcode.LOAD_X_IMM(Extended=False)
Opcode.LOAD_X_ABS(Extended=False)
Opcode.LOAD_X_X_IDX(Extended=False)
Opcode.LOAD_X_Y_IDX(Extended=False)
Opcode.LOAD_X_SP_IDX(Extended=False)
Opcode.LOAD_Y_IMM(Extended=False)
Opcode.LOAD_Y_ABS(Extended=False)
Opcode.LOAD_Y_X_IDX(Extended=False)
Opcode.LOAD_Y_Y_IDX(Extended=False)
Opcode.LOAD_Y_SP_IDX(Extended=False)
Opcode.STORE_X_ABS(Extended=False)
Opcode.STORE_X_X_IDX(Extended=False)
Opcode.STORE_X_Y_IDX(Extended=False)
Opcode.STORE_X_SP_IDX(Extended=False)
Opcode.STORE_Y_ABS(Extended=False)
Opcode.STORE_Y_X_IDX(Extended=False)
Opcode.STORE_Y_Y_IDX(Extended=False)
Opcode.STORE_Y_SP_IDX(Extended=False)
Opcode.LEA_X_A(Extended=True)
Opcode.LEA_X_B(Extended=True)
Opcode.LEA_X_C(Extended=True)
Opcode.LEA_X_D(Extended=True)
Opcode.LEA_X_IDX(Extended=False)
Opcode.LEA_Y_A(Extended=True)
Opcode.LEA_Y_B(Extended=True)
Opcode.LEA_Y_C(Extended=True)
Opcode.LEA_Y_D(Extended=True)
Opcode.LEA_Y_IDX(Extended=False)
Opcode.LEA_SP_A(Extended=True)
Opcode.LEA_SP_B(Extended=True)
Opcode.LEA_SP_C(Extended=True)
Opcode.LEA_SP_D(Extended=True)
Opcode.LEA_SP_IDX(Extended=False)
Opcode.ADC_A_A(Extended=True)
Opcode.ADC_A_B(Extended=True)
Opcode.ADC_A_C(Extended=True)
Opcode.ADC_A_D(Extended=True)
Opcode.ADC_A_IMM(Extended=True)
Opcode.ADC_B_A(Extended=True)
Opcode.ADC_B_B(Extended=True)
Opcode.ADC_B_C(Extended=True)
Opcode.ADC_B_D(Extended=True)
Opcode.ADC_B_IMM(Extended=True)
Opcode.ADC_C_A(Extended=True)
Opcode.ADC_C_B(Extended=True)
Opcode.ADC_C_C(Extended=True)
Opcode.ADC_C_D(Extended=True)
Opcode.ADC_C_IMM(Extended=True)
Opcode.ADC_D_A(Extended=True)
Opcode.ADC_D_B(Extended=True)
Opcode.ADC_D_C(Extended=True)
Opcode.ADC_D_D(Extended=True)
Opcode.ADC_D_IMM(Extended=True)
Opcode.SBC_A_A(Extended=True)
Opcode.SBC_A_B(Extended=True)
Opcode.SBC_A_C(Extended=True)
Opcode.SBC_A_D(Extended=True)
Opcode.SBC_A_IMM(Extended=True)
Opcode.SBC_B_A(Extended=True)
Opcode.SBC_B_B(Extended=True)
Opcode.SBC_B_C(Extended=True)
Opcode.SBC_B_D(Extended=True)
Opcode.SBC_B_IMM(Extended=True)
Opcode.SBC_C_A(Extended=True)
Opcode.SBC_C_B(Extended=True)
Opcode.SBC_C_C(Extended=True)
Opcode.SBC_C_D(Extended=True)
Opcode.SBC_C_IMM(Extended=True)
Opcode.SBC_D_A(Extended=True)
Opcode.SBC_D_B(Extended=True)
Opcode.SBC_D_C(Extended=True)
Opcode.SBC_D_D(Extended=True)
Opcode.SBC_D_IMM(Extended=True)
Opcode.AND_A_B(Extended=True)
Opcode.AND_A_C(Extended=True)
Opcode.AND_A_D(Extended=True)
Opcode.AND_A_IMM(Extended=True)
Opcode.AND_B_A(Extended=True)
Opcode.AND_B_C(Extended=True)
Opcode.AND_B_D(Extended=True)
Opcode.AND_B_IMM(Extended=True)
Opcode.AND_C_A(Extended=True)
Opcode.AND_C_B(Extended=True)
Opcode.AND_C_D(Extended=True)
Opcode.AND_C_IMM(Extended=True)
Opcode.AND_D_A(Extended=True)
Opcode.AND_D_B(Extended=True)
Opcode.AND_D_C(Extended=True)
Opcode.AND_D_IMM(Extended=True)
Opcode.OR_A_B(Extended=True)
Opcode.OR_A_C(Extended=True)
Opcode.OR_A_D(Extended=True)
Opcode.OR_A_IMM(Extended=True)
Opcode.OR_B_A(Extended=True)
Opcode.OR_B_C(Extended=True)
Opcode.OR_B_D(Extended=True)
Opcode.OR_B_IMM(Extended=True)
Opcode.OR_C_A(Extended=True)
Opcode.OR_C_B(Extended=True)
Opcode.OR_C_D(Extended=True)
Opcode.OR_C_IMM(Extended=True)
Opcode.OR_D_A(Extended=True)
Opcode.OR_D_B(Extended=True)
Opcode.OR_D_C(Extended=True)
Opcode.OR_D_IMM(Extended=True)
Opcode.XOR_A_A(Extended=True)
Opcode.XOR_A_B(Extended=True)
Opcode.XOR_A_C(Extended=True)
Opcode.XOR_A_D(Extended=True)
Opcode.XOR_A_IMM(Extended=True)
Opcode.XOR_B_A(Extended=True)
Opcode.XOR_B_B(Extended=True)
Opcode.XOR_B_C(Extended=True)
Opcode.XOR_B_D(Extended=True)
Opcode.XOR_B_IMM(Extended=True)
Opcode.XOR_C_A(Extended=True)
Opcode.XOR_C_B(Extended=True)
Opcode.XOR_C_C(Extended=True)
Opcode.XOR_C_D(Extended=True)
Opcode.XOR_C_IMM(Extended=True)
Opcode.XOR_D_A(Extended=True)
Opcode.XOR_D_B(Extended=True)
Opcode.XOR_D_C(Extended=True)
Opcode.XOR_D_D(Extended=True)
Opcode.XOR_D_IMM(Extended=True)
Opcode.NOT_A(Extended=True)
Opcode.NOT_B(Extended=True)
Opcode.NOT_C(Extended=True)
Opcode.NOT_D(Extended=True)
Opcode.NEG_A(Extended=True)
Opcode.NEG_B(Extended=True)
Opcode.NEG_C(Extended=True)
Opcode.NEG_D(Extended=True)
Opcode.SRC_A(Extended=True)
Opcode.SRC_B(Extended=True)
Opcode.SRC_C(Extended=True)
Opcode.SRC_D(Extended=True)
Opcode.ASR_A(Extended=True)
Opcode.ASR_B(Extended=True)
Opcode.ASR_C(Extended=True)
Opcode.ASR_D(Extended=True)
Opcode.INC_A(Extended=True)
Opcode.INC_B(Extended=True)
Opcode.INC_C(Extended=True)
Opcode.INC_D(Extended=True)
Opcode.INC_X(Extended=False)
Opcode.INC_Y(Extended=False)
Opcode.DEC_A(Extended=True)
Opcode.DEC_B(Extended=True)
Opcode.DEC_C(Extended=True)
Opcode.DEC_D(Extended=True)
Opcode.DEC_X(Extended=False)
Opcode.DEC_Y(Extended=False)
Opcode.PUSH_A(Extended=False)
Opcode.PUSH_B(Extended=False)
Opcode.PUSH_C(Extended=False)
Opcode.PUSH_D(Extended=False)
Opcode.PUSH_X(Extended=False)
Opcode.PUSH_Y(Extended=False)
Opcode.POP_A(Extended=False)
Opcode.POP_B(Extended=False)
Opcode.POP_C(Extended=False)
Opcode.POP_D(Extended=False)
Opcode.POP_X(Extended=False)
Opcode.POP_Y(Extended=False)
Opcode.CMP_A_A(Extended=True)
Opcode.CMP_A_B(Extended=True)
Opcode.CMP_A_C(Extended=True)
Opcode.CMP_A_D(Extended=True)
Opcode.CMP_A_IMM(Extended=False)
Opcode.CMP_B_A(Extended=True)
Opcode.CMP_B_B(Extended=True)
Opcode.CMP_B_C(Extended=True)
Opcode.CMP_B_D(Extended=True)
Opcode.CMP_B_IMM(Extended=False)
Opcode.CMP_C_A(Extended=True)
Opcode.CMP_C_B(Extended=True)
Opcode.CMP_C_C(Extended=True)
Opcode.CMP_C_D(Extended=True)
Opcode.CMP_C_IMM(Extended=False)
Opcode.CMP_D_A(Extended=True)
Opcode.CMP_D_B(Extended=True)
Opcode.CMP_D_C(Extended=True)
Opcode.CMP_D_D(Extended=True)
Opcode.CMP_D_IMM(Extended=False)
Opcode.TST_A(Extended=True)
Opcode.TST_B(Extended=True)
Opcode.TST_C(Extended=True)
Opcode.TST_D(Extended=True)
Opcode.JSR_ABS(Extended=False)
Opcode.JSR_REL(Extended=False)
Opcode.JSR_X(Extended=True)
Opcode.JSR_Y(Extended=True)
Opcode.RTS(Extended=False)
Opcode.SWI(Extended=True)
Opcode.RTI(Extended=True)
Opcode.JMP_ABS(Extended=False)
Opcode.JMP_REL(Extended=False)
Opcode.JMP_X(Extended=True)
Opcode.JMP_Y(Extended=True)
Opcode.JO_ABS(Extended=False)
Opcode.JO_REL(Extended=False)
Opcode.JO_X(Extended=True)
Opcode.JO_Y(Extended=True)
Opcode.JNO_ABS(Extended=False)
Opcode.JNO_REL(Extended=False)
Opcode.JNO_X(Extended=True)
Opcode.JNO_Y(Extended=True)
Opcode.JS_ABS(Extended=False)
Opcode.JS_REL(Extended=False)
Opcode.JS_X(Extended=True)
Opcode.JS_Y(Extended=True)
Opcode.JNS_ABS(Extended=False)
Opcode.JNS_REL(Extended=False)
Opcode.JNS_X(Extended=True)
Opcode.JNS_Y(Extended=True)
Opcode.JE_ABS(Extended=False)
Opcode.JE_REL(Extended=False)
Opcode.JE_X(Extended=True)
Opcode.JE_Y(Extended=True)
Opcode.JNE_ABS(Extended=False)
Opcode.JNE_REL(Extended=False)
Opcode.JNE_X(Extended=True)
Opcode.JNE_Y(Extended=True)
Opcode.JC_ABS(Extended=False)
Opcode.JC_REL(Extended=False)
Opcode.JC_X(Extended=True)
Opcode.JC_Y(Extended=True)
Opcode.JNC_ABS(Extended=False)
Opcode.JNC_REL(Extended=False)
Opcode.JNC_X(Extended=True)
Opcode.JNC_Y(Extended=True)
Opcode.JBE_ABS(Extended=False)
Opcode.JBE_REL(Extended=False)
Opcode.JBE_X(Extended=True)
Opcode.JBE_Y(Extended=True)
Opcode.JA_ABS(Extended=False)
Opcode.JA_REL(Extended=False)
Opcode.JA_X(Extended=True)
Opcode.JA_Y(Extended=True)
Opcode.JL_ABS(Extended=False)
Opcode.JL_REL(Extended=False)
Opcode.JL_X(Extended=True)
Opcode.JL_Y(Extended=True)
Opcode.JGE_ABS(Extended=False)
Opcode.JGE_REL(Extended=False)
Opcode.JGE_X(Extended=True)
Opcode.JGE_Y(Extended=True)
Opcode.JLE_ABS(Extended=False)
Opcode.JLE_REL(Extended=False)
Opcode.JLE_X(Extended=True)
Opcode.JLE_Y(Extended=True)
Opcode.JG_ABS(Extended=False)
Opcode.JG_REL(Extended=False)
Opcode.JG_X(Extended=True)
Opcode.JG_Y(Extended=True)
