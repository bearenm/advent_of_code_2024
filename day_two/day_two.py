import os

def main():
    try:
        list_of_reports = readInFile()
    except FileNotFoundError:
        print(f"No file named input.txt found in the current directory: {os.getcwd()}")
        return
    safe_reports = safeListCount(list_of_reports)
    print(f"The number of safe reports is {safe_reports}")

def readInFile():
    list_of_reports = []
    with open("input.txt", 'r') as file:
        for row in file:
            list_of_reports.append([int(x) for x in row.split()])
    return list_of_reports

def sortedChecker(report):
    path_count = {"increasing": 0, "decreasing": 0, "same": 0}

    for item in range(len(report) - 1):
        if report[item] < report[item + 1]:
            path_count["increasing"] += 1
        elif report[item] > report[item + 1]:
            path_count["decreasing"] += 1
        else:
            path_count["same"] += 1

    if path_count["same"] > 0:
        return 0  # If any adjacent levels are the same, it's not sorted.
    
    if path_count["increasing"] == len(report) - 1 or path_count["decreasing"] == len(report) - 1:
        return 1
    return 0

def incrementChecker(report):
    for item in range(len(report) - 1):
        if not 1 <= abs(report[item] - report[item + 1]) <= 3:
            return 0
    return 1

def canBeSafeWithOneRemoval(report):
    for item in range(len(report)):
        modified_report = report[:item] + report[item + 1:]
        if sortedChecker(modified_report) and incrementChecker(modified_report):
            return 1
    return 0

def safeListCount(list_of_reports):
    safe_count = 0
    for report in list_of_reports:
        sort_test = sortedChecker(report)
        increment_test = incrementChecker(report)
        if sort_test == 1 and increment_test == 1:
            safe_count += 1
        elif canBeSafeWithOneRemoval(report):
            safe_count += 1
    return safe_count

if __name__ == '__main__':
    main()
