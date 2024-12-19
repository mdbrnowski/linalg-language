# LinAlg Language

[![actions status](https://github.com/mdbrnowski/linalg-language/actions/workflows/test.yml/badge.svg)](https://github.com/mdbrnowski/linalg-language/actions)

> [!IMPORTANT]
> Python is known to be slow. This language has an interpreter *written in Python*. It will be *very* slow. Apart from providing a nice syntax for matrices and a handy semantic analyzer, it has absolutely nothing to offer; sorry about that.

## Installation

To install `uv`, please refer to the [official `uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/). Then simply clone this repository, enter the directory, run `uv sync`, and you're ready to go.

## Usage

To see all available commands, simply run `./main.py`.

I'm afraid you'll need to explore the language on your own, since I haven't had the time to write anything resembling proper documentation.

Here is a sample code snippet:

```
a = 0;
b = 1;
n = 10000;
while (a < n) {
    print a;
    temp = a;
    a = b;
    b += temp;
}
```

For more, you can browse [tests](./tests).
