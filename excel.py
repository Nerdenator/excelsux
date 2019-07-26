from openpyxl import load_workbook
import timeit
import csv
import pandas as pd

def read_in_xlsx_openpyxl():
    wb = load_workbook(filename='randoms.xlsx')
    return wb

def read_in_xlsx_pandas():
    df = pd.read_excel('randoms.xlsx')
    return df

def read_in_file_csv():
    with open('randoms.csv') as csvfile:
        randomreader = csv.reader(csvfile)
        return randomreader

def read_in_xls_pandas_python_dataset():
    df = pd.read_excel('randoms.xls')
    return df

def read_in_xls_pandas_dataframe():
    pass

print("CSV read-in, stdlib csv:")
print(timeit.timeit(read_in_file_csv, number=1000))
csv_reader = read_in_file_csv()
for row in csv_reader:
    print(row)
print("XLSX read-in, openpyxl:")
print(timeit.timeit(read_in_xlsx_openpyxl, number=1000))
print("XLS read-in, pandas:")
print(timeit.timeit(read_in_xls_pandas_python_dataset, number=1000))
print("XLSX read-in, pandas:")
print(timeit.timeit(read_in_xlsx_pandas, number=1000))