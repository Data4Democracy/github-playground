def gen_fibonacci():
    seed, next_  = 0, 1
    while True:
        next_, seed = seed, next_ + seed
        yield (next_)

def main(n):
    for m in gen_fibonacci():
        if m < n:
            print(m, end=', ')
        else:
            break

main(1000)
