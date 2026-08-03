---
title: "Hermes Agent Jadi Penagih Piutang yang Sopan: Tracking Invoice dan Reminder Otomatis"
description: "Cara saya otomasi tracking piutang dan reminder pembayaran invoice klien dengan Hermes Agent. DSO turun dari 47 ke 21 hari dalam 3 bulan."
pubDate: 2026-08-03
heroImage: "../../assets/hero-hermes-agent-piutang-reminder-otomatis.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Hermes Agent Jadi Penagih Piutang yang Sopan: Tracking Invoice dan Reminder Otomatis

Januari 2026, jam 21.00. Saya buka spreadsheet piutang yang sudah dua minggu tidak saya sentuh. Di sana ada satu baris yang membuat saya berhenti: invoice dari klien bulan November, jatuh tempo 14 Desember, nilai Rp 86 juta. Sudah lewat 48 hari, belum dibayar.

Masalahnya bukan kliennya nakal. Masalahnya saya. Invoice itu saya kirim manual, follow-up pertama saya lakukan 10 hari setelah jatuh tempo, dan itu pun lewat chat yang basa-basinya bertele-tele. Klien punya 40-an vendor lain yang juga menagih. Saya hanya salah satu yang paling tidak konsisten.

Saat itu total piutang saya Rp 143 juta tersebar di 9 invoice. Rata-rata keterlambatan pembayaran 34 hari. Angka itu saya tahu persis karena saya sempat mencatatnya di spreadsheet — sekali, di akhir tahun. Bukan karena sistem saya bagus, tapi karena saya butuh angka untuk evaluasi diri.

Setelah [expense tracking otomatis](/blog/setup-hermes-agent-expense-tracking) jalan mulus sejak Oktober, saya memutuskan menangani sisi uang masuk dengan cara yang sama: biarkan Hermes Agent yang mengingatkan, saya yang memutuskan.

## Kenapa Manual Follow-up Gagal

Saya bukan tipe orang yang suka menagih. Follow-up piutang itu pekerjaan yang paling saya tunda, dan penundaan itu mahal: setiap invoice yang telat 30 hari berarti kas saya terkunci di piutang orang lain.

Dari pengalaman 16 tahun di industri, pola keterlambatan hampir selalu sama. Tidak ada satu pun klien yang membayar lebih cepat karena kita menagih lebih sering. Yang terjadi justru sebaliknya: invoice yang tidak pernah ditagih ulang adalah yang paling lama mengendap. Atradius mencatat dalam Payment Practices Barometer Asia Pacific bahwa rata-rata B2B invoice di Asia Pasifik dibayar telat sekitar 18 hari, dan penagihan yang tidak terstruktur adalah salah satu penyebab utamanya.

Saya tidak butuh lebih sering menagih. Saya butuh menagih di waktu yang tepat, dengan nada yang konsisten, tanpa harus mengingat-reminding sendiri kapan invoice mana yang harus di-follow-up.

## Setup: Tiga Lapis yang Saya Bangun

Hermes Agent sudah terpasang di laptop saya dengan PostgreSQL sebagai memory backend — persis seperti yang saya tulis di artikel setup expense tracking. Untuk piutang, saya tidak membuat sistem terpisah. Saya menambah tiga komponen: register invoice, aturan reminder bertingkat, dan kanal notifikasi Telegram.

**Pertama, register invoice.** Setiap kali saya kirim invoice baru, saya kirim satu pesan ke bot Telegram: nama klien, nomor invoice, nilai, tanggal jatuh tempo. Hermes menyimpannya sebagai structured memory. Butuh waktu 30 detik per invoice, termasuk ngetik. Tidak ada form, tidak ada spreadsheet baru.

**Kedua, aturan reminder bertingkat.** Ini bagian yang paling mengubah perilaku saya. Hermes menjalankan job harian yang memeriksa semua invoice, lalu mengirimkan pesan sesuai umur keterlambatan:

- H-3 sebelum jatuh tempo: pesan ke saya saja, untuk konfirmasi invoice sudah terkirim dan tidak ada masalah.
- H+7 setelah jatuh tempo: pesan ke saya berisi draf follow-up yang bisa saya kirim ke klien — sopan, satu paragraf, menyebut nomor invoice dan nilai tanpa nada menekan.
- H+21: draf follow-up kedua dengan nada lebih tegas, plus saran telepon.
- H+45: alert ke saya: invoice ini masuk daftar yang perlu saya tangani langsung, bukan lewat bot.

