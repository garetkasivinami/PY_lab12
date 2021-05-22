from ..BaseController import *
from Helper import SetAdminViewsFolder
from .Parameters import default_parameters
from Api.AdminApi import AdminApi

def render_admin(template, model={}, general_template_name='General', **fargs):
    template = SetAdminViewsFolder(template)
    general_template_name = SetAdminViewsFolder(general_template_name)
    return render(template, model=model, general_template_name=general_template_name, additional_parameters=default_parameters, **fargs)

def redirect_to_admin_index(code=301):
    return redirect(default_parameters['admin_index_action'], code)

def AdminAuthorized():
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not 'is_admin_authorized' in session or not session['is_admin_authorized'] == True:
                return redirect(default_parameters['admin_login_action'])
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator