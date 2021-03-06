from fabric.api import run, local, hosts, cd
from fabric.contrib import django

#descargo el repositorio
def descargar_repositorio():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/ignaciorecuerda/gestionpedidos_django.git')

#Hacer test
def ejecutar_tests():
	run('cd gestionPedidos && make test')

#Aprovisiona maquina en azure
def lanzar_azure():
	run('cd gestionPedidos && make azure')

#Lanza aplicacion en azure
def lanzar_app_azure():
	run('sudo python gestionPedidos/manage.py runserver 0.0.0.0:80')

#Usando Docker
#Instalando mi version de Docker
def descargar_imagen_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull ignaciorecuerda2/gestionpedidos_django')
	# run('sudo docker run -p 8000:8000 -i -t ignaciorecuerda2/gestionpedidos_django')

#Ejecucion de docker
def ejecuta_docker():
	run('sudo docker run -p 8000:8000 -i -t ignaciorecuerda2/gestionpedidos_django')