import streamlit as st
import requests

# Custom CSS for styling the app
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F8F4F8;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Heading
st.markdown("<h1 style='text-align: center;'>🌺Prédiction Iris 🌺</h1>", unsafe_allow_html=True)

# Explanation of the page
st.markdown(
    """
    Entrez les mesures des sépales et des pétales pour prédire l'espèce d'iris.
    Cliquez sur "Prédiction" pour voir le résultat.
    """,
    unsafe_allow_html=True
)

# Inputs for the sliders
columns = {
    "sepal_length": st.slider("Longueur des sépales", 0.0, 10.0, 0.0),
    "sepal_width": st.slider("Largeur des sépales", 0.0, 10.0, 0.0),
    "petal_length": st.slider("Longueur des pétales", 0.0, 10.0, 0.0),
    "petal_width": st.slider("Largeur des pétales", 0.0, 10.0, 0.0)
}

# Prediction button with a spinner
button_pred = st.button("Prédiction")

# If button pred
if button_pred:
    with st.spinner('Calcul en cours...'):
        prediction = requests.post("http://server:8000/predict", json=columns)
        species_name = prediction.json().get("Fleur prédite")
        st.write(f"Fleur prédite: {species_name}")

        # Display image based on prediction
        if species_name == "Virginica":
            st.image("https://www.gardenia.net/wp-content/uploads/2023/05/iris-virginica-780x520.webp", caption="Virginica", use_container_width=True)
        elif species_name == "Setosa":
            st.image("https://www.plant-world-seeds.com/images/item_images/000/007/023/large_square/iris_baby_blue.jpg?1500653527", caption="Setosa", use_container_width=True)
        elif species_name == "Versicolor":
            st.image("https://www.jardindion.com/wp-content/uploads/2023/12/2577302d-iris-versicolor-r14_01.png", caption="Versicolor", use_container_width=True)

    # Trigger balloons animation for fun
    st.balloons()
