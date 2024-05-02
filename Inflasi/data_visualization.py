import pandas as pd
import matplotlib.pyplot as plt

def showGraph2024Inflation():
    data = pd.read_csv('./data/inflasi_rupiah_2024.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="barh")

    plt.title("Inflasi Rupiah 2024")
    plt.show()

def showGraph2023Inflation():
    data = pd.read_csv('./data/inflasi_rupiah_2023.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2023")
    plt.show()

def showGraph2022Inflation():
    data = pd.read_csv('./data/inflasi_rupiah_2022.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2022")
    plt.show()
