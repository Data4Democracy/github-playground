def gen_fibonacci():
    seed, next  = 0, 1
    while True:
        next, seed = seed, next + seed
        yield (next)

def main(n):
    for m in gen_fibonacci():
        if m < n:
            print(m, end=', ')
        else:
            break

main(1000)
