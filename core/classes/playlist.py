import requests
from core.classes.track import Track

class Playlist():
    def __init__(self, access_token, playlist_id):
        # Faz uma requisição para a API do Spotify consultando as informações da playlist
        results_playlist = self.__get_playlist(access_token, playlist_id)

        self.__name = results_playlist["name"]
        self.__cover_url = results_playlist["images"][0]['url']
        self.__items = results_playlist['tracks']['items']
        self.__link_spotify = results_playlist['external_urls']['spotify']

        # Inicia a geração da tracklist
        self.__track_list = self.__create_track_list() 

    # Faz uma requisição para a API do Spotify consultando as informações da playlist
    def __get_playlist(self, access_token, playlist_id):
        headers = {"Authorization": f"Bearer {access_token}"} # Monta o cabeçalho da reuqisição
        endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}" # Monta a URI da requisição
        r = requests.get(endpoint, headers=headers)
        results_playlist = r.json()
        return results_playlist

    # Cria a track list da playlist com o retorno da requisição (self.__items)
    def __create_track_list(self):
        count = 0
        tracks = []
        for item in self.__items:
            tracks.append(Track(item))
            count += 1
        return tracks

    @property
    def name(self):
        return self.__name

    @property
    def cover_url(self):
        return self.__cover_url

    @property
    def link_spotify(self):
        return self.__link_spotify

    def __getitem__(self, item):
        return self.__track_list[item]