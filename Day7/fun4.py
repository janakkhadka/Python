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
pos_only_arg(12) #cannot write arg=12



