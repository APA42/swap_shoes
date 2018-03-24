# -*- coding: utf-8 -*-

from swap_shoes import user, exceptions


class UserService(object):

    def __init__(self, user_repository):
        self._user_repository = user_repository

    def add(self, name, password):
        if name is None:
            raise exceptions.UsernameCanNotBeNoneError()
        if len(name) == 0:
            raise exceptions.UsernameCanNotBeEmptyError()
        if self._user_repository.find_by_name(name) is not None:
            raise exceptions.UsernameAlreadyUsed()

        an_user = user.User(name, password)
        self._user_repository.put(an_user)

    def users(self):
        return self._user_repository.find_all()
