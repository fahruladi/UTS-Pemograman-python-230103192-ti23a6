s1 = int(input("Setoran 1: "))
s2 = int(input("Setoran 2: "))
s3 = int(input("Setoran 3: "))

if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid")
else:
    total = s1 + s2 + s3

    if total < 300000:
        print("Rendah")
    elif total < 600000:
        print("Sedang")
    else:
        print("Tinggi")
