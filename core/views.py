from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from core.classes.playlist import Playlist
import requests
from urllib.parse import urlencode
from .forms import SearchForm, AddMusicForm, PlaylistIdForm
from .models import AccessTokenScoped
import environ
from core.auth import auth, authScope, get_access_token_scoped

#Environ Settings
env = environ.Env()
environ.Env.read_env()

playlist_id = env.str('PLAYLIST_ID')

def index(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        if request.method == 'GET' and 'code' in request.GET: # verifica se o método é GET e se a requisição possui o parâmetro code
            code = request.GET['code']
            access_token = authScope(code)
            b = AccessTokenScoped(access_token_scoped=access_token) # Gera o token
            b.save() #salva no DB
        else:
            access_token = auth()
            
        form = PlaylistIdForm(request.POST or None)
        if str(request.method) == 'POST' :
            if form.is_valid():
                global playlist_id 
                playlist_id = form.cleaned_data['playlist_id']
                messages.success(request, f'Playlist {playlist_id} cadastrada com sucesso')

        # Cria variiável de contexto a ser enviada para o template
        context = {
            'form' : form,
            'logged': True
        }
        return render(request, 'index.html', context)  

#View inicial que mostra as músicas da playlist e dá as opções do sistema
def spotify(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        if request.method == 'GET' and 'code' in request.GET: # verifica se o método é GET e se a requisição possui o parâmetro code
            code = request.GET['code']
            access_token = authScope(code)
            b = AccessTokenScoped(access_token_scoped=access_token) # Gera o token
            b.save() #salva no DB
        else:
            access_token = auth()

        playlist = Playlist(access_token, playlist_id) # Instancia a playlist utilizando a classe Playlist

        # Cria variiável de contexto a ser enviada para o template
        context = {
            'playlist' : playlist,
            'logged': True
        }
        return render(request, 'spotify.html', context)

def reset_playlist(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        global playlist_id
        playlist_id = env.str('PLAYLIST_ID')
        messages.warning(request, f'Playlist {playlist_id} resetada com sucesso')

        form = PlaylistIdForm(request.POST or None)


        context = {
            'form' : form,
            'logged': True
        }
        return render(request, 'index.html', context)

#View about me
def contact(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
            context = {
            'logged' : False
        }
    else:
        context = {
            'logged' : True
        }
    return render(request, 'contact.html', context)

#View do form que pesquisa a música a ser adicionada à playlist
def search_item(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        form = SearchForm(request.POST or None)

        context = {
            'form' : form,
            'logged': True
        }

        return render(request, 'add_item_playlist.html', context)

#View que lista as músicas da pesquisa e adiciona à playlist
def add_item_playlist(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        form = SearchForm(request.POST or None)

        access_token = auth()

        if str(request.method) == 'POST' :
            if form.is_valid():
                track = form.cleaned_data['track']

            # PESQUISAR POR ARTISTA OU MUSICA COM QUERY
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            endpoint = "https://api.spotify.com/v1/search"
            data = urlencode({"q": track, "type": "track"})
            lookup_url = f"{endpoint}?{data}"
            r = requests.get(lookup_url, headers=headers)

            form = AddMusicForm(request.POST or None)

            context = {
                'result': r,
                'form': form,
                'logged': True
            }

        return render(request, 'add_item_playlist_2.html', context)

# Adiciona uma música na playlist
def add_success(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        latest_token = get_access_token_scoped()

        # SE O METODO FOR POST (ADICIONAR NOVA MÚSICA À PLAYLIST)
        if str(request.method) == 'POST':
            # Autenticando na API do Spotify
            track_id = request.POST.get('track_id')
            
            headers = {
                "Authorization": f"Bearer {latest_token}",
                "Content-Type": "application/json"
            }
            endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris=spotify:track:{track_id}"
            r = requests.post(endpoint, headers=headers)
            results_add_playlist = r.json()

            if r.status_code in range(200, 299):
                messages.success(request, 'Track cadastrada com sucesso')
                context = {
                    'r': results_add_playlist,
                    'logged': True
                }
                return render(request, 'add_success.html', context)
            else:
                messages.error(request, f'Algo de errado aconteceu. Você gerou o seu Token na página inicial? --- {r.text}')
                return render(request, 'add_success.html')

# Remove uma música da playlist
def del_success(request):
    if str(request.user) == 'AnonymousUser': #verifica se o usuário está logado no sistema
        return redirect('user_in')
    else:
        latest_token = get_access_token_scoped()

        # SE O METODO FOR DELETE (Deletar NOVA MÚSICA À PLAYLIST)
        if str(request.method) == 'POST':
            # Autenticando na API do Spotify
            track_id = request.POST.get('track_id')

            headers = {
                "Authorization": f"Bearer {latest_token}",
                "Content-Type": "application/json",
                "Accept" : "application/json"
            }

            data = '{"tracks":[{"uri":' +  f'"spotify:track:{track_id}"' + '}]}'
            endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            r = requests.delete(endpoint, data=data, headers=headers)
            results_del_playlist = r.json()

            if r.status_code in range(200, 299):
                messages.success(request, 'Track removida com sucesso')
                context = {
                    'r': results_del_playlist,
                    'logged': True
                }
                return render(request, 'del_success.html', context)
            else:
                messages.error(request, f'Algo de errado aconteceu. Você gerou o seu Token na página inicial? --- {r.text}')
                return render(request, 'del_success.html')

# Cadastra um usuário (sem permissão pro admin do django)
def add_user(request):
    if request.method == "POST":
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('index')
    else:
        form_user = UserCreationForm()
    return render(request, 'add_user.html', {'form_user': form_user})

# Loga usuário
def user_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

# Desloga usuário
def user_out(request):
    logout(request)
    return redirect('index')
