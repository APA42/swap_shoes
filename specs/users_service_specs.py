# -*- coding: utf-8 -*-

from mamba import description, context, it, before
from expects import expect, equal, raise_error, contain

from swap_shoes import repositories, services, exceptions

AN_USER_NAME = 'an_user_name'
AN_USER_PASSWORD = 'an_user_password'
A_VALID_FEET_SIZE = 42


with description('User Service') as self:
    with before.each:
        self.user_repository = repositories.UsersInMemoryRepository()
        self.user_service = services.UserService(self.user_repository)

    with context('adding a new user'):
        with context('everything is ok (happy path)'):
            with it('creates a new user at the system'):
                self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD, A_VALID_FEET_SIZE)

                result = self.user_service.users()
                expect(len(result)).to(equal(1))

        with context('when user name already exits'):
            with it('raises UsernameAlreadyUsed Error'):
                self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD, A_VALID_FEET_SIZE)

                def add_user_with_name_already_used():
                    self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD, A_VALID_FEET_SIZE)

                expect(add_user_with_name_already_used).to(raise_error(exceptions.UsernameAlreadyUsed))

        with context('when validating mandatory fields'):
            with context('validating name field'):
                with context('when the name is not provided'):
                    with it('raises UsernameCanNotBeNoneError'):
                        def add_user_without_name():
                            self.user_service.add(None, AN_USER_PASSWORD, A_VALID_FEET_SIZE)

                        expect(add_user_without_name).to(raise_error(exceptions.UsernameCanNotBeNoneError))

                with context('when the name is \'\''):
                    with it('raises UsernameCanNotBeEmptyError'):
                        def add_user_with_empty_name():
                            self.user_service.add('', AN_USER_PASSWORD, A_VALID_FEET_SIZE)

                        expect(add_user_with_empty_name).to(raise_error(exceptions.UsernameCanNotBeEmptyError))

            with context('validating size field'):
                with context('when the size is lower than 1'):
                    with it('raises FeetSizeError'):
                        def add_user_with_size_lower_than_1():
                            self.user_service.add(AN_USER_NAME, AN_USER_PASSWORD, 0)

                        expect(add_user_with_size_lower_than_1).to(raise_error(exceptions.FeetSizeError,
                                                                               contain('Feet Size have to be greater than 0')))
