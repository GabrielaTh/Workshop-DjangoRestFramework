# Workshop-DjangoRestFramework

Planning Workshop Django-Rest Framework par François Héliodore

#Réaliser une API avec DRF

#Vérifier votre version de Python :

python --version

La Mettre à jour :

sudo apt-get update

sudo apt-get install python3.6

Si besoin, changer la version de python:

sudo update-alternatives --config python3

Installer l’environnement virtuel:
pip install virtualenv

Création de l’environnement virtuel :
mkdir workshop && cd workshop

virtualenv --python=python3 venv 

source venv/bin/activate 

ou 

source venv/Scripts/activate

Installation de Django :

pip install Django

pip install djangorestframework

django-admin.py startproject api

cd api

django-admin.py startapp newapp

Normalement, votre projet devrait ressembler à ça :

api/
    api/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    newapp/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    manage.py /











    1.  Présenter et installer Python et DRF
        1. Présentation de Python et DRF(15 min)
 
        2. Installation 30 min
        
    2. Présentation DRF(1h15)
        1. Models
        2. Serializers
        3. Urls
        4. Views
        
    3. Pause 11h-11h15 : 
    
    4. Authentification  (1h15)
    
        1. Présentation Admin et Browsable API
        2. Différents types d'authentification
           
