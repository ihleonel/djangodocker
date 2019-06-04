# Django - Docker
## Dependencias
1. Python v3.6
1. Virtualenv v16.0.0
1. Docker v18.09.4
1. Docker-compose v1.24.0

## Como iniciar
1. Clonar repositorio
1. Correr el comando `$ docker-compose up --build`
1. Iniciar contenedores `$ docker-compose up -d`
1. Crear entorno virtual `$ virtualenv --python=python3.6 env`
1. Activar entorno virtual `$ source env/bin/activate`
1. Instalar dependencias `$ pip install -r requirements.txt`

## Deprecated
Debido a que django esta corriendo en un contenedor, cada vez que necesitemos correr un comando del mismo (makemigrations, migrate, startapp) se deberá hacer de la siguiente manera:

`$ docker-compose run web python manage.py startapp name_new_app`

En este ejemplo estariamos creando una nueva app en el proyecto. Notese que en este caso el nombre del contenedor es `web` ya que asi fue definido en el archivo `docker-compose.yml`

## Changelog
Se agrega un archivo llamado `docker.py` dentro de una carpeta settings, y se configura que al correr el contenedor se base en ese archivo de configuración. Esto permite correr los comandos `migrate`, `makemigartions`, etc. de django sin necesidad de entrar al contenedor.
No se debe olvidar que antes de correr en local los comandos es necesario activar el entorno virtual. 

## TODO
Crear entorno virtual de manera automatica basado en la version de Python que esta en el contenedor e instalar las dependencias especificadas en requirements.txt

