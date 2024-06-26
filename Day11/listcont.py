#5.1.3. List Comprehensions

squares = []

for x in range(10):

    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled

[x*2 for x in vec]