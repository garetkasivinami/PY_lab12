from ApplicationContext import *
from RepositoryContext import *

class AlbumApi:
    _albumRepository = albumRepository

    @staticmethod
    def get_albums():
        return AlbumApi._albumRepository.GetAll()

    @staticmethod
    def get_album(id):
        return AlbumApi._albumRepository.Get(id)

    @staticmethod
    def add_album(entity):
        return AlbumApi._albumRepository.Add(entity)

    @staticmethod
    def update_album(entity):
        return AlbumApi._albumRepository.Update(entity)

    @staticmethod
    def delete_album(entity):
        return AlbumApi._albumRepository.Remove(entity)