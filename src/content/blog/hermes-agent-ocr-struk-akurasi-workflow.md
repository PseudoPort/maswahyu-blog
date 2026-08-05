---
title: "3 Bulan Membaca Struk dengan Hermes Agent: Akurasi OCR, Error yang Saya Temukan, dan Workflow Final"
description: "Setelah 3 bulan scan struk pakai Hermes Agent: 214 struk diproses, 92% terbaca bersih, 5 gagal total. Ini error yang sering muncul, cara mengatasinya, dan workflow yang akhirnya saya pakai."
pubDate: 2026-08-06
heroImage: "../../assets/hero-hermes-agent-ocr-struk-akurasi-workflow.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# 3 Bulan Membaca Struk dengan Hermes Agent: Akurasi OCR, Error yang Saya Temukan, dan Workflow Final

Februari 2026, saya foto struk kopi sambil berdiri di kasir. Baru 10 hari pakai OCR di Hermes Agent, tapi sudah ada 87 struk masuk database. Yang saya ingat dari bulan itu bukan jumlah kopinya — justru struk yang gagal terbaca. Struk Indomaret dengan kertas thermal yang sudah buram. Struk parkir yang tercetak miring. Satu struk makan malam yang totalnya ketuker dengan nomor meja.

Artikel ini bukan tutorial setup — itu sudah saya tulis di artikel sebelumnya. Ini laporan lapangan: setelah 3 bulan, 214 struk, dan beberapa kali error bikin gregetan, ini yang saya pelajari soal OCR struk di Indonesia.

## Kenapa Saya Nekat Percaya OCR

Alasannya sepele: manual input itu lambat dan rawan salah. Satu struk butuh sekitar 3-4 menit kalau diketik rapi — tanggal, nama merchant, kategori, jumlah. Kalau terburu-buru, typo dijamin muncul. Manual data entry punya error rate sekitar 1-4% per entri menurut beberapa riset industri, dan itu terjadi persis di pekerjaan yang paling membosankan: menyalin angka dari kertas ke spreadsheet.

Target saya waktu itu: foto struk, biarkan agent yang baca, saya tinggal konfirmasi. Kedengarannya naif, tapi saya pilih mulai dari struk karena volume-nya tinggi dan polanya seragam.

## Cara Kerja yang Saya Pasang

Alurnya sederhana:

1. Foto struk lewat bot Telegram — biasanya pas baru keluar dari kasir
2. Agent kirim gambar ke mesin OCR. Saya pakai kombinasi [Tesseract](https://github.com/tesseract-ocr/tesseract) untuk teks lokal dan [Cloud Vision](https://cloud.google.com/vision/docs/ocr) untuk struk yang buram
3. Hasil parsing: tanggal, merchant, total, kategori
4. Preview muncul di chat: "Indomaret, 12 Feb 2026, Rp 87.500, kategori Belanja — benar?"
5. Balas "ya" atau koreksi, lalu masuk database

Total 45 detik per struk, dari yang tadinya 4 menit. Tapi angka kotor itu menyembunyikan cerita error-nya.

## Angka Sebenarnya Setelah 214 Struk

Saya audit database dua minggu lalu, tepat 3 bulan sejak mulai. Hasilnya:

- 214 struk diproses
- 197 terbaca bersih tanpa koreksi — 92%
- 12 butuh koreksi kecil: merchant salah baca, atau total kekurangan digit
- 5 gagal total, terpaksa input manual — 2,3%

Dengan rata-rata 45 detik per struk, total waktu yang saya habiskan sekitar 2,5 jam untuk 214 struk. Kalau manual, dengan estimasi 4 menit per struk, itu 14 jam. Hemat 11,5 jam — dan 0 struk yang terlewat karena malas buka spreadsheet.

## Error yang Paling Sering Muncul

Empat pola error yang berulang.

**Kertas thermal yang memudar.** Struk belanja yang disimpan di dompet tiga minggu hampir mustahil dibaca mesin. Solusinya: foto hari itu juga. Saya pasang kebiasaan foto struk sebelum struknya masuk dompet.

**Angka ketuker.** Total belanja Rp 87.500 kadang terbaca Rp 78.500. Ini paling bahaya karena tidak kelihatan salah. Sekarang saya selalu cek digit total di preview chat, terutama struk dari toko dengan font kecil.

**Merchant generik.** Struk "Toko Sembako" terbaca benar, tapi kategori yang dipilih agent kadang meleset — satu struk alat tulis masuk kategori "Makanan". Kategorisasi butuh konteks, dan OCR hanya melihat teks.

**Struk panjang.** Struk minimarket yang 40 baris sering terpotong di foto. Solusinya: mode scan dengan crop manual, bukan foto biasa.

## Workflow yang Akhirnya Saya Pakai

Setelah trial-error, ini yang bertahan sampai sekarang:

1. **Foto maksimal sehari setelah transaksi** — sebelum thermal paper memudar
2. **Crop ke area teks**, bukan seluruh kertas — ini sendirinya menaikkan akurasi
3. **Cek preview chat 5 detik**, fokus ke total dan tanggal
4. **Struk di atas Rp 500 ribu selalu diverifikasi ulang** — foto ulang kalau ragu
5. **Satu kategori default untuk struk aneh** — daripada agent menebak, struk yang tidak jelas masuk "Lainnya" dan dirapikan mingguan

## Pelajaran yang Paling Berharga

OCR tidak menghilangkan pekerjaan input — dia memindahkannya dari mengetik ke memverifikasi. Dan verifikasi justru bagian yang paling berharga: saya tidak lagi menyalin angka, saya hanya memeriksa angka yang sudah dibaca mesin. Error rate-nya turun karena manusia cuma fokus di satu titik rawan, bukan 15 field.

Dokumentasi Tesseract dan Cloud Vision sama-sama jujur soal limitasi: akurasi sangat tergantung kualitas gambar. Struk Indonesia dengan font kecil dan kertas thermal adalah kasus uji yang adil untuk teknologi ini.

Untuk UKM, ini bukan soal teknologi canggih. Ini soal menyingkirkan pekerjaan yang tidak perlu — dan menerima bahwa 2,3% struk tetap butuh tangan manusia.

## FAQ

**Q: OCR bisa baca semua struk Indonesia?**
A: Tidak. Kertas thermal yang sudah memudar dan struk yang miring hampir selalu gagal. Dari 214 struk saya, 5 gagal total dan 12 butuh koreksi. Faktor terbesar penentu keberhasilan adalah kualitas foto, bukan merek OCR-nya.

**Q: Apakah data struk aman?**
A: Mayoritas struk saya proses dengan Tesseract yang jalan lokal di server sendiri; Cloud Vision hanya saya pakai untuk struk buram. Database tetap di infrastruktur pribadi, tidak lewat aplikasi pihak ketiga.

**Q: Berapa biaya menjalankan ini?**
A: Hampir nol untuk volume pribadi. Tesseract gratis, dan pemakaian Cloud Vision untuk 214 gambar selama 3 bulan masih jauh di bawah batas gratis bulanan. Biaya utamanya waktu setup sekali jalan — sekitar 3 jam di artikel setup sebelumnya.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*
