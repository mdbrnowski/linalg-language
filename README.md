# LinAlg Language

[![actions status](https://github.com/mdbrnowski/linalg-language/actions/workflows/test.yml/badge.svg)](https://github.com/mdbrnowski/linalg-language/actions)

> [!IMPORTANT]
> Python is known to be slow. This language has an interpreter *written in Python*. It will be *very* slow. Apart from providing nice syntax for matrices and tensors, it has absolutely nothing to offer; sorry about that.

To see all available commands, simply run `./main.py`.

I'm afraid you'll need to explore the language on your own, since I haven't had the time to write anything resembling proper documentation.

Here is a sample of code:

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
