#!/usr/bin/env python

"""Examples of template pattern

Provides an excellent means of keeping code DRY.
"""

# Base class with general, shared functionality
class QueryTemplate(object):
    def connect(self):
        pass
    # To be overridden with task-specific functionality.
    def construct_query(self):
        raise NotImplementedError()
    def do_query(self):
        pass
    def format_query(self):
        pass
    # To be overridden with task-specific functionality.
    def output_results(self):
        raise NotImplementedError

class UserQuery(QueryTemplate):
    def construct_query(self):
        # Override method with task-specific functionality.
        pass
    def output_results(self):
        # Override method with task-specific functionality.
        pass

class AnotherKindOfQuery(QueryTemplate):
    def construct_query(self):
        # Override method with task-specific functionality.
        pass
    def output_results(self):
        # Override method with task-specific functionality.
        pass

u = UserQuery()

u.construct_query() # Local, overridden logic
u.connect() # Generic, shared logic
u.do_query() # Generic, shared logic
u.format_query() # Generic, shared logic
u.output_results() # Local, overridden logic


# =============================================================================
if __name__ == '__main__':
    pass