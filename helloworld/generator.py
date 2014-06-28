__author__ = 'satish'
# fill in this function
def fib():
    a = 0
    b = 1
    for i in xrange(10):
        a, b = b, a + b
        yield b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 10:
            break
