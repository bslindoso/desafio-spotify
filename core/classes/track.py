class Track:
    def __init__(self, item):
        self.__track_id = item['track']['id']
        self.__name = item['track']['name']
        self.__spotify_url = item['track']['external_urls']['spotify']
        self.__artist_name = item['track']['artists'][0]['name']
        self.__album = item['track']['album']['name']

    @property
    def id(self):
        return self.__track_id

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__spotify_url

    @property
    def artist_name(self):
        return self.__artist_name

    @property
    def album(self):
        return self.__album