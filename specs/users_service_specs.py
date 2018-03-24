# -*- coding: utf-8 -*-

from mamba import description, context, it, before
from expects import expect, equal, raise_error

from swap_shoes import repositories, services, exceptions

AN_USER_NAME = 'an_user_name'
AN_USER_PASSWORD = 'an_user_password'


with description('User Service') as self:
    with before.each:
        self.user_repository = repositories.UsersInMemoryRepository()
        self.user_service = services.UserService(self.user_repository)

    with context('adding a new user'):
        with context('everything is ok (happy path)'):
            with it('creates a new user at the system'):
                self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD)

                result = self.user_service.users()
                expect(len(result)).to(equal(1))

        with context('when user name already exits'):
            with it('raises UsernameAlreadyUsed Error'):
                self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD)

                def add_user_with_name_already_used():
                    self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD)

                expect(add_user_with_name_already_used).to(raise_error(exceptions.UsernameAlreadyUsed))

        with context('when validating mandatory fields'):
            with context('validating name field'):
                with context('when the name is not provided'):
                    with it('raises UsernameCanNotBeNoneError'):
                        def add_user_without_name():
                            self.user_service.add(None, AN_USER_PASSWORD)

                        expect(add_user_without_name).to(raise_error(exceptions.UsernameCanNotBeNoneError))

                with context('when the name is \'\''):
                    with it('raises UsernameCanNotBeEmptyError'):
                        def add_user_with_empty_name():
                            self.user_service.add('', AN_USER_PASSWORD)

                        expect(add_user_with_empty_name).to(raise_error(exceptions.UsernameCanNotBeEmptyError))
