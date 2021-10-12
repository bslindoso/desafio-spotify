import requests
class Playlist():
    def __init__(self, access_token, playlist_id):
   
        # Faz uma requisição para a API do Spotify consultando as informações da playlist
        results_playlist = self.__get_playlist(access_token, playlist_id)

        self.__id = results_playlist["id"]
        self.__name = results_playlist["name"]
        self.__images = results_playlist["images"]
        self.__cover = self.__images[0]
        self.__cover_url = self.__cover['url']
        self.__tracks = results_playlist['tracks']
        self.__items = self.__tracks['items']
        self.__links = results_playlist['external_urls']
        self.__link_spotify = self.__links['spotify']

    # Faz uma requisição para a API do Spotify consultando as informações da playlist
    def __get_playlist(self, access_token, playlist_id):
        headers = {"Authorization": f"Bearer {access_token}"} # Monta o cabeçalho da reuqisição
        endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}" # Monta a URI da requisição
        r = requests.get(endpoint, headers=headers)
        results_playlist = r.json()
        return results_playlist

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_cover_url(self):
        return self.__cover_url

    def get_link_spotify(self):
        return self.__link_spotify
    
    def get_items(self):
        return self.__items