def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
        
cheeseshop(12)

#4.8.3. Special parameters

def standard_arg(arg):

    print(arg)


def pos_only_arg(arg, /):

    print(arg)


def kwd_only_arg(*, arg):

    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):

    print(pos_only, standard, kwd_only)
    
    
standard_arg(arg=12)
standard_arg(12)

pos_only_arg(12) #cannot write arg=12

kwd_only_arg(arg=12) #must write as arg=12

combined_example(12,12,kwd_only=12)

def foo(name, /, **kwds):

    return 'name' in kwds


foo(1, **{'name': 2})


#4.8.5. Unpacking Argument Lists

list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]

args = [3, 6]

list(range(*args))


def parrot(voltage, state='a stiff', action='voom'):

    print("-- This parrot wouldn't", action, end=' ')

    print("if you put", voltage, "volts through it.", end=' ')

    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)


