import csv
from Winner import Winner

def main():
    with open('archive.csv', newline='') as f:
    #with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

a = Winner('2016', 'Physics', 'The Nobel Prize in Physics 2016', '"for theoretical discoveries of topological phase transitions and topological phases of matter"', '1/4', '930', 'Individual', 'J. Michael Kosterlitz', '1943-06-22', 'Aberdeen', 'United Kingdom', 'Male', 'Brown University', 'Providence, RI', 'United States of America', '', '', '')





if __name__ == "__main__":
    main()
