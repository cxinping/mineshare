# -*- coding: utf-8 -*-

from random import randint
    
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
        
def random(n=13):
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))
