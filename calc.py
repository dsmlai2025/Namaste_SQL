def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    if a is None and b is None:
        return 0
    else:
        return a*b

def divide(a, b):
<<<<<<< HEAD
    return a/b
=======
    if b == 0:
        return "Division by 0 not possible"
    else:
        return a/b
>>>>>>> karthik-edits
