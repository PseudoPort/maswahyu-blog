---
title: "Morning Briefing Otomatis: Hermes Agent Kirim Ringkasan Harian ke Telegram Sebelum Saya Bangun"
description: "Hermes Agent kirim briefing harian ke Telegram tiap 06.00 WIB: ringkasan expense, task prioritas, jadwal meeting. 45 menit setup, 112 hari jalan."
pubDate: 2026-08-01
heroImage: "../../assets/hero-hermes-agent-daily-briefing-telegram.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Morning Briefing Otomatis: Hermes Agent Kirim Ringkasan Harian ke Telegram Sebelum Saya Bangun

Mei 2026, jam 06.05. Saya masih di kasur, buka Telegram, dan di sana sudah ada satu pesan baru dari bot saya sendiri. Terkirim 06.00 tepat. Isinya: 14 transaksi kemarin sudah dikategorikan ke 6 kategori, 2 tagihan jatuh tempo hari ini, 3 meeting, dan 1 pengingat bayar PPN. Semua dalam satu pesan, 2.400 karakter, sekitar 1 menit baca.

Bukan demo. Briefing ini jalan 112 hari berturut-turut sampai artikel ini saya tulis. Gagal 3 hari — dua karena server saya down, satu karena API key expired saat rotate.

Sebelumnya, pagi saya seperti ini: buka Excel expense, buka Gmail cek email penting, buka kalender lihat jadwal, buka WhatsApp cek grup kerja. Empat aplikasi, 25–30 menit, dan itu terjadi sebelum saya sempat ngopi pertama. Kalau dihitung: 25 menit × 22 hari kerja = 9 jam sebulan. Bukan untuk keputusan besar — cuma untuk membaca ulang data yang sebenarnya sudah saya simpan.

Riset Gloria Mark dari University of California, Irvine menemukan rata-rata orang butuh 23 menit untuk balik fokus setelah satu interupsi. Masalah saya bukan interupsi. Masalah saya memulai hari dengan 6 tugas kecil yang seharusnya tidak perlu dilakukan manual sama sekali.

## Yang Bikin Saya Akhirnya Setup Briefing

Setelah expense tracking dan meeting notes jalan, sisa bottleneck di pagi hari justru di sini: mengumpulkan informasi. Datanya ada — di database expense, di catatan meeting, di kalender — tapi tersebar di 4 tempat.

Target saya sederhana: satu pesan, jam 06.00 WIB, berisi 4 hal:

1. Ringkasan expense kemarin + status budget bulanan
2. 3 task prioritas (disaring dari meeting notes)
3. Jadwal meeting hari ini
4. Pengingat tagihan yang jatuh tempo 3 hari ke depan

Versi pertama selesai dalam 45 menit, plus 2 jam tuning di minggu pertama. Ini breakdown-nya.

## Step 1: Bikin Bot Telegram (5 Menit)

