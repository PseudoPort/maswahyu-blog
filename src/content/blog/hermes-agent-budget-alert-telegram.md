---
title: "Budget Alert: Hermes Agent Kirim Notifikasi Saat Pengeluaran Lewat Ambang Batas"
description: "Hermes Agent saya pasang alarm budget: kategori dicek tiap malam, Telegram kasih tahu sebelum bulan habis. Setup, aturan ambang, dan hasil 3 minggu."
pubDate: 2026-08-07
heroImage: "../../assets/hero-hermes-agent-budget-alert-telegram.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Budget Alert: Hermes Agent Kirim Notifikasi Saat Pengeluaran Lewat Ambang Batas

Minggu kedua Agustus 2026, pukul 21.47 WIB. Notifikasi Telegram masuk dari bot. Bukan promo, bukan grup, cuma satu baris: "Kategori F&B sudah Rp 2.050.000 dari budget Rp 2.500.000 (82%). Rata-rata harian Rp 97.619. Proyeksi akhir bulan Rp 2.950.000 — lewat Rp 450.000."

Saya berhenti baca dua kali. Angkanya betul. Budget F&B saya Rp 2,5 juta per bulan sejak Mei, dan seperti biasa, bulan Agustus sudah nyaris jebol di hari ke-21. Bedanya kali ini: saya tahu di hari ke-21, bukan pas tanggal 31 sambil lihat rekening.

## Budget Selama Ini Cuma Niat

Antara Januari dan April, saya menulis budget di awal bulan — F&B Rp 2,5 juta, transport Rp 1,5 juta, sisanya fleksibel. Lalu dilupakan. Mekanismenya: tidak ada. Satu-satunya alarm adalah momen kaget pas laporan bulanan keluar, dan momen itu selalu telat.

Buktinya ada di [review tengah tahun saya](/blog/mid-year-financial-review-hermes-agent): 6 dari 10 kategori konsisten melewati budget, dan saya baru sadar pas Juni. Bukan karena angkanya disembunyikan — [data expense sudah tercatat otomatis sejak April](/blog/setup-hermes-agent-expense-tracking). Masalahnya tidak ada yang membandingkan angka itu dengan budget setiap hari. Angka yang tidak dibandingkan sama saja dengan tidak ada.

Perilaku ini bukan cuma saya yang mengalaminya. Riset Karlan dkk. di Management Science (2016) menemukan pengingat sederhana — pesan teks berkala — meningkatkan tabungan secara signifikan, justru karena pengingat membuat tujuan finansial tetap "top of mind". Reminder itu bekerja bukan karena informasinya baru, tapi karena konsisten datang di waktu yang tepat. Prinsip yang sama yang saya pakai: bukan laporan baru, tapi perbandingan otomatis yang datang tiap malam.

## Yang Saya Pasang: Cek Harian + Ambang Batas

Sistemnya tiga bagian, semuanya jalan di VM yang sama dengan [briefing pagi](/blog/hermes-agent-daily-briefing-telegram) dan [bot chat expense](/blog/hermes-agent-chat-tanya-expense):

1. **File budget** — satu file YAML berisi target per kategori per bulan. Mei 2026: F&B 2.500.000, transport 1.500.000, subscription 1.200.000, lainnya 1.800.000.
2. **Job harian pukul 21.30** — Hermes Agent menjalankan query agregasi: total per kategori untuk bulan berjalan, diambil dari database SQLite yang sama dengan pencatatan expense.
3. **Aturan kirim** — tiga ambang: di bawah 70% diam, 70–99% kirim info, 100% ke atas kirim peringatan dengan proyeksi akhir bulan.

Yang saya pilih di tahap awal hanya dua kategori: F&B dan transport. Dua kategori yang paling sering bocor. Subscription saya biarkan dulu — [audit langganan butuh pendekatan berbeda](/blog/hermes-agent-chat-tanya-expense).

## Step by Step

1. **Tentukan budget per kategori.** Mulai dari rata-rata 3 bulan terakhir, bukan angka ideal. Kalau rata-rata F&B Rp 3,1 juta, pasang budget Rp 2,5 juta langsung berarti notifikasi tiap malam dan akhirnya diabaikan.
2. **Buat query agregasi.** Total transaksi per kategori untuk bulan berjalan. Satu query, satu tabel. Kalau data expense sudah rapi di SQLite, ini bagian termudah.
3. **Atur jadwal.** Saya pilih 21.30 karena setelah itu transaksi hari itu sudah masuk pipeline foto struk, dan masih ada waktu untuk mengubah rencana makan malam besok.
4. **Tulis aturan ambang.** Diam di bawah 70% itu penting — notifikasi yang datang terus-terusan mati rasa lebih cepat daripada tidak ada notifikasi sama sekali.
5. **Tes dengan data bulan lalu.** Jalankan job terhadap data Juli. Kalau outputnya masuk akal — kategori mana yang tembus, kapan tembus — baru aktifkan untuk bulan berjalan.

