#!/usr/bin/env python

"""Example of the adapter pattern.

The Adapter Pattern is useful to either either map two different interfaces or
to just modify (wrap) an existing API.
"""

from datetime import datetime


class AnnoyingAPI(object):
    def method_with_annoying_arguments(self, month, date, year, minute, second):
        return str(month) + '/' + str(date) + '/' + str(year)


class AnnoyingAdapter(object):
    def __init__(self):
        self.annoying_api = AnnoyingAPI()

    def nicer_method(self, time_object):
        mo = time_object.month
        d = time_object.day
        y = time_object.year
        mi = time_object.minute
        s = time_object.second
        return self.annoying_api.method_with_annoying_arguments(mo, d, y, mi, s)


if __name__ == '__main__':
    adapter = AnnoyingAdapter()
    r = adapter.nicer_method(datetime.now())
    print(r)