Via [@BotFather](https://t.me/BotFather) — gratis, dan bot-nya dapat token. Saya simpan token di environment variable, bukan di repo. Pelajaran dari hari ke-47: token pernah ke-commit ke repo lokal, langsung saya rotate. Sekarang aturannya satu: apapun yang menyentuh API credential tidak pernah masuk git.

## Step 2: Tulis Fungsi Briefing (30 Menit)

Inti fungsinya cuma: query database expense untuk transaksi kemarin, ambil task yang masih open dari file meeting notes, cek jadwal, lalu gabung jadi satu teks. Tidak ada yang cerdas-cerdas — yang penting teksnya pendek dan padat. Saya pakai template dengan format yang sama setiap hari supaya mata cepat scanning. Format yang konsisten itu justru yang bikin pesan ini enak dibaca: judul, 4 blok, tanpa basa-basi.

## Step 3: Jadwalkan via Cron Hermes Agent (10 Menit)

Bagian paling gampang dan paling sering salah: timezone. Versi pertama saya pakai UTC, briefing datang jam 13.00 WIB. Masih berguna — tapi bukan briefing pagi. Satu baris config diganti ke Asia/Jakarta, selesai.

Hermes Agent punya fitur scheduled job/cron bawaan, dokumentasinya di [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/). Saya pakai itu, bukan cron Linux manual, karena job-nya bisa akses memory dan tools yang sama dengan sesi interaktif. Artinya briefing bisa ambil konteks dari sesi kerja kemarin tanpa setup tambahan.

## Step 4: Urus Gagal (Pelajaran dari 3 Hari)

- **Rate limit Telegram**: kalau bot kirim lebih dari 20 pesan per menit ke chat yang sama, API balas error 429. Satu briefing = satu pesan, jadi jarang kena — tapi waktu tuning awal saya kena 2 kali karena testing dalam loop.
- **Server down**: 2 hari gagal karena VM saya mati. Solusinya bukan bikin sistem lebih pintar, tapi menerima saja: 2 dari 112 hari itu 1,7% failure rate, dan briefing tidak pernah jadi critical path.
- **API key expired**: 1 hari. Sekarang ada notifikasi di log kalau job gagal, jadi saya tahu sebelum jam 08.00.

Detail API Telegram ada di dokumentasi resminya: [Telegram Bot API](https://core.telegram.org/bots/api).

## Hasilnya Setelah 112 Hari

- Waktu hemat: 25 menit × 112 hari ≈ 46 jam — hampir 2 hari kerja penuh. Itu waktu yang tadinya dipakai untuk membaca ulang data.
- Keputusan pagi berkurang. Saya tidak lagi memutuskan "cek apa dulu" — itu sudah diputuskan oleh bot.
- Yang paling tidak terduga: briefing ini jadi pintu masuk data. Karena expense dirangkum tiap pagi, anomali ketahuan cepat. Juni lalu ada transaksi 3 kali lipat di kategori transport — saya sadar di hari yang sama, ternyata langganan Gojek corporate yang harusnya sudah dicabut.

ROI-nya: 45 menit setup + 2 jam tuning, balik modal di minggu pertama.

## Kalau Mau Mulai dari Sini

Jangan mulai dari automation besar. Mulai dari satu pesan yang benar-benar akan Anda baca tiap pagi. Bot yang mengirim 1 pesan berguna setiap hari lebih berharga daripada dashboard yang tidak pernah dibuka.

Urutan yang saya jalani: [expense tracking dulu](/blog/setup-hermes-agent-expense-tracking), lalu [meeting notes](/blog/hermes-agent-meeting-notes-action-items), baru briefing harian. Masing-masing berdiri sendiri dan saling menguatkan.

Kalau mulai dari nol, mulai dari yang ini: bikin bot kirim ringkasan satu hal yang paling sering Anda cek di pagi hari. Seminggu kemudian, tambah satu lagi.

## FAQ

**Q: Apakah Hermes Agent bisa kirim pesan Telegram otomatis?**
A: Bisa. Hermes Agent punya integrasi Telegram dan fitur scheduled job/cron bawaan, jadi bisa kirim pesan terjadwal tanpa server tambahan.

**Q: Berapa lama setup briefing harian otomatis?**
A: Versi pertama saya 45 menit, plus 2 jam tuning di minggu pertama. Kalau sudah punya database expense atau catatan meeting yang terstruktur, biasanya lebih cepat.

**Q: Apakah perlu server khusus untuk ini?**
A: Tidak. Briefing saya jalan di VM yang sudah dipakai untuk hal lain. Kalaupun mati, dampaknya kecil — saya tinggal baca datanya manual hari itu.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 1 Agustus 2026.*

## Referensi

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk scheduled job/cron dan konfigurasi
- [Telegram Bot API](https://core.telegram.org/bots/api) — Dokumentasi resmi Telegram Bot untuk token, sendMessage, dan rate limit
- [BotFather](https://t.me/BotFather) — Tool resmi Telegram untuk membuat dan mengelola bot
