import pickle
import pandas as pd
import json

def predict_mpg(config):
    ##loading the model from the saved file
    pkl_filename = "random_forest_model.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)

    df = pd.DataFrame(config)
    
    y_pred = model.predict(df)
    
    if y_pred.tolist()[0] == 0:
        return "La Transaction n'est pas frauduleuse"
    else:
        return 'La Transaction est frauduleuse'
    