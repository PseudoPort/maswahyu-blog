---
title: "Hermes Agent Jadi Admin Order: Pesanan dari Chat Masuk Database Tanpa Copy-Paste"
description: "Order klien masuk lewat chat dan sering terlewat. Hermes Agent mencatatnya otomatis: forward pesan ke bot, masuk database, rekap harian."
pubDate: 2026-08-05
heroImage: "../../assets/hero-hermes-agent-order-chat-otomatis.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Hermes Agent Jadi Admin Order: Pesanan dari Chat Masuk Database Tanpa Copy-Paste

Senin malam, 12 Januari 2026. Saya buka WhatsApp setelah seharian rapat, dan di antara notifikasi grup ada satu nama yang membuat saya berhenti: klien dari proyek yang saya tawari dua minggu lalu. Pesannya singkat — "Pak, kami mau lanjut. Mulai minggu ini bisa?" — terkirim Kamis, jam 14.02. Sudah empat hari. Saya membalasnya malam itu juga, dengan permintaan maaf yang seharusnya tidak perlu terjadi.

Masalahnya bukan saya malas. Masalahnya pesanan masuk lewat chat, dan chat itu tenggelam. Sebagai digital agency, hampir semua order Qawwa masuk lewat WhatsApp, Telegram, dan email — tiga kanal yang tidak pernah tenang. Dan saya mencatatnya manual: buka pesan, salin datanya, tempel ke spreadsheet, tandai status. Enam menit per pesanan, kalau saya ingat.

Di bulan Desember 2025, saya menemukan tiga pesanan yang tidak pernah tercatat. Dua kecil. Satu proyek Rp 28 juta yang baru saya respons setelah klien menanyakan ulang. Tidak ada satu pun yang hilang karena kliennya tidak sopan; semuanya hilang karena sistem saya bergantung pada ingatan.

Saya sudah punya [expense tracking otomatis](/blog/setup-hermes-agent-expense-tracking) sejak Oktober, dan pola yang sama berlaku di sini: Hermes Agent yang mengingatkan, saya yang memutuskan. Jadi Januari lalu saya memberinya pekerjaan baru — menjadi admin order.

## Cara Kerjanya: Forward, Catat, Konfirmasi

Tidak ada dashboard baru, tidak ada form CRM. Alurnya begini: setiap kali ada pesanan atau permintaan masuk di WhatsApp atau Telegram, saya forward pesannya ke bot Hermes Agent. Bot mem-parse datanya — nama klien, jenis layanan, nilai, tenggat — lalu menyimpannya sebagai structured memory di PostgreSQL. Satu baris di database, lengkap dengan timestamp.

Yang membuat sistem ini berguna bukan parsing-nya, tapi konfirmasinya. Setiap pesanan tercatat, bot membalas di chat yang sama dengan ringkasan: "Order #ORD-2026-014 — website company profile, klien PT Sawit Nusantara, nilai Rp 28.000.000, tenggat 15 Maret. Sudah masuk daftar." Satu balasan itu mengubah segalanya, karena kalau ringkasannya salah, saya tahu saat itu juga, bukan tiga minggu kemudian.

Kemudian setiap sore jam 17.00, job harian mengirim rekap ke Telegram: daftar order yang masuk hari itu, yang belum ditindaklanjuti, dan yang melewati tenggat. Sore itu saya tinggal menandai mana yang sudah dijawab.

## Angka yang Berubah dalam Sebulan

Saya menghitungnya karena saya perlu tahu apakah ini benar-benar membantu, bukan karena sistemnya bagus. Perbandingan Januari (manual) dan Februari (otomatis):

- Pesanan yang tercatat: 34 di Januari, 41 di Februari. Lima di antaranya kemungkinan besar tidak akan saya catat manual — termasuk satu proyek Rp 45 juta yang masuk jam 22.40 dan baru saya forward ke bot keesokan paginya.
- Pesanan yang terlewat: 3 di Desember, 0 di Februari.
- Waktu pencatatan per pesanan: sekitar 6 menit jadi 20 detik — forward, tunggu balasan bot, selesai.
- Rata-rata waktu respons ke klien: turun dari 9 jam jadi 2 jam, sebagian besar karena tidak ada lagi pesanan yang jatuh dari daftar.

DataReportal Digital 2025 Indonesia mencatat WhatsApp sebagai platform pesan yang paling banyak dipakai di Indonesia. Artinya saya bukan kasus aneh — mayoritas transaksi UKM di sini dimulai dari chat, dan mayoritas pencatatannya masih manual.

## Kesalahan yang Saya Buat di Awal

Dua hal yang saya perbaiki di minggu pertama.

Pertama, bot sempat saya set untuk membalas klien langsung dengan konfirmasi harga. Hari kedua, satu klien lama membalas: "Ini dari sistem ya? Harganya beda sama yang kemarin." Ternyata prompt parsing-nya membaca angka dari pesan lama di thread. Untungnya tidak ada order yang gagal, tapi saya langsung ubah aturannya: bot hanya membalas di chat internal saya, dan yang keluar ke klien tetap pesan dari manusia.

Kedua, parsing yang terlalu percaya diri. Bot pernah mencatat nama klien dengan format alamat email, dan pernah membaca "2,5jt" sebagai 25 juta di satu kesempatan. Perbaikannya bukan model yang lebih pintar — tapi aturan verifikasi: konfirmasi otomatis harus muncul sebelum pesanan dianggap sah. Kalau saya tidak membalas konfirmasi itu dalam 24 jam, pesanan masuk daftar "perlu dicek manual" di rekap sore.

## Kalau Anda Mulai dari Nol

Polanya sederhana, dan Hermes Agent bisa diganti dengan script cron biasa untuk versi paling dasar. Yang penting bukan tools-nya, tapi tiga prinsip ini.

Satu, semua pesanan masuk ke satu tempat. Forward ke satu bot lebih baik daripada mencatat di tiga aplikasi berbeda.

Dua, selalu ada konfirmasi. Sistem yang mencatat tanpa memberi tahu Anda apa yang dicatatnya sama saja dengan spreadsheet yang tidak pernah Anda buka.

Tiga, rekap berkala, bukan real-time. Saya butuh notifikasi per pesanan untuk order penting, tapi rekap harian untuk sisanya. Terlalu banyak alert justru membuat saya mematikan notifikasinya.

Dokumentasi resmi Hermes Agent menjelaskan cara menyusun memory dan scheduled job untuk pola seperti ini. Mulai dari satu kanal saja — misalnya hanya WhatsApp — dan biarkan berjalan dua minggu sebelum menambah kanal lain.

---

Tiga bulan kemudian, tidak ada lagi malam di mana saya membuka chat dan menemukan pesanan yang terlewat. Sistemnya tidak membuat klien membalas lebih cepat, tapi membuat saya tidak pernah lagi kehilangan satu baris pun. Untuk bisnis yang semua transaksinya dimulai dari chat, itu perbedaan yang bisa dihitung dalam rupiah.

Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.

Artikel ini pertama kali dipublikasikan: 5 Agustus 2026.

## Referensi

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk memory, scheduled job, dan konfigurasi
- [Digital 2025: Indonesia — DataReportal](https://datareportal.com/reports/digital-2025-indonesia) — Riset We Are Social tentang penggunaan internet, media sosial, dan aplikasi pesan di Indonesia
