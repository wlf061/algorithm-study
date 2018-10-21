import sys

def f123():
    print("test first")
    yield 1
    yield 2
    yield 3

for item in f123():
    print(item)