Saya yang tetap menekan tombol kirim. Bot tidak pernah chat klien sendiri. Yang berubah: saya tidak lagi menunda karena lupa.

**Ketiga, kanal notifikasi.** Semua reminder masuk ke Telegram yang sama dengan briefing harian saya. Jadi setiap pagi, bersamaan dengan ringkasan jadwal, saya dapat satu baris: *"Invoice #INV-2025-011 (Rp 86 juta) sudah 48 hari lewat jatuh tempo. Draf follow-up menunggu di chat."*

## Angka yang Berubah Setelah Tiga Bulan

Data pertama yang keluar dari sistem ini adalah kejutan untuk saya. Ternyata dua invoice yang paling lama mengendap — termasuk yang Rp 86 juta — bukan karena klien tidak mau bayar. Keduanya macet di internal klien: satu karena orang yang approve sudah pindah divisi, satu karena invoice masuk ke email lama yang jarang dibuka. Dua-duanya terbayar penuh dalam 2 minggu setelah follow-up terstruktur sampai ke orang yang tepat.

Di bulan ketiga, Maret 2026, saya bandingkan angkanya:

- Rata-rata keterlambatan pembayaran turun dari 34 hari menjadi 21 hari.
- Invoice yang lewat 30 hari: dari 3 invoice menjadi 0.
- Waktu yang saya habiskan untuk urusan piutang: dari sekitar 4 jam per bulan (mengecek spreadsheet, mencari riwayat chat, menulis pesan) menjadi sekitar 45 menit — hampir semuanya untuk membalas percakapan yang sudah dimulai bot.

Bukan angka yang dramatis, tapi dampaknya ke arus kas langsung terasa. Rp 143 juta piutang di bulan Januari turun menjadi Rp 52 juta di akhir Maret, dan tidak ada satu invoice pun yang berumur lebih dari 30 hari.

## Kesalahan yang Saya Buat di Awal

Ada dua hal yang saya kerjakan ulang.

Pertama, saya sempat membuat reminder otomatis langsung ke klien, bukan draf ke saya. Hari kedua, satu klien lama membalas singkat: *"Wah, udah otomatis ya tagihannya."* Bukan masalah besar, tapi nada relasinya berubah. Saya langsung ubah aturannya: bot cukup menyiapkan draf, keputusan kirim tetap di tangan saya. Klien tidak perlu tahu seberapa rapi sistem penagihan saya.

Kedua, saya awalnya hanya mencatat tanggal kirim invoice, bukan tanggal jatuh tempo. Akibatnya beberapa reminder muncul dengan hitungan yang salah di minggu pertama. Perbaikannya sederhana: satu field tambahan di register invoice, dan aturan baru bahwa invoice tanpa tanggal jatuh tempo dianggap belum tercatat.

## Kalau Anda Mulai dari Nol

Alur kerjanya sederhana, dan Hermes Agent bisa diganti apa saja — script cron biasa pun cukup untuk versi paling dasar. Yang penting adalah polanya: satu tempat mencatat semua piutang, aturan reminder yang jelas bertingkat, dan satu kanal yang Anda lihat setiap hari. Dokumentasi resmi Hermes Agent menjelaskan cara menyusun scheduled job dan memory dengan lengkap.

Mulai dari tiga aturan reminder saja. Jangan langsung bikin sistem yang mengirim invoice, menagih otomatis, dan menandai risiko kredit dalam satu malam — saya coba, dan hasilnya justru berantakan karena saya belum percaya pada output-nya. Sistem kecil yang Anda pakai setiap hari lebih berharga daripada sistem besar yang Anda cek sebulan sekali.

---

Tiga bulan kemudian, spreadsheet piutang itu sudah tidak saya buka lagi. Bukan karena piutangnya hilang — karena semua angkanya sudah datang sendiri setiap pagi. Piutang tidak mengecil karena sistem lebih pintar, tapi karena tidak ada lagi invoice yang jatuh dari ingatan.

Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.

Artikel ini pertama kali dipublikasikan: 3 Agustus 2026.

## Referensi

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk scheduled job, memory, dan konfigurasi
- [Atradius Payment Practices Barometer Asia Pacific](https://atradius.us/reports/payment-practices-barometer-asia-pacific-2024.html) — Riset keterlambatan pembayaran B2B di Asia Pasifik
- [Telegram Bot API](https://core.telegram.org/bots/api) — Dokumentasi resmi Telegram Bot untuk notifikasi dan pesan
