#!/usr/bin/env python3
import typer
from antlr4 import *
from generated.MyLexer import MyLexer
from generated.MyParser import MyParser


def pretty_lexer(string: str):
    lexer = MyLexer(InputStream(string))

    for token in lexer.getAllTokens():
        token_name = lexer.ruleNames[token.type - 1]
        print(f"({token.line}): {token_name}({token.text})")


def _print_tree(node, parser, level=0):
    if node.getChildCount() == 0:
        print(" | " * level + str(node))
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(" | " * level + rule_name)
        for i in range(node.getChildCount()):
            _print_tree(node.getChild(i), parser, level + 1)


def pretty_parser(string: str):
    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    _print_tree(tree, parser)


def main(action: str, filename: str):

    with open(filename, encoding="utf-8") as f:
        string = f.read()

    if action == "lexer":
        pretty_lexer(string)
    elif action == "parser":
        pretty_parser(string)
    else:
        print("Invalid action")


if __name__ == "__main__":
    typer.run(main)
