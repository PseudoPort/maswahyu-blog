---
title: "Audit Waktu 60 Hari dengan Hermes Agent: 41% Jam Kerja Saya Habis untuk Admin"
description: "Melacak 60 hari kerja dengan Hermes Agent: 41% jam habis untuk admin, dua kali perkiraan awal. Tiga otomasi memotongnya jadi 24%. Setup lengkap di sini."
pubDate: 2026-08-21
heroImage: "../../assets/hero-hermes-agent-audit-waktu-jam-kerja.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Audit Waktu 60 Hari dengan Hermes Agent: 41% Jam Kerja Saya Habis untuk Admin

Pertengahan Juli 2026, jam 21.40, saya membaca laporan mingguan dari Hermes Agent. Laporan ini bukan soal uang — sudah ada [audit langganan](/blog/hermes-agent-audit-subscription-otomatis) dan [proyeksi arus kas](/blog/hermes-agent-proyeksi-arus-kas) untuk itu. Ini laporan waktu: ringkasan 42 hari kerja yang saya catat, dikelompokkan otomatis, dikirim setiap Minggu jam 19.00 ke Telegram.

Angka pertamanya: **41% jam kerja saya habis untuk admin.** Bukan untuk klien, bukan untuk produk, bukan untuk keputusan. Admin: copy-paste data antar aplikasi, cari file, rekap laporan, balas chat yang isinya cuma "statusnya gimana".

Saya kaget bukan karena angkanya besar. Saya kaget karena perkiraan saya di awal cuma 20%. Dua kali lipat, dan saya tidak menyadarinya selama bertahun-tahun.

## Kenapa Saya Mulai Mencatat Waktu

Setelah [expense tracking](/blog/setup-hermes-agent-expense-tracking) dan [email otomatis](/blog/hermes-agent-email-inbox-otomatis) jalan, bottleneck berikutnya terasa jelas: hari kerja habis tanpa jejak. Saya tahu persis berapa rupiah yang keluar bulan ini, tapi tidak tahu jam kerja saya pergi ke mana.

Perasaan "hari ini sibuk banget" tidak memberi data. Semua orang merasa sibuk. Bedanya, perasaan bisa menipu — data tidak.

Jadi pertengahan Mei 2026 saya pasang aturan sederhana: ukur dulu selama 60 hari sebelum mengubah apa pun. Dua minggu pertama terasa membosankan dan manual. Tapi itulah poinnya — saya tidak mau mengotomasi sesuatu yang belum saya pahami polanya.

## Setup-nya: Tiga Sumber Data, Satu Laporan

Tidak ada aplikasi time tracker baru. Saya pakai data yang sudah ada, plus satu catatan harian:

1. **Kalender.** Semua meeting dan blok kerja sudah tercatat di Google Calendar. Hermes Agent membaca jadwal harian dan mengelompokkan: meeting internal, meeting klien, blok fokus.
2. **Log aktivitas.** Aplikasi yang saya pakai (email, chat, spreadsheet, editor) mencatat sesi pemakaian. Agent mengambilnya tiap malam dan memberi label kategori.
3. **Jurnal 18.00.** Satu prompt di Telegram setiap sore: "Tiga hal yang kamu kerjakan hari ini, masing-masing berapa menit, dan mana yang terasa sia-sia?" Butuh 3-5 menit. Bagian ini yang paling jujur, karena tidak bisa dibaca dari log.

Setiap Minggu 19.00, agent menggabungkan ketiganya, memotong duplikasi (misalnya meeting yang tercatat di kalender tapi tidak di log aktivitas), dan mengirim laporan ke Telegram dengan format yang sama seperti [briefing pagi](/blog/hermes-agent-daily-briefing-telegram): ringkasan, breakdown per kategori, dan perbandingan dengan minggu sebelumnya.

## Hasil 60 Hari: 128 Jam untuk Admin

Dari 42 hari kerja efektif, total 312 jam tercatat. Rinciannya:

- **41% admin (128 jam)** — sekitar 3 jam per hari kerja
- **27% meeting (84 jam)**
- **19% kerja teknis & produk (59 jam)**
- **13% review, baca, riset (41 jam)**

Di dalam 128 jam admin, empat item terbesar:

- Balas chat "status gimana" dan follow-up manual: 34 jam
- Copy-paste data antar aplikasi: 26 jam
- Input struk dan invoice manual: 29 jam
- Cari file dan informasi: 21 jam
- Rekap laporan manual: 18 jam

Sisanya 128 − (34+26+29+21+18) = 0. Persis.

