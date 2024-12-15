import streamlit as st
import requests
import os

st.title("Prédiction Iris")

columns = {
    "sepal_length" : st.slider("Sepal Length", 0.0, 10.0, 0.0),
    "sepal_width" : st.slider("Sepal Width", 0.0, 10.0, 0.0),
    "petal_length" : st.slider("Petal Length", 0.0, 10.0, 0.0),
    "petal_width" : st.slider("Petal Width", 0.0, 10.0, 0.0)
}

button_pred = st.button("Prédiction")


if button_pred :
    prediction = requests.post("http://server:8000/predict", json = columns)
    species_name = prediction.json().get("Fleur prédite")
    st.write(species_name)

    if species_name == "Virginica" :
        st.image("https://www.gardenia.net/wp-content/uploads/2023/05/iris-virginica-780x520.webp", caption = "Virginica", use_container_width=True)

    elif species_name == "Setosa" :
        st.image("https://www.plant-world-seeds.com/images/item_images/000/007/023/large_square/iris_baby_blue.jpg?1500653527", caption = "Setosa", use_container_width=True)

    elif species_name == "Versicolor" :
        st.image("https://www.jardindion.com/wp-content/uploads/2023/12/2577302d-iris-versicolor-r14_01.png", caption = "Versicolor", use_container_width=True)
