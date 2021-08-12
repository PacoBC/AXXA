sudo apt update
sudo apt upgrade

#Instalar paquetes requisitos previos
sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common
#Aregar repositorios de docker
#agregar clase GPG
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#Aregar repositorio
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#actualizar info repositorio
sudo apt update
#Verificar si está instalado desde el repositorio de docker
apt-cache policy docker-ce


#Instalar Docker
sudo apt install docker-ce

#Comprobar estado de Docker
sudo systemctl status docker