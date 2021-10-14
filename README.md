# Desafio Weni - Dev Django Júnior

Este projeto tem como intuito listar uma playlist específica (ID da playlist está imbutido), e o dono da playlist poderá se autenticar (obter o token) e gerenciar ela, adicionando ou removendo tracks.

Projeto desenvolvido inicialmente como avaliação para o cargo de Analista de Suporte N3. Atualizado como avaliação para o cargo Dev Django Júnior.

### Resumo do desafio:

- [x]  Usar gerenciador de dependências Poetry
- Instalado e configurado o Poetry como gestor de dependências
- [x]  Separar dependências dev de prod (dev-dependencies)
- Instalado o Pytest e o coverage como dev-dependencies
- [x]  Não comittar o DB (usar data migrations)
- Refatorado algumas constantes que estavam cadastradas dentro do banco de dados. Hoje utilizo variáveis de ambiente com o django-environ para isso. Adicionei no .gitignore o arquivo do banco de dados e resetei o indice do git para que o arquivo fosse excluído do repositório. Não houve necessidade de usar data migrations.
- [x]  Evitar dependencias desnecessárias
- Removido as dependências: Pillow==8.2.0, PyMySQL==1.0.2, beautifulsoup4==4.9.3, gunicorn==20.1.0, asgiref==3.3.4, idna==2.10, pytz==2021.1
- [x]  Usar git branches para commitar os fixes
- Aprendi como utilizar branches no git. A cada funcionalidade nova, eu fazia um novo commit diferente neste branch.
- [x]  Autenticação
- Desenvolvi três views novas, uma para cadastrar um novo usuário, outra para logar um usuário e a última para deslogar. Apenas usuários logados tem acesso às views index e as demais views relacionadas ao sistema.
- [x]  Alterar nomes de variáveis para inglês e snake_case / PascalCase
- Refatorado alguns nomes de variáveis e funções que encontrei
- [x]  Usar variáveis de ambiente para dados sensíveis (django-environ)
- Instalado o django-environ e configurado a SECRET_KEY, DEBUG, ALLOWED_HOSTS, CLIENT_ID, CLIENT_SECRET E PLAYLIST_ID
- [x]  A view index() faz muita coisa, o que dificulta a leitura e manutenção.
- Reestruturei as views. Tentei ao máximo comentar o que cada situação faz dentro do código.
- [ ]  Implementar testes com pytest
- Tive dificuldades de como fazer testes com as minhas funções que recebem como parâmetro uma requisição e retornam um redirect. Apesar de ter estudado como implementar testes, não consegui fazer exemplos com meu projeto.
- [ ]  Cobertura de testes com a lib "coverage"
- Instalado e adicionado os pacotes pytest-cov e coverage como dev-dependencies no poetry. Mas infelizmente não possuo nenhum teste válido no projeto.

### Melhorias no projeto:

- Criada a possibilidade do usuário informar o ID da sua playlist e gerenciá-lo através do APP (antes o ID da playlist era uma constante, ou seja, a playlist era fixa)
- Funções de autenticação foram removidas de views.py e adicionadas ao arquivo auth.py;
- Playlists foi convertida para uma classe, disponível em core/class/Playlist.py;
- Ajustado o nome de algumas constantes para o padrão "capital letters with underscore";
- Reduzida consideravelmente a view index();
- Autenticação utilizando nativamente o Django