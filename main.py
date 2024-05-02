import sys
from Inflasi import business_understanding as business
from Inflasi import data_preparation as dt
from Inflasi import data_visualization as dv

command = sys.argv

if command[1] == "show_info":
    business.showInfoData()
elif command[1] == "generate_data_preparation":
    dt.generate_data()
elif command[1] == "show_dataframe":
    print(business.showDataFrame().to_string(index=False))
elif command[1] == "generate_mean":
    dt.getMean()
elif command[1] == "graph_2024":
    dv.showGraph2024Inflation()
elif command[1] == "graph_2023":
    dv.showGraph2023Inflation()
elif command[1] == "graph_2022":
    dv.showGraph2022Inflation()
else:
    print('sorry your command invalid')