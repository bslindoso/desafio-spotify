from django.urls import path

from .views import index, contato, add_item_playlist, search_item, add_success, del_success, add_user, user_in, user_out

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('add_item_playlist/', add_item_playlist, name='add_item_playlist'),
    path('search_item/', search_item, name='search_item'),
    path('adicionado_com_sucesso/', add_success, name='add_success'),
    path('removido_com_sucesso/', del_success, name='del_success'),
    path('add_user/', add_user, name='add_user'),
    path('login/', user_in, name='user_in'),
    path('logout/', user_out, name='user_out'),
]