from random import random, sample
from random import seed
from random import randint
from random import choice
import csv


def main():
    with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
