import csv

def db_lookup(file, lookup_key):
    with open(file, "r") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        if row[0] == lookup_key:
            return row[1]
    return None

def get_keys(file):
    keys = []
    with open(file, "r") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        keys.append(row[0])
    return keys

def write_file(file, key, value):
    with open(file, mode='w') as data:
        analyst_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        analyst_writer.writerow([key, value])
