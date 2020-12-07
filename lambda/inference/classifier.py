import pickle
from pandas import DataFrame
import json

class ChurnClassifier:
    """An inference class for classifier"""
    def __init__(self) -> None:        
        filename = 'trained_model.mdl'
        self.model = pickle.load(open(filename, 'rb'))

    def predict(self, customer):
        dfc = DataFrame([customer])
        prediction = self.model.predict(dfc)
        return prediction[0]