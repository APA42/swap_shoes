# -*- coding: utf-8 -*-


from common.factory import Factory

from swap_shoes import repositories, services


def _in_memory_user_repository():
    return Factory.instance('_in_memory_user_repository',
                            lambda: repositories.UsersInMemoryRepository()
                            )


def user_service():
    return Factory.instance('user_service',
                            lambda: services.UserService(_in_memory_user_repository())
                            )