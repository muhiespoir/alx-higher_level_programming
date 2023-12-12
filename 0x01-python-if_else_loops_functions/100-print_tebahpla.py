#!/usr/bin/python3
for n in reversed(range(ord("a"), ord("z") + 1)):
    if n % 2 != 0:
        n = n - 32
    print("{:c}".format(n), end="")
