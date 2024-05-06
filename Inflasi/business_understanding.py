import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/inflation/inflasi-rupiah.csv')
dataCPI = pd.read_csv('./data/cpi/cpi_indonesia.csv')


def showInfoData():
    data.info()

def showDataFrame():
    return pd.DataFrame(data)

def showInfoCPI():
    dataCPI.info()

def showDataFrameCPI():
    return pd.DataFrame(dataCPI)
