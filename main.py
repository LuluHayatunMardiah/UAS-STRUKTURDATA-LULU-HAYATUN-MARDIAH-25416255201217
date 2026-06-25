import csv
from collections import deque

TIKET_FILE = "tiket.csv"
PESAN_FILE = "pemesanan.csv"

# =========================
# LOAD & SAVE TIKET
# =========================
def load_tiket():
    try:
        with open(TIKET_FILE, "r", newline="") as f:
            return list(csv.DictReader(f))
    except:
        return []

def save_tiket(data):
    with open(TIKET_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id_tiket", "tujuan", "harga"])
        writer.writeheader()
        writer.writerows(data)

# =========================
# LOAD & SAVE PESANAN
# =========================
def load_pesanan():
    try:
        with open(PESAN_FILE, "r", newline="") as f:
            return deque(csv.DictReader(f))
    except:
        return deque()

def save_pesanan(queue):
    with open(PESAN_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nama", "id_tiket", "tujuan", "harga"])
        writer.writeheader()
        writer.writerows(list(queue))

# =========================
# CRUD TIKET
# =========================
def tampil_tiket():
    data = load_tiket()
    if not data:
        print("Data kosong")
        return

    print("\nID | Tujuan | Harga")
    print("----------------------")
    for t in data:
        print(t["id_tiket"], t["tujuan"], t["harga"])

def tambah_tiket():
    data = load_tiket()

    data.append({
        "id_tiket": input("ID Tiket: "),
        "tujuan": input("Tujuan: "),
        "harga": input("Harga: ")
    })

    save_tiket(data)
    print("Tiket ditambah")

def hapus_tiket():
    data = load_tiket()
    id_tiket = input("ID yang dihapus: ")

    data = [t for t in data if t["id_tiket"] != id_tiket]

    save_tiket(data)
    print("Tiket dihapus")

# =========================
# SEARCH
# =========================
def cari_tiket():
    key = input("Cari tujuan: ")
    data = load_tiket()

    for t in data:
        if key.lower() in t["tujuan"].lower():
            print(t)

# =========================
# SORT (BUBBLE)
# =========================
def sort_tiket():
    data = load_tiket()
    n = len(data)

    for i in range(n):
        for j in range(n-1):
            if int(data[j]["harga"]) > int(data[j+1]["harga"]):
                data[j], data[j+1] = data[j+1], data[j]

    for t in data:
        print(t)

# =========================
# PESAN TIKET (QUEUE)
# =========================
def pesan(queue):
    data = load_tiket()

    nama = input("Nama: ")
    id_tiket = input("ID Tiket: ")

    tiket = None
    for t in data:
        if t["id_tiket"] == id_tiket:
            tiket = t
            break

    if not tiket:
        print("Tiket tidak ditemukan")
        return

    queue.append({
        "nama": nama,
        "id_tiket": tiket["id_tiket"],
        "tujuan": tiket["tujuan"],
        "harga": tiket["harga"]
    })

    save_pesanan(queue)
    print("Pesanan berhasil")

# =========================
# LIHAT PESANAN
# =========================
def tampil_pesanan(queue):
    if not queue:
        print("Kosong")
        return

    for p in queue:
        print(p)

# =========================
# PROSES PESANAN
# =========================
def proses(queue):
    if queue:
        queue.popleft()
        save_pesanan(queue)
        print("Diproses")
    else:
        print("Kosong")

# =========================
# MENU
# =========================
def menu():
    queue = load_pesanan()

    while True:
        print("\n===== SISTEM TIKET =====")
        print("1. Tampil Tiket")
        print("2. Tambah Tiket")
        print("3. Hapus Tiket")
        print("4. Cari Tiket")
        print("5. Sort Tiket")
        print("6. Pesan Tiket")
        print("7. Tampil Pesanan")
        print("8. Proses Pesanan")
        print("0. Keluar")

        p = input("Pilih: ")

        if p == "1":
            tampil_tiket()
        elif p == "2":
            tambah_tiket()
        elif p == "3":
            hapus_tiket()
        elif p == "4":
            cari_tiket()
        elif p == "5":
            sort_tiket()
        elif p == "6":
            pesan(queue)
        elif p == "7":
            tampil_pesanan(queue)
        elif p == "8":
            proses(queue)
        elif p == "0":
            break

if __name__ == "__main__":
    menu()