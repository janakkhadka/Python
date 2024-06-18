#4.8.6. Lambda Expressions

def make_incrementor(n):

    return lambda x: x + n

f = make_incrementor(42)

x=f(0)
print(x)