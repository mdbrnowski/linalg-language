#!.venv/bin/python3
import typer
from rich.console import Console
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.MyLexer import MyLexer
from generated.MyParser import MyParser
from ast_listener import ASTListener
from semantic_listener import SemanticListener

app = typer.Typer(no_args_is_help=True)
err_console = Console(stderr=True)


def _read_code_from_file(filename: str) -> str:
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        err_console.print(f"[bold red]File '{filename}' not found")
        raise typer.Exit(code=1) from e


@app.command()
def lex(filename: str):
    """Lexical analysis"""
    string = _read_code_from_file(filename)

    lexer = MyLexer(InputStream(string))

    for token in lexer.getAllTokens():
        token_name = lexer.ruleNames[token.type - 1]
        print(f"({token.line}): {token_name}({token.text})")


@app.command()
def parse(filename: str):
    """Syntactic analysis"""
    string = _read_code_from_file(filename)

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    parser.program()


@app.command()
def ast(filename: str):
    """Abstract syntax tree"""
    string = _read_code_from_file(filename)

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() == 0:
        listener = ASTListener()
        ParseTreeWalker().walk(listener, tree)


@app.command()
def sem(filename: str):
    """Semantic analysis"""
    string = _read_code_from_file(filename)

    lexer = MyLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() == 0:
        listener = SemanticListener()
        ParseTreeWalker().walk(listener, tree)


if __name__ == "__main__":
    app()
