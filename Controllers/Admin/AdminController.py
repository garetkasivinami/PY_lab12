from ApplicationContext import *
from .BaseAdminController import *
from Entities.User import User
from Models.LoginModel import LoginModel

admin_users = {
    'main': 'mainadmin',
    'demoadmin': 'demoadmin'
}

@app.route(default_parameters['admin_index_action'], methods=['GET', 'POST'])
@AdminAuthorized()
def Admin_Index():
    users = UserApi.get_users()
    return render_admin('Home', { 'users': users, 'user_count': len(users) } )

@app.route(default_parameters['admin_login_action'], methods=['GET', 'POST'])
def Admin_Login():
    form = LoginModel()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        if login in admin_users and admin_users[login] == password:
            AdminApi.login()
            return redirect_to_admin_index()

    return render_admin('Login', { 'fields': form })

@app.route(default_parameters['admin_logout_action'], methods=['GET'])
def Admin_Logout():
    AdminApi.logout()
    return redirect_to_admin_index()

@app.route(default_parameters['admin_delete_user_action_params'], methods=['GET'])
@AdminAuthorized()
def DeleteUser(id):
    user = UserApi.get_user(id)
    if not user == None:
        UserApi.delete_user(user)
    return redirect_to_admin_index()