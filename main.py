import csv

# =========================
# FILE
# =========================
TIKET_FILE = "tiket.csv"
PESAN_FILE = "pemesanan.csv"

# =========================
# LINKED LIST
# =========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

# =========================
# QUEUE
# =========================
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

queue = Queue()

# =========================
# LOAD TIKET (CSV → Linked List)
# =========================
def load_tiket():
    ll = LinkedList()
    try:
        with open(TIKET_FILE, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ll.append(row)
    except FileNotFoundError:
        print("File tiket.csv tidak ditemukan!")
    return ll

# =========================
# READ TIKET
# =========================
def show_tiket():
    data = load_tiket().to_list()
    print("\n=== DAFTAR TIKET ===")
    for d in data:
        print(d)

# =========================
# CREATE PESANAN
# =========================
def pesan_tiket():
    nama = input("Nama pemesan: ")
    id_tiket = input("ID tiket: ")
    jumlah = input("Jumlah tiket: ")

    data = [nama, id_tiket, jumlah, "terpesan"]

    queue.enqueue(data)

    with open(PESAN_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    print("✔ Pemesanan berhasil!")

# =========================
# READ PESANAN
# =========================
def show_pesanan():
    print("\n=== DATA PESANAN ===")
    try:
        with open(PESAN_FILE, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Belum ada data pemesanan.")

# =========================
# DELETE PESANAN
# =========================
def delete_pesanan():
    nama = input("Nama pemesan yang dihapus: ")

    rows = []
    found = False

    try:
        with open(PESAN_FILE, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != nama:
                    rows.append(row)
                else:
                    found = True
    except FileNotFoundError:
        print("File belum ada!")
        return

    with open(PESAN_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("✔ Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

# =========================
# SEARCH TIKET
# =========================
def search_tiket():
    keyword = input("Cari tujuan: ").lower()
    data = load_tiket().to_list()

    hasil = [d for d in data if keyword in d["nama_tujuan"].lower()]

    print("\n=== HASIL SEARCH ===")
    for h in hasil:
        print(h)

# =========================
# SORTING HARGA
# =========================
def sort_tiket():
    data = load_tiket().to_list()
    data.sort(key=lambda x: int(x["harga"]))

    print("\n=== TIKET TERMURAH - TERMAHAL ===")
    for d in data:
        print(d)

# =========================
# MENU
# =========================
def menu():
    while True:
        print("\n===== SISTEM PEMESANAN TIKET =====")
        print("1. Lihat Tiket")
        print("2. Pesan Tiket")
        print("3. Lihat Pesanan")
        print("4. Hapus Pesanan")
        print("5. Cari Tiket")
        print("6. Urutkan Tiket")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            show_tiket()
        elif pilih == "2":
            pesan_tiket()
        elif pilih == "3":
            show_pesanan()
        elif pilih == "4":
            delete_pesanan()
        elif pilih == "5":
            search_tiket()
        elif pilih == "6":
            sort_tiket()
        elif pilih == "0":
            print("Keluar...")
            break
        else:
            print("Menu tidak valid!")

# RUN
menu()