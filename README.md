## 🔍 Pengecekan Kata Diduga Typo

Dalam proyek ini, terdapat file `kata_diduga_typo.json` yang menyimpan daftar kata-kata yang dicurigai sebagai **typo**.

📄 **Lokasi file:**
data/kata_diduga_typo.json


File ini digunakan untuk mencari kata-kata bermasalah di korpus hasil penyempurnaan yang berada dalam folder:
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
