def add(a, b, *args):
    return a+b-sum(args)

print(add(5,6,1,1))
