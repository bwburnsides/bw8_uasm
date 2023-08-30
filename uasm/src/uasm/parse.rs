struct Field {
    kind: String,
    value: String,
}

struct IncludeDeclaration {
    module_name: String,    
}

struct BitFieldDefinition {
    name: String,
    width: usize,
    names: Option<Vec<String>>,
}

struct StepSpecification {
    width: usize,
}

struct OpcodeWidthSpecification {
    width: usize,
}

struct StateDefinition {
    width: usize,
    names: Vec<String>,
}

struct OpcodeDeclaration {
    name: String,
    state_fields: Vec<Field>
}

struct MicroInstructionDefinition {
    name: Option<String>,
    control_fields: Vec<Field>,
}
