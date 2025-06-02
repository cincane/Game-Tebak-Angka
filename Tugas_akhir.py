import random
# game tebak angka
# looping program berjalan
print("Selamat datang di game Tebak Angka")
while (True):
    level = input("Masukan level [easy/medium/hard/very hard] : ")
    while (level != "easy" and level != "medium" and level != "hard"):
        level = input(
            "\nMaaf inputan anda salah. Silahkan coba lagi. \nMasukan level [easy/medium/hard]: ")

    if level == "easy":
        kesempatan = 3
        bilangan_random = random.randint(1, 10)
        print("Angkanya dimulai dari 1 sampai 10")
    elif level == "medium":
        kesempatan = 5
        bilangan_random = random.randint(1, 25)
        print("Angkanya dimulai dari 1 sampai 25")
    elif level == "hard":
        kesempatan = 7
        bilangan_random = random.randint(1, 50)
        print("Angkanya dimulai dari 1 sampai 50")
    print("Level", level, "dengan kesempatan", kesempatan, "kali")


# looping tebak angka
    while (kesempatan >= 0):
        if kesempatan == 0:
            print("Mohon maaf anda gagal tebak angka")
            print("Jawaban yang benar adalah ", bilangan_random)
            break
        else:
            print("kesempatan", kesempatan)
            tebak = int(input("Masukan angka yang ditebak : "))
            if tebak == bilangan_random:
                print("wihhh pinter juga ni anak")
                break
            elif tebak > bilangan_random:
                print("Angkanya dibawah", tebak)
                kesempatan -= 1
            elif tebak < bilangan_random:
                print("Angkanya diatas", tebak)
                kesempatan -= 1

# konfirmasi ulang
    ulang = input("\nMau main lagi?[iya/tidak] : ")
    while (ulang != "iya" and ulang != "tidak"):
        ulang = input(
            "\nMaaf inputan anda salah. Silahkan input yang bener.\nMau main lagi? :")

    if ulang == "iya":
        print("\nSilahkan main lagi.\n")
    elif ulang == "tidak":
        print("\nTerimakasih sudah main tebak angka")
        break
