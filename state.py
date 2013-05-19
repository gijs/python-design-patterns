#!/usr/bin/env python

"""Example of the singleton pattern.

Allow an object to alter its behavior when its internal state changes. The
object will appear to change its class.
"""

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvqxyz'


class CharEval(object):
    def process(self, string, parser):
        """Updates state depending on first char of string"""
        first_letter = string[0].lower()
        # Set state depending on is first char is a vowel or consonant.
        if (first_letter in VOWELS):
            parser.state = Vowel()
        elif (first_letter in CONSONANTS):
            parser.state = Consonant()
        else:
            # Strip non alpha-characters
            string = string[1:]

        # Return string for for processing.
        return string


class Vowel(object):
    def process(self, string, parser):
        # Do state-specific functionality.
        print('Vowel: ' + string[0])
        # Update parser's state (to evaluate string further).
        parser.state = CharEval()
        # Return string sans first char for further processing.
        return string[1:]


class Consonant(object):
    def process(self, string, parser):
        # Do state-specific functionality.
        print('Consonant: ' + string[0])
        # Update parser's state (to evaluate string further).
        parser.state = CharEval()
        # Return string sans first char for further processing.
        return string[1:]


class Parser(object):
    """Main, manager-type class"""

    def __init__(self):
        # Set default state.
        self.state = CharEval()

    def process(self, string):
        # Process string via current state's process method.
        remaining = self.state.process(string, self)
        # If there's any string left, recursively call this method (with state updated
        # from the process method that was just called).
        if remaining:
            self.process(remaining)


if __name__ == '__main__':
    p = Parser()
    p.process('Zoe and Gambit are dogs')