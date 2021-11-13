# Desafio Spotify

Este projeto tem como intuito listar uma playlist específica (antes o ID da playlist estava imbutido, agora é possível informar sua playlist), e o dono da playlist poderá se autenticar (obter o token) e gerenciar ela, adicionando ou removendo tracks.

Para desenvolver este projeto, foi necessário conhecimentos de:

- Python
- Django
- Rest API
- Html, CSS e JavaScript
- Bootstrap

## Resumo das últimas alterações do projeto:

- [x] Alterda a classe Playlist tornando-a mais Pythônica (usando @property)
- [x] Refatorado como as músicas da Playlist são armazenadas no sistema. Agora utiliza-se a classe *Track* para gerar a lista de músicas.
- [x] Removido funções print() remanescentes das views


## Melhorias no projeto:

- Criada a possibilidade do usuário informar o ID da sua playlist e gerenciá-lo através do APP (antes o ID da playlist era uma constante, ou seja, a playlist era fixa)
- Funções de autenticação foram removidas de views.py e adicionadas ao arquivo auth.py;
- Playlists foi convertida para uma classe, disponível em core/class/Playlist.py;
- Ajustado o nome de algumas constantes para o padrão "capital letters with underscore";
- Reduzida consideravelmente a view index();
- Autenticação utilizando nativamente o Django

## IMPORTANTE (AO AVALIADOR)
- Para você conseguir manipular a Playlist, você deverá ser o proprietário dela. Ou seja, não há como manipular Playlists de terceiros ou colaborativas através da API.
- Além disso, seu usuário do Spotify deverá ser cadastrado no https://developer.spotify.com/dashboard/, pois o APP se encontra em Developer Mode. Caso queira testar o sistema, favor mandar um e-mail para <brunolindoso@gmail.com> com seu nome completo e seu e-mail cadastrado no Spotify que adiciono você como usuário do APP. (Isso é uma restrição do Spotify)

