import csv
with open('dep.csv', 'r') as f:
    reader = csv.reader(f)

    with open('odd.csv', 'w', newline='') as odd:
        odd_writer = csv.writer(odd)

        with open('even.csv', 'w', newline='') as even:
            even_writer = csv.writer(even)
            i = 1
            for row in reader:
                if i % 2 == 1:
                    odd_writer.writerow(row)
                else:
                    even_writer.writerow(row)
                i += 1

    with open('odd.csv', 'r') as odd:
        reader = csv.reader(odd)
        print("Odd rows:")
        for row in reader:
            print(row)

    with open('even.csv', 'r') as even:
        reader = csv.reader(even)
        print("Even rows:")
        for row in reader:
            print(row)