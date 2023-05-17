# P13 : Mettez à l'échelle une application Django en utilisant une architecture modulaire






## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`










# Explications :


Une fois le pipeline CircleCi est configuré, le déploiement se fera automatiquement a chaque push commit effectué.

- Les tests seront effectuer automatiquements lors du Push git.

- SI les tests sont validés:
  - Une image Docker est créer puis pousser vers DockerHub

- SI l'étape précédente est réussit:
  - Le déploiement s'effectue sur Heroku

    
    
### Conditions préalables :



Il est nécessaire de créer plusieurs comptes afin de pouvoir effectuer le déploiement et l'intégration continue de l'application

- Compte GitHub
- Compte CircleCI
- Compte Docker
- Compte Heroku
- Compte Sentry




### Une fois les comptes utilisateurs créer :


- Récupérer sur DockerHub l'acces Token.
- Récupérer sur Heroku l'API Key dans les settings de votre compte Heroku.
- Récupérer le DSN du projet Sentry.


### Puis créer un nouveau projet Heroku depuis votre terminal :

`heroku create <nom_de_mon_app>`

Puis allez dans les settings de CircleCi de votre projet afin d'ajouter votre variables d'environnements.

### 6 variables devront etre présente

- DOCKER_LOGIN = Votre username sur DockerHub.
- DOCKER_PASSWORD = Votre Token acces sur DockerHub.
- HEROKU-API_KEY = l'API Key récupérée sur votre compte Heroku.
- HEROKU_APP_NAME = Nom que vous avez choisi pour votre application sur Heroku.
- SECRET_KEY = Secret key de production de settings.py de l'application Django.
- SENTRY_DSN = DSN de votre projet Sentry.


### Une fois un commit effectuer, le site est alors disponible sur Heroku:

`https://<nom_de_mon_app>.herokuapp.com/`




docker pull boukaii/test1:310d789f682c6f53148eacc70ef85cb5f5804bae
  


docker run -d -p 8080:8080 <test_image>

# Récupération de l'image du registre (Docker) :


`docker run -d -p 8000:8000 <nom_de_l'image>`

### Vous pouvez ensuite vous rendre à l'adresse http://127.0.0.1:8000/













# Méthode "manuel" :



### Images que l'ont va créer en local : (Docker)


- Se connecter a docker :
`docker login`           

- Création de l'image :
`docker build -t <nom_de_l'image> .`    

- Vérifie création de l'image :
`docker images`  

 - Envoi vers docker :
`docker push boukaii/<nom_de_l'image>`  

 - Récupère depuis docker :
`docker pull <nom_de_l'image>`     

- Pour lancer l'image :
`docker run -d -p 8080:8080 <nom_de_l'image>`

   

###  Déploiement :  (Heroku) (nom de l'application =  deploitest )

- `heroku login`
- `heroku create <nom_application>`
- `heroku open`



