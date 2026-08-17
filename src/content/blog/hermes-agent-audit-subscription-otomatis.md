---
title: "Audit Langganan Otomatis: Hermes Agent Menemukan Rp 5,8 Juta Setahun yang Menguap"
description: "Hermes Agent mengaudit pengeluaran berulang saya: 3 langganan mati rasa ketahuan, Rp 487.500/bulan berhenti mengalir. Cara pasang audit mingguan, dan kenapa audit manual selalu gagal."
pubDate: 2026-08-18
heroImage: "../../assets/hero-hermes-agent-audit-subscription-otomatis.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Audit Langganan Otomatis: Hermes Agent Menemukan Rp 5,8 Juta Setahun yang Menguap

Minggu kedua Agustus 2026, saya duduk dengan kopi sambil membaca laporan mingguan yang dikirim Hermes Agent ke Telegram. Biasanya laporan ini soal ringkasan pengeluaran, jadi saya baca sekilas sambil sarapan. Sampai muncul satu baris yang membuat saya berhenti mengunyah:

"Pengeluaran berulang bulan ini: 9 entri, total Rp 2.340.000. Empat entri tanpa tanda pemakaian dalam 60 hari terakhir."

Saya sudah menduga angkanya ada di sana. Tapi melihat empat langganan sekaligus dalam satu daftar — bukan tersebar di empat email tagihan yang berbeda — rasanya berbeda.

## Kenapa Langganan Bisa Mati Rasa

Semua langganan itu saya aktifkan sendiri, dan masing-masing terasa masuk akal saat itu. Cloud storage 2TB pas disk penuh. Aplikasi AI writing pas saya lagi rajin menulis. VPN tahunan pas masa pandemi, saat saya kerja remote dan butuh akses ke beberapa layanan luar negeri.

Masalahnya bukan keputusan awal, tapi tidak adanya keputusan lanjutan. Auto-renew jalan sendiri, kartu tersimpan otomatis, dan email tagihan tenggelam di antara 40 email lain. Tidak ada momen di mana saya harus memilih lagi.

