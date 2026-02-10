import pandas as pd
import matplotlib.pyplot as plt 

def load_dataset(path):
    if path.endswith('csv'):
        df= pd.read_csv(path.csv)
        return df 