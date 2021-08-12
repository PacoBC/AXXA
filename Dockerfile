FROM httpd

LABEL mainteiner=isc.robertomarin15@gmail.com

RUN apt-get update
RUN apt install nano

COPY ./public-html/ /usr/local/apache2/htdocs