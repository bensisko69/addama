#! /usr/bin/env bash

# construction image -t pour le nom et . pour le chemin ou ce trouve le dockerfile
if ! docker inspect bensisko/base &> /dev/null; then
    docker build -t bensisko/base .
else
    echo "Image is already built"
fi

#  cree le conteneur qui lance le serveur
# -it recuperer la sortie standard
# -v $PWD:/app partage du dossier courant avec le conteneur
# -p exposition du port 9999 du conteneur vers le port 80 du host
# -d lance le conteneur en arrière plan (detached)
if ! docker inspect bensisko/base &> /dev/null; then
    docker run --name base -d -it -v $PWD:/app -p 80:9999 bensisko/base
    docker exec base python manage.py makemigrations
    docker exec base python manage.py migrate
else
    echo "Server is already running"
fi


