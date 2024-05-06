import pandas as pd
import matplotlib.pyplot as plt
from . import *

def showGraph2024Inflation():
    data = pd.read_csv('./data/inflation/inflasi_rupiah_2024.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="barh")

    plt.title("Inflasi Rupiah 2024")
    plt.show()

def showGraph2023Inflation():
    data = pd.read_csv('./data/inflation/inflasi_rupiah_2023.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2023")
    plt.show()

def showGraph2022Inflation():
    data = pd.read_csv('./data/inflation/inflasi_rupiah_2022.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2022")
    plt.show()

def showGraph2021Inflation():
    data = pd.read_csv('./data/inflation/inflasi_rupiah_2021.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2021")
    plt.show()

def showGraph2020Inflation():
    data = pd.read_csv('./data/inflation/inflasi_rupiah_2020.csv')
    data.plot(x="bulan", y="nilai_inflasi", xlabel="Bulan", ylabel="Nilai", kind="bar")
    plt.title("Inflasi Rupiah 2020")
    plt.show()

def showGraphMeanInflation():
    data = pd.read_csv('./data/inflation/mean_inflation.csv')
    data.plot(x="tahun", y="rata_rata", xlabel="Tahun", ylabel="Rata-Rata", kind="bar")
    plt.title("Nilai Rata Rata Inflasi Tahun ke Tahun")
    plt.show()

def showCPI2020():
    dataCPI2020.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2020")
    plt.show()

def showCPI2021():
    dataCPI2021.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2021")
    plt.show()

def showCPI2022():
    dataCPI2022.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2022")
    plt.show()

def showCPI2023():
    dataCPI2023.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2023")
    plt.show()

def showCPI2024():
    
    dataCPI2024.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2024")
    plt.show()

def showCPIAll():

    fig, axis = plt.subplots(nrows=1, ncols=5)
    dataCPI2024.plot(ax=axis[0], x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="hist", alpha=0.5)
    dataCPI2023.plot(ax=axis[1], x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="hist", alpha=0.5)
    dataCPI2022.plot(ax=axis[2], x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="hist", alpha=0.5)
    dataCPI2021.plot(ax=axis[3], x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="hist", alpha=0.5)
    dataCPI2020.plot(ax=axis[4], x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="hist", alpha=0.5)

    axis[0].set_title('CPI 2024')
    axis[1].set_title('CPI 2023')
    axis[2].set_title('CPI 2022')
    axis[3].set_title('CPI 2021')
    axis[4].set_title('CPI 2020')

    plt.show()
