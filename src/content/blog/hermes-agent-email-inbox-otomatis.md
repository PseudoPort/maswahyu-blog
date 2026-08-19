---
title: "Workflow Email dengan Hermes Agent: 214 Email per Minggu, Saya Cuma Membaca 20"
description: "Hermes Agent sortir inbox tiap pagi via IMAP: 214 email per minggu jadi 20 yang perlu dibalas. Waktu email turun dari 5,5 jam jadi 1 jam per minggu."
pubDate: 2026-08-20
heroImage: "../../assets/hero-hermes-agent-email-inbox-otomatis.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Workflow Email dengan Hermes Agent: 214 Email per Minggu, Saya Cuma Membaca 20

Senin, 4 Mei 2026, jam 07.20. Gmail saya terbuka setelah akhir pekan, dan di sana menunggu 47 email belum dibaca. Bukan angka yang luar biasa — minggu sebelumnya 52. Yang membuat saya berhenti scroll adalah cara saya menghabiskan dua jam berikutnya: buka satu per satu, label, arsip, baca setengah, buka lagi. Dua jam kemudian, hanya dua email yang benar-benar butuh balasan. Keduanya nyaris tenggelam di antara newsletter.

Minggu itu saya menghitung dengan jujur: 214 email masuk, 19 yang saya balas. Sekitar 91% isi inbox tidak perlu sampai ke mata saya. Angkanya bukan hal baru — Radicati Email Statistics Report mencatat rata-rata pekerja bisnis mengirim dan menerima 126 email per hari. Yang baru adalah kesadaran bahwa biaya terbesar bukan di emailnya, tapi di keputusan kecil yang saya buat 214 kali seminggu: penting atau tidak? baca sekarang atau nanti? balas atau arsip?

## Pemicunya: Satu Invoice yang Hampir Telat

April 2026, invoice vendor langganan server hampir lewat jatuh tempo. Emailnya masuk jam 21.47 malam, dan 11 email promo masuk setelahnya — begitu pagi, invoice itu sudah tenggelam di posisi ke-15. Saya baru menyadarinya tiga hari kemudian, setelah tanggal jatuh tempo lewat. Vendor tidak marah, tapi pengalaman itu cukup: sistem yang mengandalkan mata manusia untuk menyortir inbox tidak akan bertahan begitu volume naik.

Target saya waktu itu sederhana. Satu job, tiap pagi, tiga hasil: email mana yang butuh balasan hari ini, email mana yang hanya perlu dibaca, dan sisanya — arsip tanpa saya lihat.

## Cara Kerjanya

