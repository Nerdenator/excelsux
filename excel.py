from openpyxl import load_workbook
import timeit
import csv
import pandas as pd

def read_in_xlsx_openpyxl():
    try:
        wb = load_workbook(filename='randoms.xlsx')
    except Exception as ex:
        print(ex)

def read_in_file_csv():
    with open('randoms.csv') as csvfile:
        randomreader = csv.reader

def read_in_xls_pandas_python_dataset():
    df = pd.read_excel('randoms.xls')

def read_in_xls_pandas_dataframe():
    pass
# def main():
#
#     timeit.timeit('read_in_xlsx_openpyxl()')

# if __name__ == '__main__':
#     print(timeit.timeit("read_in_file_csv()", setup='from __main__ import read_in_csv_file'))
print("CSV read-in:")
print(timeit.timeit(read_in_file_csv, number=1000))
print("XLSX read-in:")
print(timeit.timeit(read_in_xlsx_openpyxl, number=1000))
print("XLS read-in:")
print(timeit.timeit(read_in_xls_pandas_python_dataset, number=1000))