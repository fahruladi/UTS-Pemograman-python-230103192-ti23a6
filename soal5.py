import csv, json, os, logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

try:
    os.makedirs("data", exist_ok=True)
    logging.info("Folder 'data' siap digunakan.")

    data_presensi = [
        {"nim": "23001", "nama": "Ali", "hadir_uts": 1},
        {"nim": "23002", "nama": "Budi", "hadir_uts": 0},
        {"nim": "23003", "nama": "Citra", "hadir_uts": 1}
    ]

    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nim", "nama", "hadir_uts"])
        writer.writeheader()
        writer.writerows(data_presensi)
    logging.info("Data CSV berhasil disimpan.")

    with open("data/presensi.csv") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    total = len(data)
    hadir = sum(int(d["hadir_uts"]) for d in data)
    persentase = hadir / total * 100

    ringkasan = {"total": total, "hadir": hadir, "persentase": persentase}

    with open("data/ringkasan.json", "w") as f:
        json.dump(ringkasan, f, indent=4)
    logging.info("Ringkasan JSON berhasil disimpan.")

except Exception as e:
    logging.error(f"Terjadi kesalahan: {e}")
