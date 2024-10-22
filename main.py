from antlr4 import *
from generated.MyLexer import MyLexer


with open('example.txt', encoding='utf-8') as f:
    string = f.read()

lexer = MyLexer(InputStream(string))

for token in lexer.getAllTokens():
    token_name = lexer.ruleNames[token.type - 1]
    print(f'({token.line}): {token_name}({token.text})')
