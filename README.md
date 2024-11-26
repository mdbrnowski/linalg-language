# LinAlg Language

[![actions status](https://github.com/mdbrnowski/linalg-language/actions/workflows/test.yml/badge.svg)](https://github.com/mdbrnowski/linalg-language/actions)

To explore all available commands, simply run `./main.py`.

If you want to generate lexer and parser yourself (for some reason), run

```bash
antlr4 -o generated -Dlanguage=Python3 MyLexer.g4
antlr4 -o generated -Dlanguage=Python3 MyParser.g4
```
