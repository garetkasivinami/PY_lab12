from ApplicationContext import *
from .BaseController import *
from Entities.User import User

@app.route(default_parameters['index_action'])
def Index():
    albums = AlbumApi.get_albums()
    if not albums == None:
        albums.reverse()

    for item in albums:
        item.Description = html_tags_regex.sub('', item.Description)
    return render('Home', {'albums': albums })

@app.route(default_parameters['about_action'])
def About():
    return render('About')

@app.route(default_parameters['history_action'])
def History():
    return render('History')