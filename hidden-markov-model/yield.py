import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        print("test fibonacci")
        yield a
        print("test after yield")
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

for index in fibonacci(10):
    print(index)

#while True:
 #   try:
  #      print(next(f), end=" ")
   # except StopIteration:
    #    sys.exit()