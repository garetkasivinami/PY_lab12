from flask import Flask, render_template, redirect as f_redirect, make_response, session, abort
from ApplicationContext import *
from Helper import CreateTemplateFileName
from Api.UserApi import UserApi
from Api.AlbumApi import AlbumApi
from .Parameters import default_parameters, styles, scripts

import re
html_tags_regex = re.compile(r'<[^>]+>')

def render(template, model={}, general_template_name='General', headers = {}, styles=styles, scripts=scripts, additional_parameters={}, **fargs):
    template = CreateTemplateFileName(template)
    general_template_name = CreateTemplateFileName(general_template_name)
    user_context = get_user_context()
    page = render_template(template, **model, **default_parameters, **user_context, general_template_name=general_template_name, **additional_parameters, styles=styles, scripts=scripts, **fargs)

    if not 'Content-Type' in headers:
        headers['Content-Type'] = 'text/html'
    
    page = page.replace('\ufeff', '')
    return make_response(page, 200, headers)

def redirect(relative_url, code=301):
    return f_redirect(relative_url, code=code)

def redirect_to_index(code=301):
    return redirect(default_parameters['index_action'], code)
    
def Authorized():
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = get_user_context()
            if not context['is_authorized']:
                return redirect(default_parameters['register_action'])
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

def get_user_context():
    token = request.cookies.get('account_token')
    active_user = UserApi.get_user_by_token(token)
    is_authorized = not active_user == None
    return {
            'active_user': active_user,
            'is_authorized': is_authorized
        }