#!/usr/bin/env python3
from antlr4 import *
from generated.MyLexer import MyLexer
from generated.MyParser import MyParser


def pretty_lexer(file: str):
    with open(file, encoding='utf-8') as f:
        string = f.read()

    lexer = MyLexer(InputStream(string))

    for token in lexer.getAllTokens():
        token_name = lexer.ruleNames[token.type - 1]
        print(f'({token.line}): {token_name}({token.text})')

def pretty_parser(file: str):
    with open(file, encoding='utf-8') as f:
        string = f.read()

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    # pretty_lexer('example.txt')
    pretty_parser('example3.txt')
