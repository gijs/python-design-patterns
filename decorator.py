#!/usr/bin/env python

"""Examples of the decorator pattern.

A decorator is just a wrapper. Here are some examples.
"""

# An example of wrapping an entire class. This way sucks though.
class Foo():
    def f1(self):
        print('f1 called')

    def f2(self, blurb):
        return blurb


class FooDecorator():
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print('Decorated f1')
        self._decoratee.f1()

    def f2(self, blurb):
        return self._decoratee.f2(blurb).upper()


f = Foo()
d = FooDecorator(f)

print( d.f1() ) # Decorated f1, f1 called
print( d.f2('not found') ) # NOT FOUND

# ======================================================================================================================

# This version is versatile. You don't need to create a duplicate method for every function you wish to decorate.
# However, you need to create another class for each "decoration" you with to do. So, in this example if you also
# wanted to have a decorator that divides by 2, you'd need to create a whole other class.
class DoubleDecorator():
    def __init__(self, f):
        self.f = f

    def __call__(self, a, b):
        # Actual decorator logic: just multiple the result of f(a, b) by 2.
        return self.f(a, b) * 2

# Set a decorator for this function
@DoubleDecorator
def aFunction(a, b):
    return a + b


print(aFunction(2, 3)) # 10

# Here's an example of what's actually happening with the @ syntax.

# Example function
def bFunction(a, b):
    return a + b

# This @DoubleDecorator syntax is sugar for doing this:
print( DoubleDecorator(bFunction).__call__(5, 5) ) # 20


class SquareDecorator():
    def __init__(self, f):
        self.f = f

    def __call__(self, a, b):
        result = self.f(a, b)
        print(result * result)
        # I'm not returning shit!


if __name__ == '__main__':
    @SquareDecorator # Then I'm called
    @DoubleDecorator # I get called first
    def cFunction(a, b):
        return a + b

    cFunction(1, 2) # 36, ((1+2)*2)^2
