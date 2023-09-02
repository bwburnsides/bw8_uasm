from microassembler import Field, Bus, Instruction, Opcode


class LeftRegister(Field[2]):
    A = Field.encode()
    B = Field.encode()
    C = Field.encode()
    D = Field.encode()


class RightRegister(Field[2]):
    A = Field.encode()
    B = Field.encode()
    C = Field.encode()
    D = Field.encode()


class BW8ControlBus(Bus[4]):
    LeftRegister = Bus.place()
    RightRegister = Bus.place()


FETCH = BW8ControlBus.MicroInstruction(
    LeftRegister=LeftRegister.A,
    RightRegister=RightRegister.A,
)


Opcode.MoveAtoB(Extended=False)


@Instruction
def Move8(dst, src):
    return (
        FETCH,
        BW8ControlBus.MicroInstruction(
            LeftRegister=LeftRegister.A, RightRegister=RightRegister.A
        )
        .LeftRegister(dst)
        .RightRegister(src),
        FETCH,
    )


Opcode.MoveAtoB = Move8(LeftRegister.B, RightRegister.A)
