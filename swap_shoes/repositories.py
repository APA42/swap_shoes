# -*- coding: utf-8 -*-

import pickle


class UsersInMemoryRepository(object):

    def __init__(self):
        self._storage = {}

    def put(self, value):
        self._storage[self._key(value)] = self._serialize(value)

    def find_all(self):
        return list(map(self._deserialize, self._storage.values()))

    def find_by_name(self, name):
        entity = self._storage.get(name, None)
        if entity is not None:
            return self._deserialize(entity)
        return None

    def _key(self, value):
        return '{}'.format(value.name)

    def _serialize(self, value):
        return pickle.dumps(value)

    def _deserialize(self, value):
        return pickle.loads(value)
