#4.8.8. Function Annotations

def f(ham: str, eggs: str = 'eggs') -> str:

    print("Annotations:", f.__annotations__)

    print("Arguments:", ham, eggs)

    return ham + ' and ' + eggs


f('spam')


#4.9. Intermezzo: Coding Style

#functions finish