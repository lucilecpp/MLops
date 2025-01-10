# Projet MLOps : Prédiction sur l'espèce Iris :hibiscus:

## Table des matières

1. [Description du projet](#description-du-projet)
2. [Description des données](#description-des-données)
3. [Pré-requis](#pré-requis)
4. [Utilisation de l'application](#utilisation-de-lapplication)
5. [Démonstration](#démonstration)
6. [Auteur](#auteur)

## Description du projet

Ce projet consiste à prédire l'espèce d'Iris en fonction des caractéristiques de fleurs (longueur et largeur des sépales et pétales en centimètres) en utilisant le jeu de données Iris. Le modèle un classifier de type Random Forest. Le projet met en relation plusieurs composantes : 

- **Interface Streamlit** : permet d'interagir avec le modèle et de faire des prédictions en ligne.
- **Serveur FastAPI** : permet d'obtenir la classe prédite
- **Déploiement avec Docker** : l'interface, le serveur et le modèle est gérer avec Docker pour un déploiement facile'.

## Description des données

Le jeu de données Iris est l'un des jeux de données les plus connus en machine learning. Il contient 150 échantillons de fleurs de type iris, répartis équitablement entre trois espèces :

1. *Setosa*
2. *Versicolor*
3. *Virginica*

Chaque échantillon est décrit par quatre caractéristiques :

- Longueur du sépale (en cm)
- Largeur du sépale (en cm)
- Longueur du pétale (en cm)
- Largeur du pétale (en cm)

Ces données sont souvent utilisées pour illustrer des algorithmes de classification.



## Pré-requis

Si ce n'est pas déjà le cas, assurez-vous d'installer [Docker](https://www.docker.com/products/docker-desktop/) sur votre machine.
 
## Utilisation de l'application

1. **Cloner le repertoire**
   
   ```bash
   git clone https://github.com/lucilecpp/MLops.git
    ```
 Avant de lancer l'application assurez-vous d'ouvrir Docker Desktop.
2. **Lancer l'application**

    ```bash
    docker compose up --build
    ```
    Cette commande va démarrer l'application. Une fois lancée, vous pouvez accéder à l'interface Streamlit à l'adresse suivante : 
    
    http://localhost:8501/ 
    
    Cela vous permettra de réaliser vos propres prédictions en fonction des valeurs que vous mettrez pour chaque features. Le lien vers l'application sera également affiché dans votre console.  


## Démonstration
L'interface une fois démarée et la prédiction lancée ressemble à ceci : 

<img src="https://github.com/lucilecpp/MLops/blob/main/Image/Animation.gif"/>

## Auteur
Ce projet a été réalisé par Lucile PERBET dans le cadre du Master 2 SISE à l'université Lumière Lyon 2.
 
