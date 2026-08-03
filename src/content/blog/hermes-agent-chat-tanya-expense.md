---
title: "Chat ke Bot, Tanya Balik Data Expense: 'Berapa Pengeluaran Kopi Saya Bulan Ini?'"
description: "Hermes Agent tidak cuma mencatat expense — dia bisa ditanya balik lewat chat. Contoh query, hasil real, dan pelajaran dari 4 bulan pemakaian."
pubDate: 2026-08-04
heroImage: "../../assets/hero-hermes-agent-chat-tanya-expense.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Chat ke Bot, Tanya Balik Data Expense: "Berapa Pengeluaran Kopi Saya Bulan Ini?"

Jumat malam, akhir Juli 2026, saya baru keluar dari meeting klien di Senopati. Di dalam Grab, pengemudi bertanya mau lewat tol atau tidak, dan saya sadar saya tidak tahu sisa budget transport bulan ini. Tiga puluh detik kemudian saya tahu: chat ke bot di Telegram, ketik "sisa budget transport Juli berapa?", jawabannya muncul sebelum Grab sampai di pintu tol: "Rp 412.000 dari Rp 1.500.000. Transaksi terakhir: tol, Rp 16.000, tadi 18.42 WIB."

Bukan fitur canggih. Ini natural language query ke data yang sudah saya simpan berbulan-bulan. Expense tracking saya jalan sejak April — [datanya masuk otomatis dari struk foto dan notifikasi bank](/blog/setup-hermes-agent-expense-tracking). Tapi selama dua bulan pertama, satu hal masih manual: kalau saya butuh angka tertentu, saya buka dashboard, filter tanggal, filter kategori, lalu menjumlahkan sendiri. Bagian itu yang saya hapus.

## Masalahnya Bukan Mencatat, tapi Menanyakan

Antara April dan Mei, saya membuka laporan expense 3–4 kali seminggu hanya untuk menjawab pertanyaan kecil: berapa pengeluaran F&B minggu ini, kemarin belanja apa saja, kategori mana yang paling besar bulan ini. Saya pernah menghitung waktu satu sesi cek-and-filter: 4–7 menit. Empat kali seminggu, berarti sekitar 20 menit per bulan untuk membaca ulang data yang sebenarnya sudah saya punya.

Bukan jumlah yang besar. Tapi yang mengganggu bukan waktunya — pola pikirnya. Setiap pertanyaan kecil berarti membuka laptop, menunggu dashboard, lalu filter. Untuk pertanyaan yang jawabannya paling lama 30 detik. Saya butuh sesuatu yang bisa ditanya, bukan hanya menampilkan laporan.

## Cara Kerjanya

Hermes Agent berjalan sebagai proses yang bisa diajak chat, dan data expense saya ada di database SQLite sejak setup awal. Chat ke bot artinya memberi prompt yang punya akses baca ke database itu. Bedanya dengan [briefing harian](/blog/hermes-agent-daily-briefing-telegram): briefing itu push — satu arah, terjadwal setiap jam 06.00. Chat ini pull — dua arah, kapan pun saya butuh, tanpa menunggu jadwal.

Contoh pertanyaan yang saya pakai tiap minggu:

- "Total pengeluaran minggu ini, breakdown per kategori"
- "Transaksi paling besar bulan ini"
- "Rata-rata pengeluaran harian Juni dibanding Juli"

Jawabannya teks pendek. Saya minta format tetap: angka dengan satuan Rupiah, tanpa tabel kecuali saya minta. Konsisten seperti briefing — biar mata cepat scanning.

## Step by Step

1. **Pastikan database terstruktur.** Tabel transaksi dengan kolom tanggal, kategori, nominal. Kalau belum punya, mulai dari [setup expense tracking](/blog/setup-hermes-agent-expense-tracking) dulu — chat ini hanya berguna kalau datanya rapi.
2. **Jalankan Hermes Agent dengan akses ke database.** Konfigurasi standar di [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/). Tidak perlu server tambahan, jalan di VM yang sama dengan briefing.
3. **Coba query natural language pertama.** Mulai dari pertanyaan yang jawabannya sudah Anda tahu, misalnya total bulan lalu. Kalau jawabannya sama, berarti akses database-nya benar.
4. **Normalisasi kategori.** Ini pelajaran paling penting, cerita lengkap di bawah.
5. **Batasi akses jadi read-only.** Saya sengaja tidak memberi izin tulis ke bot chat, supaya tidak ada query yang mengubah data. Semua input tetap lewat pipeline foto struk dan notifikasi bank yang sudah ada.

