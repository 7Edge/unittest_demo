#! /usr/bin/env python
# coding:utf-8


class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('%s not found %s attr!' % (self, item))

    def __setattr__(self, key, value):
        self[key] = value


