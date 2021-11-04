from django import forms

class SearchForm(forms.Form):
    track = forms.CharField(label='Nome da Música')

class AddMusicForm(forms.Form):
    add_track_id = forms.CharField(label='Id da Música', widget=forms.HiddenInput())

class PlaylistIdForm(forms.Form):
    playlist_id = forms.CharField(label='Playlist ID')