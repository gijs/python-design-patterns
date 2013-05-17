#!/usr/bin/env python

"""Examples of the observer pattern.

Watch for changes in an object(s). Basically, sub/pub.
"""

class ObjectOfInterest(object):
    def __init__(self):
        self.observers = []
        self._name = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name
        self._update_observers()

    name = property(_get_name, _set_name)

    def _update_observers(self):
        for observer in self.observers:
            observer.update()

class Observer(object):
    def __init__(self, thing_to_watch):
        self.thing_to_watch = thing_to_watch
        self.thing_to_watch.register_observer(self)

    def update(self):
        print("updated.")

thing_to_watch = ObjectOfInterest()
observer = Observer(thing_to_watch)

print(thing_to_watch.name) # None

thing_to_watch.name = 'Bilbo' # updated.
print(thing_to_watch.name) # Bilbo

thing_to_watch.name = 'Frodo' # updated.
print(thing_to_watch.name) # Frodo


# =============================================================================
if __name__ == '__main__':
    pass