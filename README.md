## 🔍 Pengecekan Kata Diduga Typo

Dalam proyek ini, terdapat file `kata_diduga_typo.json` yang menyimpan daftar kata-kata yang dicurigai sebagai **typo**.

📄 **Lokasi file:**
data/kata_diduga_typo.json


File ini digunakan untuk mencari kata-kata bermasalah baik inggris dan indonesia di korpus hasil penyempurnaan yang berada dalam folder:
./parallel_disempurnakan

---

## 🧭 Cara Melakukan Pengecekan di Visual Studio Code

Gunakan fitur **Search** di Visual Studio Code dengan langkah berikut:

1. Tekan `Ctrl + Shift + F` untuk membuka **Search Panel**
2. Masukkan kata yang ingin dicari (contoh: `vet`)
3. Pada bagian `files to include`, isi:
./parallel_disempurnakan
4. Tekan Enter untuk melihat hasilnya

---

## ✅ Contoh Hasil

...

Kata tersebut tampak seperti kesalahan ketik (typo) dan perlu divalidasi atau diperbaiki secara manual.

---

## 📊 Progress Pengecekan

Berikut adalah daftar progres pengecekan kata dalam file `kata_diduga_typo.json`:

| Rentang Kata | Status     |
|--------------|------------|
| 0 – 1067     | ✅ Selesai |
| 7442 – 7780  | ✅ Selesai |

tersisa 6.374 kata

> 💡 **Pro Tip!**  
> Jika kamu ingin memperbaiki kata yang ditemukan, pastikan kamu benar-benar yakin dengan perubahan tersebut.  
> File yang sedang kamu buka di Visual Studio Code bisa **tertutup otomatis** jika kata yang dicari sudah tergantikan seluruhnya.  
> Beberapa saran:
> - Catat atau ingat nama file yang sedang kamu buka
> - Lakukan commit per rentang kata untuk memudahkan pelacakan
> - Gunakan fitur undo/redo atau version control seperti Git untuk menghindari kehilangan revisi


## ⚙️ Catatan Otomatisasi (Untuk Skrip)

Jika kamu menemukan pola kesalahan yang berulang dan bisa diselesaikan dengan skrip, berikut catatan yang telah dibuat di:

📓 `notebooks/replacement.ipynb`

ikuti saja pola yang sudah saya buat

### Contoh Aturan:
- Jika `eng` adalah **"bid"** dan `indo` adalah **"tawaran"**, maka ubah menjadi `eng = bird`, `indo = burung`
- Jika `eng = bil` dan `indo = bil` → ganti menjadi `eng = bill`, `indo = paruh`
- Jika `eng` = **"birs", "bir"** dan `indo` = **"bir"** → ganti `eng = bird`, `indo = burung`
- Jika `eng = birth` dan `indo = kelahiran / lahir` → ubah ke `eng = bird`, `indo = burung`
- Cari kata **"black"** pada teks bahasa Indonesia untuk validasi warna
- Ganti kata: `brow`, `brows`, `eyebrow`, `eyebrows` → **superciliary**

> 💬 *Skrip atau pencocokan otomatis sangat membantu untuk mempercepat validasi dan normalisasi istilah.*
---

## 📘 Daftar Istilah Ornitologi & Padanan Bahasa Indonesia

Berikut adalah istilah-istilah ornitologi yang sering muncul dalam proyek ini (baik dalam dataset maupun dokumentasi), beserta arti atau padanan yang digunakan dalam bahasa Indonesia:

| Istilah Ornitologi      | Padanan Bahasa Indonesia                      |
|--------------------------|-----------------------------------------------|
| **superciliary**         | superciliary                                   |
| **malar stripe**         | garis malar                                     |
| **secondaries**          | bulu sekunder                                  |
| **tarsus**               | tarsus                                        |
| **vent**                 | lubang kloaka                                  |
| **rump**                 | pantat                                         |
| **nape**                 | tengkuk                                        |
| **primaries**            | bulu primer (utama di sayap)                   |
| **bill**                 | paruh                                          |

> 📝 *Catatan: Beberapa istilah (seperti `tarsus` atau `superciliary`) lebih baik dipertahankan dalam bentuk aslinya bila telah menjadi istilah baku dalam literatur ilmiah.*

> ❗ *TERDAPAT BANYAK TYPO, CONTOH UNTUK KATA **"YELLOW"**:*
> `yeallow`, `yelklow`, `yell`, `yelllow`, `yello`, `yelloe`, `yelloiw`, `yelloow`, `yellos`

---

Jika kamu menambahkan istilah baru atau melakukan validasi terjemahan di masa depan, bagian ini bisa diperbarui secara berkala untuk menjadi referensi glosarium proyek.



---
catatan pribadi
> paralel_cub_200_2011_captions.json -> caption asli dari penelitian yang menggunakan dataset CUB
> paralel_cub_200_2011_captions_disempurnakan.json -> replace terjemahan indo dengan hasil GT dari ibu uci
> paralel_cub_200_2011_captions_disempurnakan_updated.json -> dataset yang sedang dikerjakan (disempurnakan)
