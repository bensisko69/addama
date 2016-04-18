#! /usr/bin/env bash

# construction image -t pour le nom et . pour le chemin ou ce trouve le dockerfile
if ! docker inspect bensisko/addama &> /dev/null; then
    docker build -t bensisko/addama .
else
    echo "Image is already built"
fi

#  cree le conteneur qui lance le serveur
# -it recuperer la sortie standard
# -v $PWD:/app partage du dossier courant avec le conteneur
# -p exposition du port 9999 du conteneur vers le port 80 du host
# -d lance le conteneur en arrière plan (detached)
if ! docker inspect wouf-educ &> /dev/null; then
    docker run --name wouf-educ -d -it -v $PWD:/app -p 81:9999 bensisko/addama
    docker exec wouf-educ python manage.py makemigrations
    docker exec wouf-educ python manage.py migrate
else
    echo "Server is already running"
fi


