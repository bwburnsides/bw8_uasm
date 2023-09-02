use std::fs;

pub enum LexError {
    UnexpectedEOF,
    UnexpectedCharacter,
}

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
    Integer(usize),

    LeftParen,
    RightParen,
    LeftBrace,
    RightBrace,
    LeftBracket,
    RightBracket,

    Comma,
    SemiColon,
    Colon,
    Dot,
    AtSign,
}

#[derive(Default)]
struct TextPosition {
    absolute: usize,
    line: usize,
    column: usize,
}

#[derive(Default)]
struct Span {
    start: TextPosition,
    end: TextPosition,
}

pub struct Token {
    kind: TokenKind,
    span: Span,
}

impl Token {
    pub fn new(kind: TokenKind) -> Self {
        Self {
            kind: kind,
            span: Span::default(),
        }
    }
}
pub struct Lexer {
    input: Vec<char>,         // Source code
    pub position: usize,      // Reading position
    pub read_position: usize, // Current moving reading position
    pub ch: char,             // Current read character
}

impl Lexer {
    fn new(data: Vec<char>) -> Self {
        return Self {
            input: data,
            position: 0,
            read_position: 0,
            ch: '\0', // TODO: Handle this better
        };
    }

    pub fn read_char(&self) -> Option<char> {
        match self.input.get(self.position) {
            // TODO: Cleaner way to dereference "inner type"
            Some(&c) => Some(c),
            None => None,
        }
    }

    pub fn next_token(&self) -> Result<Token, LexError> {
        let token_kind: TokenKind = match self.read_char() {
            None => return Err(LexError::UnexpectedEOF),
            Some(c) => match c {
                ',' => TokenKind::Comma,
                ';' => TokenKind::SemiColon,
                ':' => TokenKind::Colon,
                '.' => TokenKind::Dot,
                '@' => TokenKind::AtSign,
                '(' => TokenKind::LeftParen,
                ')' => TokenKind::RightParen,
                '{' => TokenKind::LeftBrace,
                '}' => TokenKind::RightBrace,
                '[' => TokenKind::LeftBracket,
                ']' => TokenKind::RightBracket,
                c if c.is_ascii_alphabetic() => self.next_keyword_or_identifer(),
                c if c.is_ascii_digit() => self.next_integer(),
                _ => return Err(LexError::UnexpectedCharacter),
            },
        };

        todo!()
    }

    pub fn next_keyword_or_identifer(&self) -> TokenKind {
        todo!()
    }

    pub fn next_integer(&self) -> TokenKind {
        todo!()
    }
}

pub fn tokenize(file_name: String) -> Vec<Token> {
    let contents: Vec<char> = fs::read_to_string(file_name)
        .expect("Failed to read in source file.")
        .chars()
        .collect();

    let mut lexer = Lexer::new(contents);
    let mut tokens: Vec<Token> = Vec::new();

    // loop {
    //     match lexer.next_token() {
    //         Some(token) => tokens.push(token),
    //         None => break,
    //     }
    // }

    todo!();
}
