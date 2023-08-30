# `bw8` Microassembler
A microassembler for the BW8 instruction set which produces the microprogram for the BW8 8-bit homebrew CPU.

##

### File Inclusion
Additional files can be into the microassembly program as shown below. This is similar to C-like `#include` expansion - so ordering matters - but files will not be included more than once.

```
@include "opcodes.uasm"
```

### Named Field
Defines the enumerated decodings of an *n*-bit wide encoded bit field. In this case, a 2-bit field that encodes one of either `A`, `B`, `C`, or `D`.

```
field(2) LeftRegisterSelect {
    A, B, C, D
}
```

- Enumerated values begin with `0` and increment sequentially.
- More than 2<sup>*n*</sup> decodings is an assembly-time semantic error.
- Enumerated values can be accessed anonymously using subscripting:

```
LeftRegisterSelect[0] == LeftRegisterSelect::A
```

### Anonymous Field
Fields can be defined anonymously. That is, the decoded values are not named.

```
field(2) Foo;
```

- Just as above, field values can be accessed with subscripting.

### Control Bus
Defines the width and layout of an *n*-bit wide control bus, which is the output format of any microinstruction in the microprogram.

```
bus(4) {
    LeftRegisterSelect, RightRegisterSelect
}
```

- Bus layout is defined from the least significant bit towards the most significant bit, and layout is determined by ordering of the bus members.
- That is, `LeftRegisterSelect` represents bit 0 and bit 1, whereas `RightRegisterSelect` represents bit 2 and bit 3.
- For an *n*-bit wide bus definition, the sum width of all included fields must be *n*. Otherwise, it is an assembly-time semantic error.

### Step Count
Defines the *n*-bit width of the sequencer, where 2<sup>*n*</sup> represents the maximum number of clock cycles consumed by the execution of a single opcode.

```
step(3);
```

### Opcode Width
Defines the width of opcodes in the target instruction set.

```
opcodewidth(8);
```

### State Inputs
Defines additional bit fields on the control unit state input. The format of the state input is assumed to be (from LSb to MSb) `step`, then `opcode`, then the fields specified here in order of their inclusion.

```
state(12) {
    Extended,
}
```

### Opcode Declaration

Declares an opcode alongside other required state input values.

```
opcode MovAtoB { Extended: True }
```

- There may not be more than 2<sup>*opcodewidth*</sup> opcode declarations. Otherwise, it is an assembly-time semantic error.

### Named Microinstruction
Defines a microinstruction; a concrete control bus value.

```
microinstruction Fetch {
    LeftRegisterSelect: A,
    RightRegisterSelect: B,
    ...
}
```

- Microinstructions must include values for all fields included in the `bus` declaration. Otherwise, it is an assembly-time semantic error.
- NOTE: Or, omitted fields will be set to the 0-value for each.

### Anonymous Microinstruction
Microinstructions can also be defined anonymously, which can be used to define bus values inline.

```
microinstruction {
    LeftRegisterSelect: A,
    RightRegisterSelect: B,
}
```

### Instruction
Defines an instruction, which is a set of microinstructions in the larger microprogram that represent all operations needed to execute a particular opcode.

```
instruction Foo {
    Fetch,
    microinstruction {
        ...
    },
    End,
}
```

- The order of the microinstructions maps to the sequencer values from 0 to (2<sup>*n*</sup> - 1).
- Greater than 2<sup>*n*</sup> microinstructions is an assembly-time semantic error.

#### Specialization
Microinstructions can be modified inline in the context of a *instruction* definition to override the set values for that usage. This is done by appending a `.` and a valid field name to any microinstruction. The specific field encoding is represented as a name or integer in parenthesis following the field. These can be dot-chained.

```
instruction Bar {
    WhateverUop.LeftRegisterSelect(A),
    AnotherUop.LeftRegisterSelect(B).RightRegisterSelect(C),
}
```

#### Parameterization
Instructions can be parameterized, such that particular field values must be specified at the usage-site.

```
instruction Baz(param1, param2) {
    WhateverUop
        .LeftRegisterSelect(param1)
        .RightRegisterSelect(param2)
}
```

- Provided parameters must have types consistent with the specialization they are used in. Otherwise, it is an assembly-time semantic error.

### Opcode Definition
Defines the microinstruction for a specific opcode.

```
define MoveAtoB = Move(SelectRegisterLeft.A, SelectRegisterRight.B);
define MoveBtoA = Move(SelectRegisterLeft.B, SelectRegisterRight.A);
```

All declared opcodes must be defined. Otherwise it is an assembly-time semantic error.
