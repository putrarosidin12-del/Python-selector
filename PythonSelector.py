import os


def print_tengah(teks, warna=""):
    try:
        lebar = os.get_terminal_size().columns
    except OSError:#Jika tidak menggunakan terminal
        lebar = 80 
    print(warna + teks.center(lebar) + RESET)


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

# Tampilan pembuka
print_tengah("Selamat datang di kuis penentuan jurusan!", CYAN + BOLD)
print_tengah("Jawablah pertanyaan berikut dengan memilih nomor jawaban yang sesuai.\n", YELLOW)

# Fungsi kuis
def tanya_pertanyaan(pertanyaan, opsi, skor_jurusan):
    print_tengah(pertanyaan, BOLD)
    for i, item in enumerate(opsi, 1):
        print_tengah(f"{i}. {item}", BLUE)
    
    while True:
        try:
            jawaban = int(input(GREEN + "Pilih nomor jawaban (1-{}): ".format(len(opsi)) + RESET))
            if 1 <= jawaban <= len(opsi):
                break
            else:
                print_tengah("Pilih nomor yang valid.", RED)
        except ValueError:
            print_tengah("Masukkan nomor yang valid.", RED)
    
    for jurusan, skor in skor_jurusan[jawaban-1].items():
        skor_total[jurusan] += skor

# Inisialisasi skor
skor_total = {
    "Akuntansi": 0,
    "MPLB": 0,
    "BR": 0,
    "BD": 0,
    "DKV": 0,
    "RPL": 0,
    "TKJ": 0
}

# Daftar pertanyaan (gunakan list pertanyaan kamu sebelumnya)
pertanyaan_list = [
       {
        "pertanyaan": "Apa hobi utama kamu di waktu luang?",
        "opsi": ["Bermain game atau eksplorasi teknologi", "Menggambar atau membuat konten kreatif", "Membaca buku bisnis atau menghitung angka", "Berbelanja atau berinteraksi dengan orang", "Belajar tentang jaringan komputer", "Membuat aplikasi atau coding", "Mengelola keuangan pribadi"],
        "skor": [
            {"TKJ": 2, "RPL": 1},
            {"DKV": 2},
            {"Akuntansi": 2, "MPLB": 1},
            {"BR": 2, "BD": 1},
            {"TKJ": 2},
            {"RPL": 2},
            {"Akuntansi": 1, "MPLB": 1}
        ]
    },
    {
        "pertanyaan": "Apa yang ingin kamu ketahui lebih dalam?",
        "opsi": ["Cara kerja komputer dan internet", "Bahasa pemrograman dan algoritma", "Desain grafis dan visual", "Akuntansi dan keuangan", "Manajemen bisnis dan pemasaran", "Bisnis online dan e-commerce", "Teknik jaringan dan perbaikan perangkat"],
        "skor": [
            {"TKJ": 2},
            {"RPL": 2},
            {"DKV": 2},
            {"Akuntansi": 2},
            {"MPLB": 2, "BR": 1},
            {"BD": 2},
            {"TKJ": 2}
        ]
    },
    {
        "pertanyaan": "Apa kebiasaan sehari-hari kamu yang paling menonjol?",
        "opsi": ["Menggunakan gadget dan aplikasi", "Membuat sketsa atau edit foto", "Menghitung pengeluaran harian", "Berbelanja online atau offline", "Belajar coding atau troubleshooting", "Membaca artikel bisnis", "Merancang website atau game"],
        "skor": [
            {"TKJ": 1, "RPL": 1},
            {"DKV": 2},
            {"Akuntansi": 2},
            {"BR": 2, "BD": 1},
            {"TKJ": 2},
            {"MPLB": 2},
            {"RPL": 2, "BD": 1}
        ]
    },
    {
        "pertanyaan": "Jika kamu punya proyek pribadi, apa yang akan kamu buat?",
        "opsi": ["Aplikasi mobile atau website", "Poster atau desain branding", "Laporan keuangan atau budget", "Toko online kecil", "Sistem jaringan rumah", "Presentasi bisnis", "Game sederhana"],
        "skor": [
            {"RPL": 2},
            {"DKV": 2},
            {"Akuntansi": 2},
            {"BD": 2},
            {"TKJ": 2},
            {"MPLB": 2},
            {"RPL": 1, "DKV": 1}
        ]
    },
    {
        "pertanyaan": "Apa mata pelajaran favorit kamu di sekolah?",
        "opsi": ["Matematika atau IPA", "Seni atau Bahasa", "Ekonomi atau Akuntansi", "Bahasa Inggris atau Sosial", "Komputer atau Teknologi", "Bisnis atau Kewirausahaan", "Fisika atau Elektronika"],
        "skor": [
            {"RPL": 1, "TKJ": 1},
            {"DKV": 2},
            {"Akuntansi": 2},
            {"MPLB": 2},
            {"TKJ": 2, "RPL": 1},
            {"BR": 1, "BD": 1},
            {"TKJ": 2}
        ]
    }
]

# Loop kuis
for item in pertanyaan_list:
    tanya_pertanyaan(item["pertanyaan"], item["opsi"], item["skor"])
    print_tengah("-"*50, CYAN)
    print()  # spasi antar pertanyaan

# Menentukan jurusan cocok
skor_tertinggi = max(skor_total.values())
jurusan_cocok = [jurusan for jurusan, skor in skor_total.items() if skor == skor_tertinggi]

print_tengah("\nBerdasarkan jawaban kamu, jurusan yang cocok adalah:", GREEN + BOLD)
for jurusan in jurusan_cocok:
    print_tengah(f"- {jurusan}", YELLOW)

if len(jurusan_cocok) > 1:
    print_tengah("Kamu memiliki beberapa pilihan yang cocok. Pertimbangkan minat pribadi lebih lanjut.", CYAN)
