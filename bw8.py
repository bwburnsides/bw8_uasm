import microassembler as uasm


class LeftRegister(uasm.Field[2]):
    A = uasm.Field.encode()
    B = uasm.Field.encode()
    C = uasm.Field.encode()
    D = uasm.Field.encode()


class RightRegister(uasm.Field[2]):
    A = uasm.Field.encode()
    B = uasm.Field.encode()
    C = uasm.Field.encode()
    D = uasm.Field.encode()


uasm.Bus[32](LeftRegister, RightRegister)

FETCH = uasm.MicroInstruction(
    LeftRegister=LeftRegister.A,
    RightRegister=RightRegister.A,
)

print(FETCH)
print()

NewFetch = FETCH.LeftRegister(2).RightRegister(2)

print(NewFetch)
print()
print(FETCH)


# def Move8(dst, src):
#     return (
#         FETCH,
#         MicroInstruction(LeftRegister=LeftRegister.A, RightRegister=RightRegister.A)
#         .LeftRegister(dst)
#         .RightRegister(src),
#         FETCH,
#     )

# class Opcodes:
#     MoveAtoB = ...


# Opcodes.MoveAtoB = Move8(LeftRegister.B, RightRegister.A)
