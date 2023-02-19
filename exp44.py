import csv
with open("dep.csv","r")as f:
    r=csv.reader(f)

    with open('newcsv.csv', 'w',newline='') as new:
        writer=csv.writer(new)
        for i in range(5):
            writer.writerow(next(r))

    with open('newcsv.csv', 'r') as new:
        r=csv.reader(new)
        for row in r:
            print(row)