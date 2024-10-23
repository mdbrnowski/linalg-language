#!/usr/bin/env python3
import typer
from antlr4 import *
from generated.MyLexer import MyLexer
from generated.MyParser import MyParser


def pretty_lexer(string: str):
    lexer = MyLexer(InputStream(string))

    for token in lexer.getAllTokens():
        token_name = lexer.ruleNames[token.type - 1]
        print(f'({token.line}): {token_name}({token.text})')


def pretty_parser(string: str):
    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))  # todo: pretty print


def main(action: str, filename: str):

    with open(filename, encoding='utf-8') as f:
        string = f.read()

    if action == 'lexer':
        pretty_lexer(string)
    elif action == 'parser':
        pretty_parser(string)
    else:
        print('Invalid action')


if __name__ == '__main__':
    typer.run(main)
