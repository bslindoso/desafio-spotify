# Desafio Spotify

Este projeto tem como intuito listar uma playlist específica (antes o ID da playlist estava imbutido, agora é possível informar sua playlist), e o dono da playlist poderá se autenticar (obter o token) e gerenciar ela, adicionando ou removendo tracks.

Para desenvolver este projeto, foi necessário conhecimentos de:

- Python
- Django
- Rest API
- Html, CSS e JavaScript
- Bootstrap

## Resumo da última versão:

- [x]  Instalado e configurado o Poetry como gestor de dependências
- [x]  Separado dependências dev de prod (dev-dependencies)
- [x]  Não comittar o DB (usar data migrations)
- Refatorado algumas constantes que estavam cadastradas dentro do banco de dados. Hoje utilizo variáveis de ambiente com o django-environ para isso. Adicionei no .gitignore o arquivo do banco de dados e resetei o indice do git para que o arquivo fosse excluído do repositório. Não houve necessidade de usar data migrations.
- [x]  Evitar dependencias desnecessárias
- Removido as dependências: Pillow==8.2.0, PyMySQL==1.0.2, beautifulsoup4==4.9.3, gunicorn==20.1.0, asgiref==3.3.4, idna==2.10, pytz==2021.1
- [x]  Autenticação: Desenvolvida três views novas, uma para cadastrar um novo usuário, outra para logar um usuário e a última para deslogar. Apenas usuários logados tem acesso às views index e as demais views relacionadas ao sistema.
- [x]  Alterar nomes de variáveis para inglês e snake_case / PascalCase
- Refatorado alguns nomes de variáveis e funções que encontrei
- [x]  Usar o django-environ para variáveis de ambiente e ocultar dados sensíveis 
- [x]  Reestruturada as views, modularizando e reduzindo ao máximo.


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

