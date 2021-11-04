from .models import AccessTokenScoped
import requests
import base64
import environ

#Environ Settings
env = environ.Env()
environ.Env.read_env()

CLIENT_ID = env.str('CLIENT_ID')
CLIENT_SECRET = env.str('CLIENT_SECRET')
REDIRECT_URI = env.str('REDIRECT_URI')

def authScope(code):

    # Credenciais do APP
    global CLIENT_ID, CLIENT_SECRET
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # Consulta o token para uso posterior
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        "grant_type": "authorization_code",
        "code": f"{code}",
        "redirect_uri": f"{REDIRECT_URI}"
    }
    token_headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"  # base64 encoded
    }

    # Requisição para o endpoint api/token
    r = requests.post(token_url, data=token_data, headers=token_headers)

    valid_request = r.status_code in range(200, 299)

    # Token de Acesso
    if valid_request:
        token_response_data = r.json()
        access_token = token_response_data['access_token']
        return access_token
    else:
        print(f'Erro: {r} --- {r.text}')

def auth():

    # Credenciais do APP
    global CLIENT_ID, CLIENT_SECRET
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode())


    # Consulta o token para uso posterior
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        "grant_type": "client_credentials"
    }
    token_headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"  # base64 encoded
    }

    # Requisição para o endpoint api/token
    r = requests.post(token_url, data=token_data, headers=token_headers)

    valid_request = r.status_code in range(200, 299)

    # Token de Acesso
    if valid_request:
        token_response_data = r.json()
        access_token = token_response_data['access_token']
        return access_token

def get_access_token_scoped():
    access_token_scoped = AccessTokenScoped.objects.last()
    return access_token_scoped