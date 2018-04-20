#!/usr/bin/env python3
"""
# Returns
## Optional type enforcement for python with a more 'readable' syntax
---
Returns lets you declare what you are expecting to be returned from a function with a simple decorator.

I'm aware that python already has type hints. I'm also aware that it's probably better than this.

```python
@returns(some_class(), error_msg="fancier than default", warnonly=True)
def some_function():
    #do stuff
    return some_val_of_type_some_class
```
---
some_class(): any class you wish to enforce is returned from the function.
error_msg: a simple error_msg to replace the default
warnonly: if set to false a TypeError is raised


Written on a whim and with questionable style choices by Eli McRae.

"""
def returns(the_type_you_expect, error_msg="", warnonly=False):
    def inner_decorator(orig_function):
        def wrapper(*args, **kwargs):
            res = orig_function(*args, **kwargs)
            if type(res) != type(the_type_you_expect):
                nonlocal error_msg # because we're assigning...
                if error_msg == "":
                    error_msg = f"You're expecting a {type(the_type_you_expect)} rather than a {type(res)} to be returned from function named {orig_function.__name__}."
                print(error_msg)
                if warnonly == False:
                    raise TypeError
            return res
        return wrapper
    return inner_decorator


@returns(int())
def f1():
    print("1: int")
    return 1


@returns(None, error_msg="red alert!", warnonly=True)
def f2():
    print('2: None')
    return 1


@returns(bytes())
def f3():
    print("3: bytes")
    return bytes("asdf", 'utf8')


@returns(str())
def f4():
    print("4: string")
    return "asdf"


@returns(set(), warnonly=True)
def f5():
    print("5: returning string but expecting set")
    return "asdf"


@returns(list(), warnonly=True)
def f6():
    print("6: list")
    return ['a','b']

print(type(f1()))
print(type(f2()))
print(type(f3()))
print(type(f4()))
print(type(f5()))
print(type(f6()))
