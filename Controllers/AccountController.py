from ApplicationContext import *
from .BaseController import *
from Entities.User import User
from Models.LoginModel import LoginModel
from Models.RegisterModel import RegisterModel
from Helper import *

@app.route(default_parameters['login_action'], methods=['GET', 'POST'])
def Login():
    form = LoginModel()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        user = UserApi.get_user_by_login_data(login, password)
        if not user == None:
            print(f'User logined: {user.Login}')
            result = redirect_to_index()
            UserApi.login(user, result)
            return result

    return render('Login', { 'fields': form })

@app.route(default_parameters['register_action'], methods=['GET', 'POST'])
def Register():
    form = RegisterModel()
    if form.validate_on_submit():
        username = form.username.data
        login = form.login.data
        password = form.password.data
        if UserApi.get_user_by_login(login) == None:
            passwordData = HashPassword(password)
            user = User(login, passwordData[0], passwordData[1], username)
            UserApi.add_user(user)
            result = redirect_to_index()
            UserApi.login(user, result)
            return result
        else:
            form.login.errors.append('123')

    return render('Register', { 'fields': form })

@app.route('/delete-user')
@Authorized()
def DeleteCurrentUser():
    user = get_user_context()['active_user']
    UserApi.delete_user(user)
    return redirect_to_index()

@app.route(default_parameters['logout_action'])
def Logout():
    result = redirect_to_index()
    UserApi.logout(result)
    return result