**Langkah 1 — Akses baca lewat IMAP.** Saya buat app password khusus untuk Gmail dengan scope IMAP, bisa dicabut kapan saja tanpa mengganggu login utama. Untuk membaca, saya pakai [Himalaya](https://github.com/pimalaya/himalaya), CLI IMAP/SMTP open source — satu perintah untuk list email baru sejak kemarin. Kuncinya: agent membaca email dari server, tidak pernah memindahkan atau menghapus apa pun. Data tetap di Gmail.

**Langkah 2 — Job pagi jam 06.30.** Hermes Agent punya scheduled job bawaan, dokumentasinya di [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/). Setiap pagi job ini mengambil email baru, lalu mengklasifikasikannya ke tiga label: urgent (invoice, klien, payment), perlu dibaca (laporan, newsletter yang memang saya langganan), dan sisanya masuk arsip. Klasifikasinya bukan AI ajaib — aturan berbasis pengirim dan kata kunci di subjek, ditambah contoh email yang saya tandai manual di minggu pertama.

**Langkah 3 — Ringkasan ke Telegram.** Hasilnya dikirim ke Telegram pribadi jam 06.30: daftar email urgent, satu baris per email, plus draft balasan pendek untuk yang paling mendesak. Pagi saya berubah dari "buka Gmail dan tenggelam" menjadi "baca 6 baris, approve 2 draft, selesai".

**Langkah 4 — Aturan pengiriman.** Draft balasan tidak pernah terkirim sendiri. Saya yang klik approve. Ini batas yang saya pegang sejak hari pertama, dan sampai sekarang tidak saya ubah.

## Angka Setelah 74 Hari

Workflow ini jalan 74 hari saat artikel ini ditulis. Catatan yang saya simpan:

- 214 email per minggu masuk, rata-rata 18 yang benar-benar saya balas. Sisanya diarsipkan atau dibaca sekilas.
- Waktu email: dari 5 jam 45 menit per minggu menjadi sekitar 1 jam 15 menit, sesuai catatan waktu kerja.
- Satu email penting yang terselamatkan: minggu ketiga, invoice klien dengan tanggal jatuh tempo 7 hari. Agent menaikkan prioritasnya karena kata "invoice" dan angka jatuh tempo muncul di subjek. Saya approve balasan konfirmasi di hari yang sama — sebelumnya email seperti ini bisa lewat 2–3 hari.
- Gagal 2 hari: satu karena VM mati, satu karena app password kedaluwarsa saat saya rotate. Tidak ada email yang hilang — paling parah email menumpuk dan saya baca manual hari itu.

Setup-nya sekitar 2 jam di minggu pertama, termasuk tuning aturan klasifikasi. Balik modal di minggu pertama.

## Batas yang Saya Pasang

Tiga aturan yang tidak saya langgar:

1. **Agent tidak pernah mengirim email sendiri.** Balasan yang salah terkirim lebih mahal daripada balasan yang telat satu hari.
2. **Email tidak pernah pindah dari Gmail.** Agent baca via IMAP, dan mark-as-read hanya untuk email yang sudah masuk ringkasan. Kalau suatu saat agent saya matikan, inbox kembali seperti semula.
3. **App password khusus, bukan password utama.** Kalau bocor, saya cabut satu credential, bukan mengganti seluruh akun.

## Kalau Mau Mulai

Jangan bangun semuanya sekaligus. Mulai dari satu label saja: misalnya "email yang mengandung kata invoice" — ringkas ke Telegram tiap pagi, tanpa draft balasan dulu. Seminggu pertama cukup untuk melihat apakah Anda benar-benar membuka ringkasannya. Kalau ya, tambah label berikutnya; kalau tidak, perbaiki format ringkasannya dulu.

Workflow ini berdiri di atas hal yang sama dengan [expense tracking saya](/blog/setup-hermes-agent-expense-tracking) dan [briefing harian](/blog/hermes-agent-daily-briefing-telegram): bukan soal membuat sistem lebih pintar, tapi menghilangkan keputusan kecil yang berulang supaya fokus tersisa untuk yang benar-benar penting.

## FAQ

**Q: Apakah Hermes Agent bisa membaca email dan membalas otomatis?**
A: Bisa membaca via IMAP dan menyusun draft balasan. Pengiriman tetap manual — agent menyiapkan, manusia yang approve. Ini sengaja, supaya tidak ada email yang salah terkirim.

**Q: Apakah aman memberikan akses email ke agent?**
A: Aman kalau memakai app password khusus dengan scope IMAP read dan tidak menyimpan credential di repo. Agent saya tidak pernah memindahkan atau menghapus email; data tetap di Gmail.

**Q: Berapa lama setup-nya?**
A: Versi pertama saya sekitar 2 jam, termasuk tuning aturan klasifikasi di minggu pertama. Kalau hanya satu label dan satu ringkasan Telegram, bisa kurang dari satu jam.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 20 Agustus 2026.*

## Referensi

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk scheduled job dan konfigurasi
- [Himalaya CLI](https://github.com/pimalaya/himalaya) — CLI IMAP/SMTP open source untuk membaca email dari terminal
- [Radicati Email Statistics Report](https://www.radicati.com/wp/wp-content/uploads/2018/01/Email-Statistics-Report-2018-2022-Executive-Summary.pdf) — Riset industri soal volume email bisnis harian
- [Gmail IMAP settings](https://support.google.com/mail/answer/7126229) — Dokumentasi resmi Google untuk IMAP dan app password
