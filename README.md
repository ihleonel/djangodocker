# Django - Docker
## Dependencias
1. Docker v18.09.4
1. Docker-compose v1.24.0

## Como iniciar
1. Clonar repositorio
1. Correr el comando `$ docker-compose up --build`
1. Iniciar contenedores `$ docker-compose up -d`

## Nota
Debido a que django esta corriendo en un contenedor, cada vez que necesitemos correr un comando del mismo (makemigrations, migrate, startapp) se deberá hacer de la siguiente manera:

`$ docker-compose run web python manage.py startapp name_new_app`

En este ejemplo estariamos creando una nueva app en el proyecto. Notese que en este caso el nombre del contenedor es `web` ya que asi fue definido en el archivo `docker-compose.yml`

## Changelog
Se agrega un archivo llamado `settings-docker.py` y se configura que al correr el contenedor se base en ese archvo de configuracion. Esto permite correr los comandos `migrate`, `makemigartions`, etc. de django sin necesidad de entrar al contenedor. 
