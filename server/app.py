from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import pickle
import numpy as np

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load the model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

species_dict = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

@app.post("/predict")
def predict(item: Item):
    item_data = jsonable_encoder(item)
    features = np.array([[item_data["sepal_length"], 
                          item_data["sepal_width"], 
                          item_data["petal_length"], 
                          item_data["petal_width"]]])
    
    
    predicted_species = int(model.predict(features)[0]) 
    species_name = species_dict.get(predicted_species)
    return {"Fleur prédite": species_name}
    
    # predicted_class = int(model.predict(features)[0])
    # return {"Fleur prédite ": (predicted_class)}
    # data = np.array([item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]).reshape(1, -1)
    # prediction = int(model.predict(data))
    # if prediction == 0:
    #     classe = "Setosa"
    # elif prediction == 1:
    #     classe = "Versicolor"
    # elif prediction == 2:
    #     classe = "Virginica"
    # return {"Classe": classe}