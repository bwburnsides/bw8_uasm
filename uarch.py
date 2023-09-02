from microassembler import Field, Bus


class LeftRegister(Field[3]):
    A = Field.encode()
    B = Field.encode()
    C = Field.encode()
    D = Field.encode()
    Temp = Field.encode()


class RightRegister(Field[3]):
    A = Field.encode()
    B = Field.encode()
    C = Field.encode()
    D = Field.encode()
    Temp = Field.encode()


class PointerSelect(Field[3]):
    ProgramCounter = Field.encode()
    StackPointer = Field.encode()
    XPointer = Field.encode()
    YPointer = Field.encode()
    Temp = Field.encode()
    NmiVector = Field.encode()
    IrqVector = Field.encode()
    SwiVector = Field.encode()


class RegisterWriteBack(Field[1]):
    AluResult = Field.encode()
    MemoryData = Field.encode()


class Bw8ControlBus(Bus[6]):
    LeftRegister = Bus.place()
    RightRegister = Bus.place()


class Bw8StateElements():
    Sequencer = Field[3]
    Opcode = Field[8]
    Extended: 5 = Field[1]
