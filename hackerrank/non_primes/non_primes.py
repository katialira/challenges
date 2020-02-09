def manipulate_generator(generator, n):
    a = n+1

    if a > 2:
        if all( a % i != 0 for i in range(2, n//2) ):
            next(g)
    else:
        next(g)
        next(g)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
