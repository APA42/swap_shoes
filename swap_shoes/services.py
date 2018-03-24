# -*- coding: utf-8 -*-

from swap_shoes import user, exceptions


class UserService(object):

    def __init__(self, user_repository):
        self._user_repository = user_repository

    def add(self, name, password, feet_size):
        if name is None:
            raise exceptions.UsernameCanNotBeNoneError()
        if len(name) == 0:
            raise exceptions.UsernameCanNotBeEmptyError()
        if self._user_repository.find_by_name(name) is not None:
            raise exceptions.UsernameAlreadyUsed()

        if feet_size < 1:
            raise exceptions.FeetSizeError('Feet Size have to be greater than 0')

        an_user = user.User(name, password, feet_size)
        self._user_repository.put(an_user)

    def users(self):
        return self._user_repository.find_all()
