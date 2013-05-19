#!/usr/bin/env python

"""Example of the Command Pattern.

The Command Pattern provides a command object to act as an abstraction between
the object that does the work and probably manages its own state and the
objects that invoke that work.

This is the controller in the MVC pattern.
"""


class Doc(object):
    """I am the model in MVC"""

    def __init__(self, filename):
        self.filename = filename

    def save(self):
        print('Saved!')


class KeyboardShortcut(object):
    """I am the View in MVC"""

    def keypress(self):
        self.command()


class SaveCommand(object):
    """I am the controller of MVC.

    Command Object. I act as a buffer between the invoking object
    and the document. The invoker (keypress, toolbar button, etc)
    doesn't need to know anything about the document.
    """

    def __init__(self, doc):
        self.doc = doc

    def __call__(self):
        self.doc.save()


if __name__ == '__main__':
    doc = Doc('xxx.txt')
    save_cmd = SaveCommand(doc)

    shortcut = KeyboardShortcut()
    shortcut.command = save_cmd

    shortcut.keypress()