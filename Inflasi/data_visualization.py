import pandas as pd
import matplotlib.pyplot as plt

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
    data = pd.read_csv('./data/cpi/cpi_2020.csv')
    data.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2020")
    plt.show()

def showCPI2021():
    data = pd.read_csv('./data/cpi/cpi_2021.csv')
    data.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2021")
    plt.show()

def showCPI2022():
    data = pd.read_csv('./data/cpi/cpi_2022.csv')
    data.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2022")
    plt.show()

def showCPI2023():
    data = pd.read_csv('./data/cpi/cpi_2020.csv')
    data.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2023")
    plt.show()

def showCPI2024():
    data = pd.read_csv('./data/cpi/cpi_2024.csv')
    data.plot(x="periode", y=["food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"], xlabel="Periode", ylabel="Index", kind="line")
    plt.title("CPI Tahun 2024")
    plt.show()