## Pelajaran dari 4 Bulan

**Ambiguitas itu nyata.** Pertanyaan pertama saya — "berapa pengeluaran kopi?" — dijawab dengan tiga interpretasi: kategori F&B, tag "cafe", dan merchant "Kopi Kenangan". Angkanya beda jauh. Solusinya dua: saya menambahkan kolom kategori yang dinormalisasi sejak input, dan bot saya minta menanyakan balik kalau menemukan lebih dari satu tafsir. Sekarang pertanyaan ambigu dibalas "Maksudnya kategori F&B, atau semua transaksi di Kopi Kenangan?" — dan itu lebih baik daripada jawaban salah yang terlihat benar.

**Bahasa campuran itu normal.** "Budget transport" dan "sisa uang gojek" adalah hal yang sama di kepala saya. Bot perlu tahu sinonimnya. Saya menambahkan daftar istilah sederhana — butuh 15 menit, dan sejak itu query seperti itu tidak pernah gagal.

**Read-only itu disiplin, bukan batasan.** Godaan terbesar justru membiarkan bot "membetulkan" kategori yang salah. Saya tahan. Kalau bot bisa menulis, satu prompt yang salah tafsir bisa mengubah data tanpa saya sadari. Semua koreksi tetap lewat input pipeline.

## Angkanya

Sejak Juni, dashboard manual saya turun ke 2–3 kali sebulan — hanya untuk hal yang memang butuh grafik. Pertanyaan rutin pindah ke chat. Perhitungan kasarnya: 20 menit per bulan yang tadinya untuk filter, sekarang nol. Yang lebih penting dari waktu: keputusan jadi lebih cepat.

Juli lalu saya bertanya "kategori mana yang paling besar?" Jawabannya: "Makanan, Rp 4,3 juta, 38% dari total." Dua detik setelah membaca itu saya memutuskan menghentikan langganan meal delivery bulanan yang ternyata menyumbang hampir seperempat dari kategori tersebut. Keputusan itu butuh 2 detik setelah chat, padahal datanya sudah ada sejak lama — saya tidak pernah benar-benar membaca laporan bulanan sampai akhir.

## FAQ

**Q: Apakah chat ke bot bisa menggantikan dashboard?**
A: Tidak sepenuhnya. Untuk melihat tren atau membandingkan bulan, grafik tetap lebih baik. Chat menang untuk pertanyaan spesifik dan cepat: berapa, kapan, kategori apa. Saya pakai keduanya — chat untuk tanya, dashboard untuk eksplorasi.

**Q: Apakah perlu bisa coding untuk ini?**
A: Tidak perlu menulis model atau AI. Yang diperlukan memahami struktur database dan menulis prompt. Kalau sudah punya database expense yang rapi, bagian paling teknisnya adalah memberi tahu bot kolom apa saja yang ada.

**Q: Apakah data expense saya aman kalau bot bisa diakses dari Telegram?**
A: Bot saya read-only dan hanya bisa diakses dari chat pribadi dengan autentikasi. Tidak ada data yang dikirim ke pihak ketiga selain API Telegram untuk pengiriman pesan, dan database tetap di VM sendiri. Detail arsitekturnya ada di dokumentasi resmi [Telegram Bot API](https://core.telegram.org/bots/api).

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 4 Agustus 2026.*

## Referensi

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk konfigurasi, chat, dan akses tools/database
- [Telegram Bot API](https://core.telegram.org/bots/api) — Dokumentasi resmi Telegram Bot untuk pengiriman pesan dan autentikasi
- [SQLite Documentation](https://www.sqlite.org/docs.html) — Dokumentasi resmi SQLite untuk struktur database yang dipakai menyimpan transaksi
