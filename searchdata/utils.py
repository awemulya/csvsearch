import csv


def search(csv_file, first_name, last_name, phone, address):
    with open(csv_file, 'rt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            if first_name == row[0] and last_name == row[1] and address == row[2] and phone == row[3]:
                return True
    return False