from microassembler import Field, Bus, Instruction, Opcodes


# Field[n] is a generic parent type that represents an n-bit wide field
# on a control bus. Its members are named representations of
# the encoded values in that field. Having more than 2^n members
# in a Field[n] is illegal and will result in the assembler exiting.
#
# Field members encode the values from 0 to 2^n - 1 in order of
# inclusion in the declaration.
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


# Bus[n] is a generic parent type that represents an n-bit wide
# control bus composed of smaller control fields. The fields placed
# on it must be previously-defined Field[n] types. It is illegal for
# the sum of the width of the fields on the bus to be greater than n
# on a Bus[n]. This will result in the assembler exiting.
#
# The positioning of the fields on the bus are defined beginning from the
# least significant bit, in order of the fields' inclusion in the declaration.
class BW8ControlBus(Bus[4]):
    LeftRegister = Bus.place()
    RightRegister = Bus.place()


# MicroInstructions are snapshots of a control bus, and represent its value
# at any specific time. As such, they are defined by specifying concrete field
# encodings for each field on the bus. Fields that are not provided default to
# the 0-encoding for that field.
FETCH = BW8ControlBus.MicroInstruction(
    LeftRegister=LeftRegister.A,
    RightRegister=RightRegister.A,
)


# Declare an opcode, as well as any other state information that it is dependent on.
# NOTE: Implement control state elements.
# Opcodes must later be defined by providing an instruction definition for each.
Opcodes.MoveAtoB(Extended=False)

# An instruction is a grouping of MicroInstructions. There are constraints put on the
# number of MicroInstructions per instruction which are enforced by the target microarchitecture.
# For example, if you have a 3-bit sequencer, then an instruction may only contain 8 microinstructions.
# TODO: Implement length-enforcement.
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

# Opcodes are defined by assigning an instruction to them. This tells the
# microassembler what microinstructions should be assembled for each opcode.
Opcodes.MoveAtoB = Move8(LeftRegister.B, RightRegister.A)
