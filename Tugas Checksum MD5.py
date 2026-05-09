import hashlib

def buat_hash_md5(nama, email, nomor_hp):
    """Menggabungkan data profil dan menghasilkan hash MD5."""
    data_gabung = f"{nama}|{email}|{nomor_hp}"
    hash_md5 = hashlib.md5(data_gabung.encode()).hexdigest()
    return hash_md5, data_gabung

def tampilkan_header(judul):
    print("\n" + "=" * 50)
    print(f"  {judul}")
    print("=" * 50)

# INPUT DATA AWAL
tampilkan_header("INPUT DATA PROFIL AWAL")
print("Masukkan data profil user:")
nama_awal    = input("  Nama      : ")
email_awal   = input("  Email     : ")
hp_awal      = input("  Nomor HP  : ")

hash_awal, data_awal = buat_hash_md5(nama_awal, email_awal, hp_awal)

print("\nData tersimpan.")
print(f"   Data Profil : {data_awal}")
print(f"   Hash MD5    : {hash_awal}")

# INPUT DATA BARU (SIMULASI PERUBAHAN)
tampilkan_header("INPUT DATA PROFIL BARU")
print("Masukkan data profil baru (tekan Enter jika tidak berubah):")

nama_baru  = input(f"  Nama      [{nama_awal}] : ") or nama_awal
email_baru = input(f"  Email     [{email_awal}] : ") or email_awal
hp_baru    = input(f"  Nomor HP  [{hp_awal}] : ") or hp_awal

hash_baru, data_baru = buat_hash_md5(nama_baru, email_baru, hp_baru)

# PERBANDINGAN HASH
tampilkan_header("HASIL PERBANDINGAN HASH MD5")
print(f"  Data Lama   : {data_awal}")
print(f"  Hash Lama   : {hash_awal}")
print()
print(f"  Data Baru   : {data_baru}")
print(f"  Hash Baru   : {hash_baru}")
print()

# STATUS PERUBAHAN
print("-" * 50)
if hash_awal == hash_baru:
    print("STATUS : Data TIDAK berubah. Integritas terjaga.")
else:
    print("STATUS : Data TELAH BERUBAH / dimodifikasi!")
    # Deteksi field mana yang berubah
    perubahan = []
    if nama_awal  != nama_baru:  perubahan.append(f"Nama      : '{nama_awal}' → '{nama_baru}'")
    if email_awal != email_baru: perubahan.append(f"Email     : '{email_awal}' → '{email_baru}'")
    if hp_awal    != hp_baru:    perubahan.append(f"Nomor HP  : '{hp_awal}' → '{hp_baru}'")
    print("   Field yang berubah:")
    for p in perubahan:
        print(f"   • {p}")
print("-" * 50)
