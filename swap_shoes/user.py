# -*- coding: utf-8 -*-


class User(object):

    def __init__(self, name, password):
        self._name = name
        self._password = password

    @property
    def name(self):
        return self._name