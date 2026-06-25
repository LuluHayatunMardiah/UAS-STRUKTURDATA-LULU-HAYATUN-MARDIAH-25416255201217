import csv
from collections import deque

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

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


# =========================
# LOAD TIKET
# =========================
def load_tiket():
    data = []
    try:
        with open(TIKET_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("tiket.csv tidak ditemukan")
    return data


def save_tiket(data):
    with open(TIKET_FILE, "w", newline="") as file:
        fieldnames = ["id_tiket", "tujuan", "harga"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# =========================
# QUEUE (PESANAN)
# =========================
def load_pesanan():
    q = deque()
    try:
        with open(PESAN_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                q.append(row)
    except FileNotFoundError:
        pass
    return q


def save_pesanan(queue):
    with open(PESAN_FILE, "w", newline="") as file:
        fieldnames = ["nama", "id_tiket", "tujuan", "harga"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list(queue))


# =========================
# TAMPIL TIKET
# =========================
def tampil_tiket():
    data = load_tiket()

    if not data:
        print("Data kosong")
        return

    ll = LinkedList()
    for d in data:
        ll.append(d)

    print("\n=== DATA TIKET ===")
    print("ID\tTujuan\tHarga")
    print("----------------------")

    current = ll.head
    while current:
        t = current.data
        print(f"{t['id_tiket']}\t{t['tujuan']}\t{t['harga']}")
        current = current.next


# =========================
# TAMBAH TIKET
# =========================
def tambah_tiket():
    data = load_tiket()

    id_tiket = input("ID Tiket: ")
    tujuan = input("Tujuan: ")
    harga = input("Harga: ")

    data.append({
        "id_tiket": id_tiket,
        "tujuan": tujuan,
        "harga": harga
    })

    save_tiket(data)
    print("Tiket berhasil ditambah")


# =========================
# UPDATE TIKET
# =========================
def update_tiket():
    data = load_tiket()
    id_tiket = input("ID yang diubah: ")

    for t in data:
        if t["id_tiket"] == id_tiket:
            t["tujuan"] = input("Tujuan baru: ")
            t["harga"] = input("Harga baru: ")
            save_tiket(data)
            print("Berhasil update")
            return

    print("ID tidak ditemukan")


# =========================
# DELETE TIKET
# =========================
def delete_tiket():
    data = load_tiket()
    id_tiket = input("ID yang dihapus: ")

    new_data = [t for t in data if t["id_tiket"] != id_tiket]

    if len(new_data) == len(data):
        print("ID tidak ditemukan")
        return

    save_tiket(new_data)
    print("Berhasil dihapus")


# =========================
# SEARCH
# =========================
def cari_tiket():
    key = input("Cari tujuan: ")
    data = load_tiket()

    ditemukan = False
    for t in data:
        if key.lower() in t["tujuan"].lower():
            print(t)
            ditemukan = True

    if not ditemukan:
        print("Tidak ditemukan")


# =========================
# SORT (BUBBLE SORT)
# =========================
def sort_tiket():
    data = load_tiket()
    n = len(data)

    for i in range(n):
        for j in range(n - 1):
            if int(data[j]["harga"]) > int(data[j + 1]["harga"]):
                data[j], data[j + 1] = data[j + 1], data[j]

    print("\n=== SORT HARGA ===")
    for t in data:
        print(t)


# =========================
# PESAN TIKET (QUEUE)
# =========================
def pesan_tiket(queue):
    data = load_tiket()

    nama = input("Nama: ")
    id_tiket = input("ID Tiket: ")

    tiket = None
    for t in data:
        if t["id_tiket"] == id_tiket:
            tiket = t
            break

    if tiket:
        queue.append({
            "nama": nama,
            "id_tiket": tiket["id_tiket"],
            "tujuan": tiket["tujuan"],
            "harga": tiket["harga"]
        })

        save_pesanan(queue)
        print("Pesanan berhasil")
    else:
        print("Tiket tidak ditemukan")


# =========================
# TAMPIL PESANAN
# =========================
def tampil_pesanan(queue):
    if not queue:
        print("Belum ada pesanan")
        return

    for p in queue:
        print(p)


# =========================
# PROSES PESANAN
# =========================
def proses_pesanan(queue):
    if queue:
        queue.popleft()
        save_pesanan(queue)
        print("Pesanan diproses")
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
        print("6. Sort Harga")
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
            cari_tiket()
        elif pilih == "6":
            sort_tiket()
        elif pilih == "7":
            pesan_tiket(queue)
        elif pilih == "8":
            tampil_pesanan(queue)
        elif pilih == "9":
            proses_pesanan(queue)
        elif pilih == "0":
            break


if __name__ == "__main__":
    menu()