from data_manager import load_data, save_data
from tiket import Tiket
from struktur_data import Queue, HashMap
from utils import cari_tiket, sort_jadwal

queue = Queue()
hashmap = HashMap()

data = load_data()

for row in data:
    if row:
        hashmap.set(row[0], row)


def tampilkan():
    print("\nDATA TIKET:")
    for row in data:
        print(row)


def create():
    id_tiket = input("ID: ")
    nama = input("Nama: ")
    jadwal = input("Jadwal: ")
    kursi = input("Kursi: ")

    tiket = Tiket(id_tiket, nama, jadwal, kursi)

    queue.enqueue(tiket)
    data.append(tiket.to_list())
    hashmap.set(id_tiket, tiket.to_list())

    save_data(data)
    print("Berhasil pesan tiket")


def delete():
    id_tiket = input("ID hapus: ")

    global data
    data = [d for d in data if d[0] != id_tiket]

    save_data(data)
    print("Tiket dihapus")


def search():
    keyword = input("Cari nama: ")
    hasil = cari_tiket(data, keyword)

    for h in hasil:
        print(h)


def sort():
    hasil = sort_jadwal(data)
    for r in hasil:
        print(r)


while True:
    print("""
1. Lihat
2. Pesan
3. Hapus
4. Cari
5. Sorting
0. Keluar
""")

    pilih = input("Pilih: ")

    if pilih == "1":
        tampilkan()
    elif pilih == "2":
        create()
    elif pilih == "3":
        delete()
    elif pilih == "4":
        search()
    elif pilih == "5":
        sort()
    elif pilih == "0":
        break