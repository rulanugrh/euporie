import csv
import math

inflasi_2024 = []
inflasi_2023 = []
inflasi_2022 = []
inflasi_2021 = []
inflasi_2020 = []
calculation = []
cpi_2020 = []
cpi_2021 = []
cpi_2022 = []
cpi_2023 = []
cpi_2024 = []

def generate_data():
    field_calculation = ['tahun', 'nilai']
    fields = ['bulan', 'nilai_inflasi']
    with open('./data/inflation/inflasi-rupiah.csv', 'r') as f:
        plot = csv.reader(f, delimiter=",")
        for rows in plot:
            calculation.append({
                'tahun': rows[2],
                'nilai': rows[3]
            })

            if rows[2] == "2024":
                inflasi_2024.append({
                    'bulan': rows[1],
                    'nilai_inflasi': rows[3]
                })
            
            elif rows[2] == "2023":
                inflasi_2023.append({
                    'bulan': rows[1],
                    'nilai_inflasi': rows[3]
                })
            
            elif rows[2] == "2022":
                inflasi_2022.append({
                    'bulan': rows[1],
                    'nilai_inflasi': rows[3]
                })

            elif rows[2] == "2021":
                inflasi_2021.append({
                    'bulan': rows[1],
                    'nilai_inflasi': rows[3]
                })
                
            
            elif rows[2] == "2020":
                inflasi_2020.append({
                    'bulan': rows[1],
                    'nilai_inflasi': rows[3]
                })


    with open('./data/inflation/inflasi_rupiah_2024.csv', 'w', newline='') as dt2024:
        writer = csv.DictWriter(dt2024, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2024)

    with open('./data/inflation/inflasi_rupiah_2023.csv', 'w', newline='') as dt2023:
        writer = csv.DictWriter(dt2023, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2023)

    with open('./data/inflation/inflasi_rupiah_2022.csv', 'w', newline='') as dt2022:
        writer = csv.DictWriter(dt2022, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2022)

    with open('./data/inflation/inflasi_rupiah_2021.csv', 'w', newline='') as dt2021:
        writer = csv.DictWriter(dt2021, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2021)

    with open('./data/inflation/inflasi_rupiah_2020.csv', 'w', newline='') as dt2020:
        writer = csv.DictWriter(dt2020, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2020)

    with open('./data/inflation/inflation_accumulation.csv', 'w', newline='') as dtaccumulation:
        writer = csv.DictWriter(dtaccumulation, fieldnames=field_calculation)
        writer.writeheader()
        writer.writerows(calculation)


def generateDataCPI():
    field = ["periode", "food_n_beverages", "clothing_footwear", "house_water_electricity", "health", "transport", "education_services", "other"]

    with open('./data/cpi/cpi_indonesia.csv', 'r') as f:
        plot = csv.reader(f, delimiter=',')
        for rows in plot:
            if rows[13] == "2020":
                cpi_2020.append({
                    'periode': rows[0],
                    'food_n_beverages': rows[2],
                    'clothing_footwear': rows[3],
                    'house_water_electricity': rows[4],
                    'health': rows[6],
                    'transport': rows[7],
                    'education_services': rows[10],
                    'other': rows[12]
                })
            elif rows[13] == "2021":
                cpi_2021.append({
                    'periode': rows[0],
                    'food_n_beverages': rows[2],
                    'clothing_footwear': rows[3],
                    'house_water_electricity': rows[4],
                    'health': rows[6],
                    'transport': rows[7],
                    'education_services': rows[10],
                    'other': rows[12]
                })
            elif rows[13] == "2022":
                cpi_2022.append({
                    'periode': rows[0],
                    'food_n_beverages': rows[2],
                    'clothing_footwear': rows[3],
                    'house_water_electricity': rows[4],
                    'health': rows[6],
                    'transport': rows[7],
                    'education_services': rows[10],
                    'other': rows[12]
                })
            elif rows[13] == "2023":
                cpi_2023.append({
                    'periode': rows[0],
                    'food_n_beverages': rows[2],
                    'clothing_footwear': rows[3],
                    'house_water_electricity': rows[4],
                    'health': rows[6],
                    'transport': rows[7],
                    'education_services': rows[10],
                    'other': rows[12]
                })
            elif rows[13] == "2024":
                cpi_2024.append({
                    'periode': rows[0],
                    'food_n_beverages': rows[2],
                    'clothing_footwear': rows[3],
                    'house_water_electricity': rows[4],
                    'health': rows[6],
                    'transport': rows[7],
                    'education_services': rows[10],
                    'other': rows[12]
                })

    with open('./data/cpi/cpi_2020.csv', 'w', newline='') as cpi2020:
        writer = csv.DictWriter(cpi2020, fieldnames=field)
        writer.writeheader()
        writer.writerows(cpi_2020)
    
    with open('./data/cpi/cpi_2021.csv', 'w', newline='') as cpi2021:
        writer = csv.DictWriter(cpi2021, fieldnames=field)
        writer.writeheader()
        writer.writerows(cpi_2021)
    
    with open('./data/cpi/cpi_2022.csv', 'w', newline='') as cpi2022:
        writer = csv.DictWriter(cpi2022, fieldnames=field)
        writer.writeheader()
        writer.writerows(cpi_2022)
    
    with open('./data/cpi/cpi_2023.csv', 'w', newline='') as cpi2023:
        writer = csv.DictWriter(cpi2023, fieldnames=field)
        writer.writeheader()
        writer.writerows(cpi_2023)

    with open('./data/cpi/cpi_2024.csv', 'w', newline='') as cpi2024:
        writer = csv.DictWriter(cpi2024, fieldnames=field)
        writer.writeheader()
        writer.writerows(cpi_2024)
        
def getMean():
    i2024 = []
    i2023 = []
    i2022 = []
    i2021 = []
    i2020 = []
    with open('./data/inflation/inflation_accumulation.csv', 'r') as f:
        plot = csv.reader(f, delimiter=',')
        for rows in plot:
            if rows[0]  == '2024':
                i2024.append(float(rows[1]))
            elif rows[0]  == '2023':
                i2023.append(float(rows[1]))
            elif rows[0]  == '2022':
                i2022.append(float(rows[1]))
            elif rows[0] == '2021':
                i2021.append(float(rows[1]))
            elif rows[0] == '2020':
                i2020.append(float(rows[1]))

    with open('./data/inflation/mean_inflation.csv', 'w', newline='') as fs:
        mean = [{
            'tahun': "2024",
            'rata_rata': (math.fsum(i2024) / 3)
        }, {
            'tahun': "2023",
            'rata_rata': (math.fsum(i2023) / 12)
        }, {
            'tahun': "2022",
            'rata_rata': (math.fsum(i2022) / 12)
        }, {
            'tahun': "2021",
            'rata_rata': (math.fsum(i2021) / 12)
        }, {
            'tahun': "2020",
            'rata_rata': (math.fsum(i2020) / 12)
        }]

        writer = csv.DictWriter(fs, fieldnames=['tahun', 'rata_rata'])
        writer.writeheader()
        writer.writerows(mean)