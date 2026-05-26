---
title: "AI buat Screening CV: Cara UKM Indonesia Saring Pelamar Tanpa Buang Waktu Seharian"
description: "Panduan praktis pakai AI untuk screening CV pelamar di UKM — dari ekstrak data, scoring otomatis, sampai shortlist final yang siap dipanggil interview."
pubDate: "2026-05-27"
heroImage: "../../assets/hero-ai-screening-cv-rekrutmen-ukm-indonesia.jpg"
---

Saya pernah ngobrol sama owner toko bahan bangunan di Bekasi yang baru aja buka cabang kedua. Dia butuh 3 admin gudang. Iklan kerja dipasang di JobStreet sama satu grup Telegram lokal. Dalam 4 hari masuk 187 CV. Dia coba baca satu-satu sambil ngurus operasional, baru sampai CV ke-30 udah pusing duluan. Akhirnya dia rekrut yang pertama nelpon balik. 2 bulan kemudian, 1 keluar, 1 dipecat karena nyolong barang.

Cerita kayak gini umum banget di UKM. Owner jadi HR dadakan, padahal nggak punya waktu, nggak punya sistem, dan nggak punya filter yang konsisten. Yang kepilih sering bukan yang paling cocok, tapi yang paling cepat bales WhatsApp.

AI bisa motong proses screening dari satu hari penuh jadi sekitar 30 menit. Bukan buat ngambil keputusan akhir — itu tetap kerjaan kamu — tapi buat naikin yang pantas masuk shortlist ke atas, dan turunin yang nggak relevan.

## Kenapa screening CV manual itu bocor di UKM

Tiga masalah utama yang saya lihat di lapangan:

Pertama, tidak ada kriteria tertulis. Owner tahu di kepalanya kandidat ideal kayak apa, tapi pas baca CV ke-50, kriteria itu udah blur. Yang dipanggil interview sering bukan yang paling kuat, tapi yang dibaca pas owner masih segar.

Kedua, format CV berantakan. Sebagian pelamar UKM Indonesia kirim PDF, sebagian foto KTP plus narasi WhatsApp, sebagian lagi cuma chat "saya tertarik bu". Membandingkan apel dengan jeruk dengan kelapa.

Ketiga, bias yang nggak disadari. Nama yang familiar, alamat yang dekat, foto yang rapi — semua ngaruh tanpa kita sadari. Buat posisi teknis sederhana, bias ini bisa bikin kita nolak orang yang sebenarnya paling cocok.

AI tidak menghapus tiga masalah ini sepenuhnya, tapi memaksa kita bikin kriteria eksplisit dan menerapkannya konsisten ke semua kandidat. Itu udah lompatan besar.

## Workflow screening AI yang dipakai UKM saya bantu

Saya pakai pendekatan tiga lapis. Sederhana, tapi cukup untuk volume 50–500 CV per posisi.

### Lapis 1: Kumpulkan dan normalkan

Semua CV yang masuk — entah PDF, JPG, atau chat — dilempar ke satu folder. Buat UKM yang baru mulai, folder Google Drive sudah cukup. Yang sudah punya tools, bisa pakai Notion atau Airtable.

Pakai AI buat ekstrak ke format seragam. Prompt-nya kira-kira:

> "Dari dokumen ini, ekstrak: nama, umur, kota domisili, pendidikan terakhir, pengalaman kerja terakhir (posisi + lama), keahlian relevan, gaji yang diharapkan kalau ada. Output dalam format JSON. Kalau ada info yang tidak ada di dokumen, isi 'tidak ada'."

Sekarang kamu punya tabel rapi, bukan tumpukan PDF.

### Lapis 2: Scoring otomatis berdasarkan kriteria

Bikin daftar kriteria yang bener-bener penting. Bukan wishlist, tapi must-have.

Contoh untuk admin gudang:
- Domisili maksimal 10 km dari toko
- Pengalaman minimal 1 tahun di logistik atau retail
- Bisa pakai Excel dasar
- Umur 22–40

