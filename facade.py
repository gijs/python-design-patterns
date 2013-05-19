#!/usr/bin/env python


"""Example of the Facade Pattern.

Similar to the Adapter Pattern, the Facade Pattern is used to simplify
a system. The Adapter Patterns seeks to map two interfaces or simplify a
single thing.

A common task that might employ many classes and methods may be wrapped up
into a much simpler Facade Pattern.
"""


class Facade(object):
    def simple_task(self):
        # Tons of other classes and method calls.
        pass

    def another_simple_tasl(self):
        # Many more classes and method calls.
        pass