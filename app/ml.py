# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import os

class MachineLearning(object):
    """docstring for MachineLearning."""

    module_dir = os.path.dirname(__file__) # get the current directory
    file_path = os.path.join(module_dir, 'static/ml/heart_model.pickle')
    model = pd.read_pickle(file_path)

    def __init__(self):
        super(MachineLearning, self).__init__()
        #self.arg = arg


    def predict(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        result = self.model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])  # input must be 2D array
        if result == 1:
            str = "Malade"
            return str
        else:
            str = "Pas Malade"
            return str
