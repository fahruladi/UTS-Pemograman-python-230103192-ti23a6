def jadwal_hari(hari):
    jadwal = {
        "Senin": ["Basis Data", "Aljabar Linear"],
        "Selasa": ["Pemrograman Python", "Jaringan Komputer"],
        "Rabu": ["Sistem Operasi", "Kewirausahaan"]
    }

    if hari in jadwal:
        return jadwal[hari]
    else:
        return ["Tidak ada jadwal"]

print(jadwal_hari())
