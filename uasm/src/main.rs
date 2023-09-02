#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![warn(unused_must_use)]

mod uasm;

fn main() {
    let source_name = String::from("../bw8_microassembly/bw8.uasm");
    let tokens = uasm::lex::tokenize(source_name);

    println!("Hello, world!");
}
