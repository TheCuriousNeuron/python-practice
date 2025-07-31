import csv
with open('grades.csv') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['M1'],row['M2'],row['M3'])