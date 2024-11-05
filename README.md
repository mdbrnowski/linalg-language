# LinAlg Language

[![actions status](https://github.com/mdbrnowski/linalg-language/actions/workflows/test.yml/badge.svg)](https://github.com/mdbrnowski/linalg-language/actions)

To generate lexer and parser in Python, run

```bash
antlr4 -o generated -Dlanguage=Python3 MyLexer.g4
antlr4 -o generated -Dlanguage=Python3 MyParser.g4
```

To use lexer on `example.txt`, run

```bash
./main.py lex example.txt
```

To use parser on `example.txt`, run

```bash
./main.py parse example.txt
```
