from RepositoryContext import *
from Entities.User import User
from Helper import *

class UserApi:
    _userRepository = userRepository

    @staticmethod
    def get_users():
        return UserApi._userRepository.GetAll()

    @staticmethod
    def get_user(id):
        return UserApi._userRepository.Get(id)

    @staticmethod
    def add_user(user):
        UserApi._userRepository.Add(user)

    @staticmethod
    def delete_user(user):
        UserApi._userRepository.Remove(user)

    @staticmethod
    def get_user_by_token(token):
        if token == None:
            return None

        result = UserApi._userRepository.Where(lambda x: x.GetToken() == token)
        if len(result) == 0:
            return None
        return result[0]

    @staticmethod
    def get_user_by_login(login):
        result = UserApi._userRepository.Where(lambda x: x.Login == login)
        if len(result) == 0:
            return None
        return result[0]

    @staticmethod
    def get_user_by_login_data(login, password):
        user = UserApi.get_user_by_login(login)
        if user == None:
            return None
        hashedPassword = HashPasswordWithSalt(password, user.Salt)
        if not user.Password == hashedPassword:
            return None
        return user

    @staticmethod
    def login(user, response):
        response.set_cookie('account_token', user.GetToken())

    @staticmethod
    def logout(response):
        response.set_cookie('account_token', '', expires=0)