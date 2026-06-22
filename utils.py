def cari_tiket(data, keyword):
    hasil = []
    for row in data:
        if keyword.lower() in row[1].lower():
            hasil.append(row)
    return hasil


def sort_jadwal(data):
    return sorted(data, key=lambda x: x[2])