Lempar tabel hasil lapis 1 plus kriteria ini ke AI. Minta scoring 0–10 per kandidat dengan alasan singkat. Yang penting: minta AI **menjelaskan** kenapa skornya segitu. Jangan terima skor tanpa alasan, karena di situlah bias atau salah baca ketauan.

### Lapis 3: Shortlist manual dari top 20 persen

Lapis 2 ngasih kamu peringkat. Jangan langsung percaya. Buka manual top 20 persen — biasanya 10–30 CV — dan baca seperti biasa. Di sini intuisi dan pengalaman kamu sebagai owner main. AI nggak ngerti bahwa Pak Budi yang nulis CV jelek itu sepupu pelanggan setia kamu.

Dari shortlist ini, baru kamu pilih siapa yang dipanggil interview.

## Pitfall yang sering bikin UKM salah pakai AI buat rekrutmen

Beberapa kesalahan yang udah saya lihat berulang:

**Menyerahkan keputusan akhir ke AI.** Jangan. AI bagus buat menyaring, jelek buat memutuskan siapa yang masuk tim kamu selama bertahun-tahun. Keputusan akhir tetap manusia.

**Kriteria terlalu kaku.** Kalau kamu set "pendidikan minimal S1" ke AI, semua SMA otomatis ke-skip. Padahal buat banyak posisi UKM, pengalaman lapangan jauh lebih relevan. Kriteria yang baku biasanya: lokasi, pengalaman, dan kemampuan teknis spesifik. Pendidikan formal sering bukan pembeda.

**Lupa simpan jejak data.** CV pelamar berisi data pribadi: KTP, alamat, nomor HP. Setelah proses selesai, hapus data yang tidak terpilih dalam 30–60 hari. Kalau kamu pakai AI cloud, jangan unggah scan KTP atau dokumen sensitif lain — ekstrak dulu informasi yang dibutuhkan, baru lempar ke AI.

**Pakai AI buat nilai kepribadian.** Skip aja. Model bahasa nggak bisa nilai integritas dari CV. Itu kerjaan interview dan trial period.

## Tools yang realistis untuk UKM Indonesia

Saya jarang nyaranin satu tools spesifik karena UKM kondisinya beda-beda. Tapi pola umumnya:

Untuk volume kecil (di bawah 30 CV per bulan), ChatGPT atau Claude versi web udah cukup. Copy-paste CV ke chat, kasih kriteria, minta scoring.

Untuk volume menengah dan butuh konsistensi, agentic workflow kayak Hermes Agent atau OpenClaw bisa otomatis baca folder, ekstrak, dan output ke spreadsheet. Setup awalnya 1–2 sore. Setelah itu jalan sendiri.

Untuk yang udah punya HRIS, biasanya vendor-nya udah nyediain modul AI screening. Tinggal aktifin dan kalibrasi kriteria.

Yang paling penting bukan tools, tapi disiplin nulis kriteria dulu sebelum nyebar lowongan. Kalau kriterianya nggak jelas, AI sebagus apapun cuma akan bikin kebingungan kamu lebih cepat.

## ROI yang masuk akal

Owner yang saya ceritain di awal akhirnya pakai workflow tiga lapis ini buat rekrutmen berikutnya. Hasilnya bukan ajaib, tapi nyata: dari 142 CV, dia panggil interview 12 orang, hire 3, dan dua tahun kemudian semuanya masih kerja di sana.

Hemat waktunya jelas. Tapi yang lebih berharga adalah dia tidur lebih nyenyak waktu rekrutmen. Bukan karena AI ngambil keputusan, tapi karena dia tahu dia nggak skip kandidat bagus cuma karena CV-nya nomor 187.

Kalau kamu lagi mau buka rekrutmen bulan ini, coba mulai dari yang paling kecil: tulis 5 kriteria must-have, lempar 10 CV pertama ke AI, dan lihat apakah hasil scoring-nya masuk akal. Dari situ kamu kalibrasi.

Rekrutmen yang baik bukan soal teknologi. Tapi teknologi yang baik bisa bikin kamu fokus ke bagian yang memang butuh penilaian manusia.
