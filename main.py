import csv
from collections import deque

TIKET_FILE = "tiket.csv"
PESAN_FILE = "pemesanan.csv"

# =========================
# NODE + LINKED LIST
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
        if self.head is None:
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
# CSV HANDLER
# =========================
def load_tiket():
    ll = LinkedList()
    try:
        with open(TIKET_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ll.append(row)
    except FileNotFoundError:
        pass
    return ll


def save_tiket(data_list):
    with open(TIKET_FILE, "w", newline="") as file:
        fieldnames = ["id", "tujuan", "harga"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)


def load_pesanan():
    q = deque()
    try:
        with open(PESAN_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                q.append(row)
    except FileNotFoundError:
        pass
    return q


def save_pesanan(queue):
    with open(PESAN_FILE, "w", newline="") as file:
        fieldnames = ["nama", "id_tiket"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(queue)


# =========================
# SEARCH (LINEAR SEARCH)
# =========================
def search_tiket(data, keyword):
    hasil = []
    for item in data:
        if keyword.lower() in item["tujuan"].lower():
            hasil.append(item)
    return hasil


# =========================
# SORTING (BUBBLE SORT)
# =========================
def sort_tiket(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(data[j]["harga"]) > int(data[j + 1]["harga"]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# =========================
# CRUD TIKET
# =========================
def tampil_tiket():
    data = load_tiket().to_list()
    if not data:
        print("Data kosong")
        return
    for t in data:
        print(t)


def tambah_tiket():
    data = load_tiket().to_list()
    id = input("ID: ")
    tujuan = input("Tujuan: ")
    harga = input("Harga: ")

    data.append({"id": id, "tujuan": tujuan, "harga": harga})
    save_tiket(data)
    print("Tiket berhasil ditambah")


def update_tiket():
    data = load_tiket().to_list()
    id = input("ID tiket yang diubah: ")

    for t in data:
        if t["id"] == id:
            t["tujuan"] = input("Tujuan baru: ")
            t["harga"] = input("Harga baru: ")
            save_tiket(data)
            print("Berhasil diupdate")
            return
    print("Data tidak ditemukan")


def delete_tiket():
    data = load_tiket().to_list()
    id = input("ID tiket yang dihapus: ")

    data = [t for t in data if t["id"] != id]
    save_tiket(data)
    print("Berhasil dihapus")


# =========================
# PEMESANAN (QUEUE)
# =========================
def pesan_tiket(queue):
    nama = input("Nama: ")
    id_tiket = input("ID Tiket: ")

    queue.append({"nama": nama, "id_tiket": id_tiket})
    save_pesanan(queue)
    print("Pesanan masuk antrian")


def tampil_pesanan(queue):
    if not queue:
        print("Belum ada pesanan")
        return
    for p in queue:
        print(p)


def hapus_pesanan(queue):
    if queue:
        queue.popleft()
        save_pesanan(queue)
        print("Pesanan diproses (FIFO)")
    else:
        print("Antrian kosong")


# =========================
# MENU
# =========================
def menu():
    queue = load_pesanan()

    while True:
        print("\n===== SISTEM TIKET =====")
        print("1. Tampil Tiket")
        print("2. Tambah Tiket")
        print("3. Update Tiket")
        print("4. Hapus Tiket")
        print("5. Cari Tiket")
        print("6. Urutkan Tiket")
        print("7. Pesan Tiket")
        print("8. Tampil Pesanan")
        print("9. Proses Pesanan")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampil_tiket()

        elif pilih == "2":
            tambah_tiket()

        elif pilih == "3":
            update_tiket()

        elif pilih == "4":
            delete_tiket()

        elif pilih == "5":
            key = input("Cari tujuan: ")
            hasil = search_tiket(load_tiket().to_list(), key)
            print(hasil)

        elif pilih == "6":
            data = sort_tiket(load_tiket().to_list())
            for d in data:
                print(d)

        elif pilih == "7":
            pesan_tiket(queue)

        elif pilih == "8":
            tampil_pesanan(queue)

        elif pilih == "9":
            hapus_pesanan(queue)

        elif pilih == "0":
            break


if __name__ == "__main__":
    menu()