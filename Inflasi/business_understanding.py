import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/inflasi-rupiah.csv')

def showInfoData():
    data.info()

def showDataFrame():
    return pd.DataFrame(data)