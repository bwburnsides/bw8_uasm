from microassembler import Instruction, Opcode
from uarch import Bw8ControlBus, LeftRegister, RightRegister

FETCH = Bw8ControlBus.MicroInstruction(
    LeftRegister=LeftRegister.A,
    RightRegister=RightRegister.A,
)


InstructionBase = Instruction(base=None)

Bw8Instruction = Instruction(
    base=lambda opcode: ExtendedBase if opcode.Extended else NormalBase
)


@InstructionBase
def NormalBase():
    return (FETCH,)


@InstructionBase
def ExtendedBase():
    return (FETCH, FETCH.SetExtension(True))


@Bw8Instruction
def Move8(dst, src):
    return (FETCH, Bw8ControlBus.MicroInstruction(LeftRegister=dst, RightRegister=src))


# Opcode Declaration
Opcode.MoveAtoB(Extended=True)

# Opcode Definition
Opcode.MoveAtoB = Move8(LeftRegister.B, LeftRegister.A)
