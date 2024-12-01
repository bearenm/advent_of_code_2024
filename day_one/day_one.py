'''

Advent of Code Day One - Historian Hysteria

'''

import csv

def main():
    list_one, list_two = fileRead("input.txt")
    list_one.sort()
    list_two.sort()
    differences = computeDifferences(list_one, list_two)
    similiarities = computeSimilarity(list_one, list_two)
    print(f"Total difference score is: {differences}")
    print(f"Total similarity score is: {similiarities}")

def fileRead(filename):
    list_one, list_two = [], []
    with open(filename, "r") as file:
        input_data = csv.reader(file, delimiter=" ")
        for row in input_data:
            list_one.append(row[0])
            list_two.append(row[3])

        return list_one, list_two

def computeDifferences(list_one, list_two):
    differences = []
    for x in range(0, len(list_one)):
        differences.append(abs(int(list_one[x]) - int(list_two[x])))
    return sum(differences)

def computeSimilarity(list_one, list_two):
    number_count = {}
    similiarities = []
    for x in list_two:
        if x in number_count:
            number_count[x] += 1
        else:
            number_count[x] = 1
    for x in list_one:
        if x in number_count:
            similiarities.append(int(x) * int(number_count[x]))
    return sum(similiarities)

if __name__ == "__main__":
    main()