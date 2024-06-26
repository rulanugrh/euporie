import sys
from Inflasi import business_understanding as business
from Inflasi import data_preparation as dt
from Inflasi import data_visualization as dv
from typing import List
from tabulate import tabulate

def helpCommand():
    helps = [
        ["help", "print help command"],
        ["show", "showing about info dataframe or graph [inflation / cpi / graph]"],
        ["generate", "generated preparation data or mean data"]
    ]

    head = ["flag", "description"]
    print(tabulate(helps, headers=head, tablefmt="grid"))

def helpShow():
    helps = [
        ["inflation", "show about info or dataframe", "ex. python main.py show inflation [ info / dataframe ]"],        
        ["cpi", "show about info or dataframe", "ex. python main.py show cpi [ info / dataframe ]"],
        ["graph inflation", "show graph inflation", "ex. python main.py show graph inflation [ 2020 / 2021 / 2022 / 2023 / 2024 / mean / all ]"],
        ["graph cpi", "show graph cpi", "ex. python main.py show graph cpi [ 2020 / 2021 / 2022 / 2023 / 2024 / all ]"]

    ]

    head = ["flag", "description", "example usage"]
    print(tabulate(helps, headers=head, tablefmt="grid"))

def helpGenerate():
    helps = [
        ["inflation", "generated data preparation inflation", "ex. python main.py generated inflation [ preparation / mean ]"],
        ["cpi", "generated data preparation cpi", "ex. python main.py generated inflation [ preparation ]"],        

    ]

    head = ["flag", "description", "example usage"]
    print(tabulate(helps, headers=head, tablefmt="grid"))
def main(command: List[str]):
    if command[1] == "show":
        if command[2] == "inflation":
            if command[3] == "info":
                business.showInfoData()
            elif command[3] == "dataframe":
                print(business.showDataFrame().to_string(index=False))
        elif command[2] == "cpi":
            if command[3] == "info":
                business.showInfoCPI()
            elif command[3] == "dataframe":
                print(business.showDataFrameCPI().to_string(index=False))
        elif command[2] == "graph":
            if command[3] == "inflation":
                if command[4] == "2024":
                    dv.showGraph2024Inflation()
                elif command[4] == "2023":
                    dv.showGraph2023Inflation()
                elif command[4] == "2022":
                    dv.showGraph2022Inflation()
                elif command[4] == "2021":
                    dv.showGraph2021Inflation()
                elif command[4] == "2020":
                    dv.showGraph2020Inflation()
                elif command[4] == "mean":
                    dv.showGraphMeanInflation()
                elif command[4] == "all":
                    dv.showInflationAll()
            elif command[3] == "cpi":
                if command[4] == "2024":
                    dv.showCPI2024()
                elif command[4] == "2023":
                    dv.showCPI2023()
                elif command[4] == "2022":
                    dv.showCPI2022()
                elif command[4] == "2021":
                    dv.showCPI2021()
                elif command[4] == "2020":
                    dv.showCPI2020()
                elif command[4] == "all":
                    dv.showCPIAll()
        else:
            helpShow()
    elif command[1] == "generate":
        if command[2] == "inflation":
            if command[3] == "preparation":
                dt.generate_data()
            elif command[3] == "mean":
                dt.getMean()
        if command[2] == "cpi":
            if command[3] == "preparation":
                dt.generateDataCPI()
        else:
            helpGenerate()
    else:
        helpCommand()

if __name__ == "__main__":
    command = sys.argv
    main(command=command)