Pola ini bukan anomali. [Anatomy of Work Index 2023 dari Asana](https://asana.com/resources/anatomy-of-work-index) menemukan knowledge worker rata-rata menghabiskan 58% hari untuk "work about work" — komunikasi tentang pekerjaan, cari informasi, pindah antar tool. Angka saya 41%, di bawah rata-rata, karena email dan expense sudah lebih dulu otomatis. Kalau tidak, mungkin angkanya 50% ke atas.

## Tiga Otomasi yang Saya Pasang

Saya tidak mengotomasi semuanya. Saya pilih tiga item terbesar, karena 34+26+18 = 78 jam, atau 61% dari total admin:

1. **Follow-up chat (34 jam).** [Order dari chat](/blog/hermes-agent-order-chat-otomatis) yang sudah jalan untuk pesanan saya perluas: sekarang agent juga mengecek chat yang belum dibalas lebih dari 4 jam di jam kerja, mengelompokkannya, dan menagih saya satu kali per dua jam — bukan setiap chat masuk. Balasan "status gimana" berkurang drastis karena status pesanan otomatis dikirim ke pembeli saat berubah.

2. **Rekap laporan (18 jam).** Laporan mingguan yang dulu saya susun dari Excel, catatan meeting, dan email sekarang di-generate agent dari database expense dan [catatan meeting](/blog/hermes-agent-meeting-notes-action-items). Saya tinggal review 10 menit sebelum dikirim. Dulu 2,5 jam per minggu.

3. **Input struk dan invoice (29 jam).** Sebagian sudah teratasi [workflow OCR](/blog/hermes-agent-ocr-struk-akurasi-workflow). Yang tersisa adalah verifikasi — dan itu saya otomatiskan dengan aturan: struk di bawah Rp 500.000 langsung masuk tanpa review, di atas itu masuk antrian verifikasi sore hari.

30 hari setelah otomasi itu jalan, admin turun dari 41% ke 24%. Artinya sekitar 27 jam per bulan kembali — 3,5 hari kerja, tanpa menambah jam lembur.

## Yang Tidak Saya Otomatiskan

Meeting klien, keputusan strategis, dan blok kerja teknis tetap manual. Bukan karena tidak bisa, tapi karena di situlah nilai saya.

Analisis [McKinsey tentang otomasi](https://www.mckinsey.com/capabilities/operations/our-insights/human-plus-machine-a-new-era-of-automation-in-manufacturing) menunjukkan potensi otomasi bervariasi per sektor — di apparel 82% jam kerja berpotensi otomatis, di food 76%, beverages 69%. Yang menarik: di pekerjaan yang paling bisa diotomasi sekalipun, sisa jam kerjanya justru yang paling berharga — judgment, negosiasi, hubungan. Otomasi tidak menggantikan itu. Otomasi memberi ruang untuk itu.

## Pelajaran: Ukur Dulu, Otomasi Kemudian

Kesalahan terbesar yang saya lihat di UKM lain: langsung pasang AI di mana-mana tanpa tahu masalahnya di mana. Saya hampir melakukan hal yang sama — sempat mau otomasi cari file (21 jam) sebelum sadar follow-up chat (34 jam) justru lebih besar.

Dua bulan mencatat mengubah perilaku sebelum otomasi apa pun jalan. Begitu saya melihat "34 jam untuk chat" dalam satu baris laporan, saya otomatis mulai membalas lebih cepat dan lebih singkat. Data sendiri sudah jadi intervensi.

Kalau Anda pemilik usaha, mulailah dari yang sama: satu kalender yang rapi, satu jurnal harian, satu laporan mingguan. Satu bulan saja. Angka yang keluar mungkin tidak nyaman — tapi itu titik awal yang jauh lebih baik daripada menebak.

## FAQ

**Berapa lama setup audit waktu dengan Hermes Agent?**
Sekitar 2-3 jam untuk sumber data (kalender, log aktivitas, prompt jurnal) dan laporan mingguan. Sisanya iterasi: dua minggu pertama saya sesuaikan kategori dan cara agent membedakan meeting dari blok fokus.

**Apakah harus mencatat manual tiap hari?**
Cukup jurnal 18.00 selama 3-5 menit. Kalender dan log aktivitas otomatis. Tanpa jurnal, laporan tetap jalan, tapi Anda kehilangan bagian paling jujur — alasan di balik aktivitas, bukan cuma aktivitasnya.

**Berapa jam yang realistis bisa dihemat UKM dari audit waktu?**
Di kasus saya 27 jam per bulan dari tiga otomasi. Tapi itu setelah data selama 60 hari. UKM yang baru mulai biasanya menemukan 20-30% jam kerja untuk admin — angka itu sudah menjadi target otomasi yang jelas.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini diperbarui: 21 Agustus 2026. Pertama kali dipublikasikan: 21 Agustus 2026.*

## Referensi

- [Asana Anatomy of Work Index 2023](https://asana.com/resources/anatomy-of-work-index) — knowledge worker menghabiskan 58% hari untuk "work about work"
- [McKinsey: Human + machine — A new era of automation](https://www.mckinsey.com/capabilities/operations/our-insights/human-plus-machine-a-new-era-of-automation-in-manufacturing) — potensi otomasi jam kerja per sektor: apparel 82%, food 76%, beverages 69%
