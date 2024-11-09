#!/usr/bin/env python3
import typer
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.MyLexer import MyLexer
from generated.MyParser import MyParser
from ast_listener import ASTListener

app = typer.Typer(no_args_is_help=True)


@app.command()
def lex(filename: str):
    """Lexical analysis"""
    with open(filename, encoding="utf-8") as f:
        string = f.read()

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


@app.command()
def parse(filename: str):
    """Syntactic analysis"""
    with open(filename, encoding="utf-8") as f:
        string = f.read()

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    parser.program()


@app.command()
def ast(filename: str):
    """Abstract syntax tree"""
    with open(filename, encoding="utf-8") as f:
        string = f.read()

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() == 0:
        listener = ASTListener()
        ParseTreeWalker().walk(listener, tree)


if __name__ == "__main__":
    app()
