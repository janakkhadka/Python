def fib(n):    # write Fibonacci series up to n

    """Print a Fibonacci series up to n."""

    a, b = 0, 1

    while a < n:

        print(a, end=' ')

        a, b = b, a+b

    print()


# Now call the function we just defined:

fib(2000)

#4.8.1 default argument values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('hello','janak','nepal')


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
        
ask_ok()