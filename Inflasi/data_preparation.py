import csv
import math
from operator import itemgetter

inflasi_2024 = []
inflasi_2023 = []
inflasi_2022 = []
inflasi_2021 = []
inflasi_2020 = []
calculation = []

fields = ['bulan', 'nilai_inflasi']
field_calculation = ['tahun', 'nilai']

def generate_data():
    with open('./data/inflasi-rupiah.csv', 'r') as f:
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

    with open('./data/inflasi_rupiah_2024.csv', 'w', newline='') as dt2024:
        writer = csv.DictWriter(dt2024, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2024)

    with open('./data/inflasi_rupiah_2023.csv', 'w', newline='') as dt2023:
        writer = csv.DictWriter(dt2023, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2023)

    with open('./data/inflasi_rupiah_2022.csv', 'w', newline='') as dt2022:
        writer = csv.DictWriter(dt2022, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2022)

    with open('./data/inflasi_rupiah_2021.csv', 'w', newline='') as dt2021:
        writer = csv.DictWriter(dt2021, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2021)

    with open('./data/inflasi_rupiah_2020.csv', 'w', newline='') as dt2020:
        writer = csv.DictWriter(dt2020, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inflasi_2020)

    with open('./data/inflation_accumulation.csv', 'w', newline='') as dtaccumulation:
        writer = csv.DictWriter(dtaccumulation, fieldnames=field_calculation)
        writer.writeheader()
        writer.writerows(calculation)


def getMean():
    i2024 = []
    i2023 = []
    i2022 = []
    i2021 = []
    i2020 = []
    with open('./data/inflation_accumulation.csv', 'r') as f:
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

    with open('./data/mean_inflation.csv', 'w', newline='') as fs:
        mean = [{
            'tahun': 2024,
            'rata_rata': math.fsum(i2024)
        }, {
            'tahun': 2023,
            'rata_rata': math.fsum(i2023)
        }, {
            'tahun': 2022,
            'rata_rata': math.fsum(i2022)
        }, {
            'tahun': 2021,
            'rata_rata': math.fsum(i2021)
        }, {
            'tahun': 2020,
            'rata_rata': math.fsum(i2020)
        }]

        writer = csv.DictWriter(fs, fieldnames=['tahun', 'rata_rata'])
        writer.writeheader()
        writer.writerows(mean)