#!/usr/bin/env python

"""Examples of template pattern

Provides an excellent means of keeping code DRY.
"""

# Base class with general, shared functionality
class QueryTemplate(object):
    def connect(self):
        print('Generic, shared logic')

        # To be overridden with task-specific functionality.
    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        print('Generic, shared logic')

    def format_query(self):
        print('Generic, shared logic')

        # To be overridden with task-specific functionality.
    def output_results(self):
        raise NotImplementedError


class UserQuery(QueryTemplate):
    def construct_query(self):
        # Override method with task-specific functionality.
        print('Specific logic')

    def output_results(self):
        # Override method with task-specific functionality.
        print('Specific logic')


class AnotherKindOfQuery(QueryTemplate):
    def construct_query(self):
        # Override method with task-specific functionality.
        print('Specific logic')

    def output_results(self):
        # Override method with task-specific functionality.
        print('Specific logic')


if __name__ == '__main__':
    u = UserQuery()
    u.construct_query() # Local, overridden logic
    u.connect() # Generic, shared logic
    u.do_query() # Generic, shared logic
    u.format_query() # Generic, shared logic
    u.output_results() # Local, overridden logic