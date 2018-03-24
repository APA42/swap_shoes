# -*- coding: utf-8 -*-


class User(object):

    def __init__(self, name, password, feet_size):
        self._name = name
        self._password = password
        self._feet_size = feet_size

    @property
    def name(self):
        return self._name

    def __str__(self):
        return 'name:{} feet_size:{}'.format(self._name, self._feet_size)