Ini pola yang terukur di banyak riset. Survei subscription spending 2026 dari [resubs.app](https://resubs.app/resources/subscription-spending-statistics) menemukan rata-rata orang Amerika membayar US$219 per bulan untuk 8,2 layanan, padahal mereka memperkirakan hanya US$86 — gap persepsi 2,5 kali lipat. Riset [justcancel.io](https://www.justcancel.io/research/subscription-spending-statistics) menambahkan: sekitar US$32 per bulan mengalir ke langganan yang dilupakan. Angka rupiahnya pasti beda, tapi polanya sama: orang membayar lebih banyak daripada yang mereka sadari, dan tidak ada yang menagih kesadaran itu selain rekening koran.

Saya sendiri bukan pengecualian. Antara Januari dan Mei 2026, saya membayar dua langganan tanpa pernah membukanya: satu aplikasi catatan premium yang saya lupakan, dan satu storage tambahan yang ternyata tidak pernah saya isi. Saya baru sadar saat [mencatat semua expense otomatis](/blog/setup-hermes-agent-expense-tracking) mulai April dan angkanya terkumpul di satu tempat.

## Audit Berulang, Bukan Audit Ingatan

Audit manual punya dua kelemahan: pertama, hanya jalan saat ada momen "saya harus hemat" — lalu dilupakan. Kedua, bergantung pada ingatan, padahal ingatan justru yang gagal di sini.

Yang saya pasang sekarang adalah job mingguan di Hermes Agent, di VM yang sama dengan [budget alert](/blog/hermes-agent-budget-alert-telegram) dan [bot chat expense](/blog/hermes-agent-chat-tanya-expense):

1. **Query transaksi berulang.** Dari database SQLite yang sudah menampung semua transaksi sejak April, satu query mengelompokkan transaksi per merchant, lalu memfilter yang muncul minimal 3 bulan berturut-turut dengan nominal sama atau hampir sama.
2. **Filter yang benar-benar berulang.** Nominal tetap bulanan. Saya mengecualikan transaksi dengan pola tidak tetap seperti listrik atau air, karena itu bukan langganan dan tidak bisa dicabut.
3. **Cross-check pemakaian.** Ini bagian yang tidak bisa dilakukan query: apakah langganannya benar-benar dipakai? Saya memakai dua sumber — log aktivitas aplikasi kalau ada, dan catatan jujur: kapan terakhir kali saya membuka layanan itu.
4. **Job mingguan.** Setiap Senin 08.00, Hermes Agent mengirim daftar ke Telegram: nama layanan, nominal, bulan terakhir pemakaian, dan status rekomendasi. Pola pengirimannya sama dengan [briefing pagi](/blog/hermes-agent-daily-briefing-telegram) yang sudah jalan lebih dulu.
5. **Deadline keputusan.** Setiap entri yang muncul dua minggu berturut-turut tanpa keputusan otomatis naik statusnya jadi "perlu dicabut atau dipertahankan secara eksplisit".

Setup-nya sendiri tidak sampai satu jam — sebagian besar sudah ada dari [pencatatan expense otomatis](/blog/setup-hermes-agent-expense-tracking) yang datanya memang tersimpan terstruktur sejak awal. Bagian tersulitnya bukan teknis, tapi membuat aturan review yang tidak bisa saya tunda-tunda.

## Yang Ditemukan dan Berapa yang Berhenti

Audit minggu pertama menemukan 9 entri berulang. Tiga di antaranya jelas mati rasa:

1. **Cloud storage 2TB — Rp 149.000/bulan.** Saya berhenti mengunggah sejak Januari, dan 90 hari terakhir tidak ada satu file pun yang diakses dari akun itu. File lama tetap tersimpan, jadi saya pindahkan ke storage yang lebih murah sebelum mencabut.
2. **Aplikasi AI writing — Rp 195.000/bulan.** Dulu dipakai untuk draft artikel, lalu saya menggantinya dengan workflow internal Qawwa yang hasilnya lebih sesuai. Aplikasinya tetap bagus, tapi untuk saya tidak lagi.
3. **VPN tahunan — Rp 143.500/bulan.** Sejak kembali bekerja penuh dari kantor tahun lalu, saya tidak pernah membukanya lagi. Satu-satunya alasan bertahan: "dulu sering dipakai".

Total: Rp 487.500 per bulan, atau Rp 5.850.000 per tahun. Yang dipertahankan tetap enam: layanan yang benar-benar dipakai mingguan — tool desain tim, penyimpanan dokumen kerja, streaming keluarga, dan tiga lainnya yang masuk kategori kerja.

Pelajaran paling jujur dari proses ini: daftar saja tidak cukup. Setelah laporan pertama keluar, saya butuh dua hari untuk benar-benar mencabut tiga langganan itu. Bukan karena ragu — karena menunda adalah default. Deadline keputusan di poin lima yang membuat prosesnya tuntas; tanpa itu, laporan mingguan hanya jadi daftar yang saya baca lalu tutup.

## Angka Setelah Satu Minggu

Pengeluaran berulang bulanan saya turun dari Rp 2.340.000 menjadi Rp 1.852.500 — turun 21%. Proyeksi setahun: hemat sekitar Rp 5,85 juta.

Nominal ini kecil untuk ukuran perusahaan. Tapi yang paling berharga bukan uangnya: tiga langganan itu mengalir tanpa keputusan selama berbulan-bulan, dan satu-satunya alasan mereka berhenti adalah ada sistem yang rutin bertanya "masih kamu pakai?". Pertanyaan itu dulunya tidak pernah muncul karena tidak ada yang menanyakannya.

Kalau transaksi Anda belum terkumpul di satu tempat, [mulai dari pencatatan otomatis](/blog/setup-hermes-agent-expense-tracking) dulu. Kalau sudah, audit ini bisa dipasang dalam satu sore — dan jawabannya jarang menyenangkan, tapi selalu lebih baik daripada tahu lima tahun kemudian.

## FAQ

**Q: Apakah perlu aplikasi khusus untuk audit langganan?**
A: Tidak. Yang dibutuhkan hanya database transaksi yang terstruktur dan job terjadwal — keduanya bisa dijalankan Hermes Agent di VM atau komputer yang menyala rutin. Dokumentasi lengkap tentang scheduled jobs ada di [dokumentasi Hermes Agent](https://hermes-agent.nousresearch.com/docs).

**Q: Bagaimana tahu sebuah langganan benar-benar tidak dipakai?**
A: Dua sumber: log aktivitas aplikasi kalau tersedia, dan kejujuran. Kalau Anda harus berpikir lebih dari lima detik kapan terakhir memakainya, itu sudah tanda yang kuat. Log transaksi juga membantu — lihat kapan terakhir ada aktivitas yang memicu tagihan.

**Q: Seberapa sering audit langganan perlu dijalankan?**
A: Bulanan cukup untuk kondisi stabil. Saya menjalankan mingguan selama tiga bulan pertama karena masih ada langganan lama yang belum terpetakan, lalu menurunkannya ke bulanan. Yang penting konsisten, bukan sering.

## Tentang Penulis

Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.
