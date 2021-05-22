from flask import session

class AdminApi:
    @staticmethod
    def login():
        session['is_admin_authorized'] = True

    @staticmethod
    def logout():
        session['is_admin_authorized'] = None