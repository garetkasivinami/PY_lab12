from ApplicationContext import *
from .BaseController import *
from Entities.Album import Album
from Models.CreateAlbumModel import CreateAlbumModel
from Models.EditAlbumModel import EditAlbumModel

@app.route(default_parameters['create_album_action'], methods=['GET', 'POST'])
@Authorized()
def CreateAlbum():
    form = CreateAlbumModel()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        year = form.year.data
        countOfTracks = form.countOfTracks.data
        imageUrl = form.imageUrl.data
        album = Album(name, description, year, countOfTracks, imageUrl)
        AlbumApi.add_album(album)
        return redirect_to_index()
    return render('CreateAlbum', { 'fields': form })

@app.route(default_parameters['update_album_action_params'], methods=['GET', 'POST'])
@Authorized()
def UpdateAlbum(id):
    form = EditAlbumModel()
    originalalbum = AlbumApi.get_album(id)
    if originalalbum == None:
        return redirect_to_index()
    if form.validate_on_submit():
        originalalbum.Name = form.name.data
        originalalbum.Description = form.description.data
        originalalbum.Year = form.year.data
        originalalbum.СountOfTracks = form.countOfTracks.data
        originalalbum.ImageUrl = form.imageUrl.data
        AlbumApi.update_album(originalalbum)
        return redirect_to_index()
    else:
        form.name.data = originalalbum.Name
        form.description.data = originalalbum.Description
        form.year.data = originalalbum.Year
        form.countOfTracks.data = originalalbum.CountOfTracks
        form.id.data = originalalbum.Id
        form.imageUrl.data = originalalbum.ImageUrl
    return render('EditAlbum', { 'fields': form })


@app.route(default_parameters['delete_album_action_params'], methods=['GET', 'POST'])
@Authorized()
def DeleteAlbum(id):
    originalalbum = AlbumApi.get_album(id)
    if originalalbum == None:
        return redirect_to_index()
    AlbumApi.delete_album(originalalbum)
    return redirect_to_index()

@app.route(default_parameters['details_album_action_params'], methods=['GET'])
def Details(id):
    album = AlbumApi.get_album(id)
    if album == None:
        return redirect_to_index()

    return render('DetailsAlbum', {'album': album })