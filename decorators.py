def outer(fun):
    def inner():
        print "before function"
        ret = fun()
        return ret + 1
    return inner


def foo():
    return 1

decorated = outer(foo) # decorated version of foo
print decorated()

foo = outer(foo) # any calls to foo() won't get the original foo, they get decotated version



@outer     # bar = outer(bar)  predecorating the function
def bar():
    return 2
print bar()
