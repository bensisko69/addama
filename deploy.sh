#! /usr/bin/env bash

# construction image -t pour le nom et . pour le chemin ou ce trouve le dockerfile
    docker build -t bensisko/base .
#  cree le conteneur qui lance le serveur
# -it recuperer la sortie standard
# -v $PWD:/app partage du dossier courant avec le conteneur
# -p exposition du port 9999 du conteneur vers le port 80 du host
# -d lance le conteneur en arrière plan (detached)
    docker run -it bensisko/base -v $PWD:/app django-admin startproject $1
    docker run -it bensisko/base -v $PWD:/app python manage.py startapp main
    docker run --name base -d -it -v $PWD:/app -p 80:9999 bensisko/base


