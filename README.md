# Projet MLOps : Prédiction sur l'espèce Iris

## Description du projet

Ce projet consiste à prédire l'espèce d'Iris en fonction des caractéristiques de fleurs (longueur et largeur des sépales et pétales) en utilisant le jeu de données Iris. Le modèle un classifier de type random forest. Le projet met en relation plusieurs composantes : 
- Une interface Streamlit
- Un serveur FastApi
- Le déploiement du modèle dans un container Docker
 
## Utilisation de l'applicat

1. **Cloner le repertoire**
   
   ```bash
   git clone https://github.com/lucilecpp/MLops.git
    ```

2. **Lancer l'application**

    ```bash
    docker compose up --build
    ```

Une fois l'application lancée suivez ce lien  http://localhost:8501/ qui vous permettra de réaliser vos propres prédictions en fonction des valeurs que vous mettrez pour chaque features. 

Le lien apparaît également dans votre console au moment du docker compose.


3. **Shutdown de l'application**

Une fois toutes vos prédictions terminées lancez la commande suivante pour fermer l'application : 

    ```bash
    docker compose down
    ```