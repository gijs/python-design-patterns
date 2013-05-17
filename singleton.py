#!/usr/bin/env python

"""Example of the singleton pattern.

Often used as a manager class, so you only want a single instance, it is
likely needed to be used by many objects and rather then passing around
references, you can just keep "instantiating" it.
"""

class Singleton(object):
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


if __name__ == '__main__':
    s1=Singleton()
    s2=Singleton()
    if(id(s1)==id(s2)):
        print "Same"
    else:
        print "Different"