Le livrable finale de ma SAE2.3 contient 4 fichiers Python :

- "Request.py" est un fichier qui contient toutes les requêtes SQL nécessaires à la création de ma base ainsi qu'à un jeu d'essai de plusieurs enregistrements par table. Il a été modifié depuis le rendu du livrable 1 pour intégrer une nouvelle table "enchérir" qui était nécessaire au bon fonctionnement de ma vente aux enchères. Il est inutile d'exécuter ce fichier car rien ne se passera.

- "BDsae23Utils.py" est un fichier qui contient les différentes fonctions nécessaires à la création et à l'initialisation de ma base de données. Ce fichier peut être exécuté si l'on souhaite simplement créer et initialiser la base de données, sans avoir accès au CRUD en mode CLI.

- "CLI.py" est un fichier qui permet de créer différentes fonctions CRUD pour les tables "pilotes" et "motos" de ma base de données. Ces fonctions CRUD sont accessibles en mode CLI grâce à un menu interactif et à différentes routines non interactives. Vous pourrez constater que j'ai ajouté quelques procédures non interactives qui sont utiles pour mon appli web dans ce fichier afin de centraliser toutes les procédures qui interagissent avec ma base de données dans le même fichier python pour améliorer l'organisation de mes données. Ce fichier doit être exécuté pour accéder à toutes les fonctionnalités du livrable 1, à savoir la création et l'initialisation de ma base de données ainsi que l'accès à une interface en mode CLI qui permet d'interagir avec la base de données. 

- "ServeurWeb.py" est le fichier qui permet de démarrer le serveur CherryPy. Il définit différentes méthodes pour chaque page de l'application web. Chaque méthode représente une page spécifique et permet de gérer les requêtes vers cette page en utilisant le moteur de template Mako et les procédures présentes dans le fichier "CLI.py". Ce fichier doit être exécuté afin de démarrer le serveur CherryPy. Une fois exécuté, il faut se rendre sur un navigateur et entrer l'URL "http://localhost:8080/" afin d'avoir accès à mon application web fonctionnelle. 




Informations complémentaires :

- Attention à bien modifier les identifiants de connexion à l'intérieur des scriptes "BDsae23Utils.py" et "CLI.py" s'ils sont différents des miens. Sinon, la connexion à la base de données echoueras et les programmes python ne pourront pas s'exécuter correctement.

- Lors de mes testes sur la configuration examRT des ordinateurs de l'IUT, j'ai constaté que mes programmes ne s'exécutaient pas correctement lors de la première exécution. Il faut donc exécuter 2 fois le programme python qui crée ma base (BDsae23Utils.py) puis 2 fois le programme python qui démarre le serveur web cherryPy (ServeurWeb.py) si l'on veut avoir accès à mon appli web fonctionnelle. 