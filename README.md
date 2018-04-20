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
