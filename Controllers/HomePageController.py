from ApplicationContext import *
from .BaseController import *
from Entities.User import User

@app.route(default_parameters['index_action'])
def Index():
    albums = AlbumApi.get_albums()
    for item in albums:
        item.Description = html_tags_regex.sub('', item.Description)
    return render('Home', {'albums': albums })

@app.route('/users')
def Users():
    return ', '.join(x.UserName for x in UserApi.get_users())