## Minggu Pertama: 9 Notifikasi, 4 Salah Sasaran

Setup-nya selesai 40 menit. Tuning-nya yang makan waktu.

Minggu pertama Agustus, bot mengirim 9 notifikasi. Lima berguna. Empat lainnya salah sasaran: transaksi makan siang tim masuk kategori F&B padahal itu biaya operasional, satu transfer antar-rekening kehitung sebagai pengeluaran, dan dua transaksi kategori "lainnya" yang belum dinormalisasi ikut dihitung sebagai F&B.

Koreksinya butuh dua hari. Saya menambahkan aturan: transfer antar-rekening dikecualikan, kategori "lainnya" tidak diikutkan ke perhitungan F&B, dan transaksi yang ditandai "reimburse tim" dipisah kolomnya. Setelah itu akurasinya stabil — sejak 12 Agustus, tidak ada lagi notifikasi yang saya rasa salah.

## Angkanya Setelah 3 Minggu

Juli 2026, bulan sebelum alarm dipasang: F&B selesai di Rp 3,1 juta — 24% di atas budget, dan saya baru tahu pas review. Agustus, dengan alarm aktif sejak tanggal 1: notifikasi pertama datang tanggal 9 (F&B 71%), kedua tanggal 15 (78%), ketiga tanggal 21 (82%, yang mengawali artikel ini).

Perbedaan yang paling terasa bukan di angka akhir, tapi di keputusan harian. Tanggal 22, setelah notifikasi 82%, saya menunda dua rencana makan malam di luar ke minggu depan. Tidak ada yang dramatis — hanya dua keputusan kecil yang sebelumnya tidak pernah saya ambil karena tidak tahu posisinya. Di akhir bulan, F&B berhenti di Rp 2,64 juta. Masih di atas budget, tapi 15% lebih hemat dari Juli, dan untuk pertama kalinya dalam 6 bulan saya tahu angkanya sebelum bulan berakhir.

Saya juga belajar batasnya: alarm tidak menggantikan [review bulanan](/blog/mid-year-financial-review-hermes-agent). Alarm menjawab "di mana saya sekarang"; review menjawab "kenapa polanya begini". Keduanya butuh data yang sama, tapi pertanyaannya beda.

## FAQ

**Q: Apakah perlu bisa coding untuk memasang ini?**
A: Tidak. Bagian teknisnya: query SQL sederhana, file YAML untuk budget, dan konfigurasi job terjadwal. Kalau data expense sudah ada di database, total waktu setup sekitar satu jam, termasuk tuning.

**Q: Kenapa pakai Telegram, bukan aplikasi budget komersial?**
A: Karena datanya sudah ada di sistem saya sejak April. Menambahkan aplikasi baru berarti memindahkan 1.800+ transaksi dan membayar langganan — persis kategori yang sedang saya kendalikan. Notifikasi lewat Telegram gratis dan langsung bisa dibaca tanpa buka aplikasi lain.

**Q: Apakah ambang 70% cocok untuk semua orang?**
A: Tidak. Ambang harus mengikuti pola pengeluaran. Kalau pengeluaran di awal bulan biasanya besar, ambang 70% terlalu dini. Saya memilih diam-di-bawah-70% karena pola saya merata; sesuaikan dengan data 3 bulan terakhir Anda sendiri.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 7 Agustus 2026.*

## Referensi

- [Getting to the Top of Mind: How Reminders Increase Saving](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1652784) — Karlan, McConnell, Mullainathan & Zinman, Management Science (2016): pengingat berkala meningkatkan perilaku menabung
- [Tren Rerata Pengeluaran Bulanan Warga Indonesia 2021–2025](https://databoks.katadata.co.id/pdb/statistik/68f056ea3da70/tren-rerata-pengeluaran-bulanan-warga-indonesia-periode-2021-2025) — Data BPS lewat Databoks Katadata: pengeluaran rumah tangga Indonesia terus naik tiap tahun
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk konfigurasi job terjadwal dan akses tools
