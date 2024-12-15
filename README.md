# Projet MLOps : Prédiction sur l'espèce Iris

## Description du projet

Ce projet consiste à prédire l'espèce d'Iris en fonction des caractéristiques de fleurs (longueur et largeur des sépales et pétales en centimètres) en utilisant le jeu de données Iris. Le modèle un classifier de type Random Forest. Le projet met en relation plusieurs composantes : 

- **Interface Streamlit** : permet d'interagir avec le modèle et de faire des prédictions en ligne.
- **Serveur FastAPI** : permet d'obtenir la classe prédite
- **Déploiement avec Docker** : l'interface, le serveur et le modèle est gérer avec Docker pour un déploiement facile'.

## Prérequis

Si ce n'est pas déjà le cas, assurez-vous d'installer [Docker](https://www.docker.com/products/docker-desktop/) sur votre machine.
 
## Utilisation de l'application

1. **Cloner le repertoire**
   
   ```bash
   git clone https://github.com/lucilecpp/MLops.git
    ```

2. **Lancer l'application**

    ```bash
    docker compose up --build
    ```
    Cette commande va démarrer l'application. Une fois lancée, vous pouvez accéder à l'interface Streamlit à l'adresse suivante : 
    
    http://localhost:8501/ 
    
    Cela vous permettra de réaliser vos propres prédictions en fonction des valeurs que vous mettrez pour chaque features. Le lien vers l'application sera également affiché dans votre console.  

    <br>

3. **Arrêt de l'application**
    
    Une fois toutes vos prédictions terminées lancez la commande suivante pour fermer l'application :
    
    ```bash
    docker compose down
    ```
 
