# -*- coding: utf-8 -*-


class UsernameAlreadyUsed(Exception):
    pass


class UsernameCanNotBeNoneError(Exception):
    pass


class UsernameCanNotBeEmptyError(Exception):
    pass


class FeetSizeError(Exception):
    def __init__(self, exception_message):
        self._exception_message = exception_message

    def __str__(self):
        return self._exception_message
