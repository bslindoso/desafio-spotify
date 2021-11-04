from requests.api import request
from core.views import index

def test_se_usuario_nao_esta_logado_entao_redireciona_para_o_login():
    request.user = "AnonymousUser"
    assert index(request) == 1