pub enum KeywordKind {
    Include,
    Field,
    Bus,
    Step,
    OpcodeWidth,
    State,
    Opcode,
    MicroInstruction,
    Instruction,
    Define,
}

pub enum TokenKind {
    Keyword(KeywordKind),
    Identifier(String),
    LeftParen,
    RightParen,
    LeftBrace,
    RightBrace,
    LeftBracket,
    RightBracket,
    Integer(usize),
    Comma,
    SemiColon,
    Colon,
    Resolution,
    Dot,
}

struct TextPosition {
    absolute: usize,
    line: usize,
    column: usize,
}

struct Span {
    start: TextPosition,
    end: TextPosition,
}

pub struct Token {
    kind: TokenKind,
    span: Span,
}
