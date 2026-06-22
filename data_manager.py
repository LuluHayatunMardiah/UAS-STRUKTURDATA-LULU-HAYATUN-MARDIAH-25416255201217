import csv

FILE = "tiket.csv"

def load_data():
    try:
        with open(FILE, "r") as f:
            return list(csv.reader(f))
    except:
        return []

def save_data(data):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)