# Desafio Weni - Dev Django Júnior

Este projeto tem como intuito listar uma playlist específica (ID da playlist está imbutido), e o dono da playlist poderá se autenticar (obter o token) e gerenciar ela, adicionando ou removendo tracks.

Projeto desenvolvido inicialmente como avaliação para o cargo de Analista de Suporte N3. Atualizado como avaliação para o cargo Dev Django Júnior.

## Release notes commit "fixes views"

- Funções de autenticação foram removidas de views.py e adicionadas ao arquivo auth.py;
- Playlists foi convertida para uma classe, disponível em core/class/Playlist.py;
- Ajustado o nome de algumas constantes para o padrão "capital letters with underscore";
- Reduzida consideravelmente a view index();