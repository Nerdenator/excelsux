from openpyxl import load_workbook
import timeit


def main():
    print_everything()


def print_everything():
    wb = load_workbook('Book.xlsx')
    # get the "active" worksheet, whatever that is (ambiguous)
    ws = wb.active
    # you can hardcode it, but what if it's changed? process is broken
    #tuple_o_values = tuple(ws.values)
    # that's a bunch of numbers, right? wrong. it's '=RAND()' or None, over and over again.
    #print(tuple_o_values)
    for row in ws.values:
        for value in row:
            print(value)
    #print(len(tuple_o_values))


if __name__ == '__main__':
    main()

