---
title: "Mid-Year Financial Review dengan Hermes Agent: Saya Temukan Rp 4,3 Juta Menguap dalam 6 Bulan"
description: "Juli 2026 saya minta Hermes Agent audit 6 bulan pengeluaran. Hasilnya: 3 langganan tidak terpakai, total Rp 4,32 juta. Ini cara saya menjalankan review-nya."
pubDate: 2026-08-02
heroImage: "../../assets/hero-mid-year-financial-review-hermes-agent.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Mid-Year Financial Review dengan Hermes Agent: Saya Temukan Rp 4,3 Juta Menguap dalam 6 Bulan

Sabtu pagi, awal Juli 2026. Saya duduk dengan kopi dan satu pertanyaan yang mengganggu sejak Mei: enam bulan setelah pindah dari Excel ke Hermes Agent, ke mana saja uang saya sebenarnya pergi?

Angkanya sudah ada — 1.847 transaksi tercatat otomatis sejak Januari. Tapi data mentah tidak sama dengan keputusan. Butuh analisis: kategori mana yang membengkak, langganan mana yang tidak terpakai, dan kebocoran mana yang tidak saya sadari.

Jadi saya minta agent melakukan mid-year review. Bukan "rekap pengeluaran" — itu bisa dilakukan Excel. Tapi audit: membandingkan pemakaian, menandai anomali, dan memberi rekomendasi.

## Kenapa Review Manual Selalu Gagal

Sebelumnya, review keuangan saya bentuknya: buka Excel, filter per kategori, buat pivot table, lalu "nanti ah kalau ada waktu". Hasilnya — review terakhir yang benar-benar selesai adalah Maret, padahal sudah lewat 4 bulan. Butuh 2-3 hari kerja yang terpecah-pecah, dan selalu selesai setelah keputusan sudah terlanjur diambil.

Polanya klasik: autodebit jalan terus, tidak ada friction, jadi tidak ada yang menyadari langganan yang tidak pernah dibuka.

C+R Research mencatat konsumen memperkirakan belanja langganan mereka $86 per bulan, padahal angka sebenarnya $219 — selisih 2,5 kali lipat ([sumber](https://www.lowermysubs.com/blog/subscription-statistics)). Saya rasa angka Indonesia tidak jauh berbeda. Langganan Rp 59 ribu di sini, Rp 149 ribu di sana; semuanya lewat autodebit, dan tidak pernah dicek lagi.

## Menjalankan Review dengan Hermes Agent

Saya tidak menulis prompt sekali jadi. Butuh tiga iterasi:

1. **"Rekap pengeluaran 6 bulan"** — hasilnya cuma tabel per kategori. Kurang dalam.
2. **"Cari langganan berulang, bandingkan dengan pemakaian, tandai yang tidak dipakai 60 hari terakhir"** — agent membaca data transaksi, mengelompokkan merchant berulang, lalu mencocokkan dengan riwayat aktivitas.
3. **"Beri output berupa keputusan, bukan data"** — daftar langganan, nominal per bulan, total 6 bulan, status (dipakai / diragukan / tidak dipakai), dan rekomendasi.

Prompt final butuh sekitar 25 menit untuk disusun. Output lengkap keluar dalam 11 menit — termasuk membaca 1.847 transaksi. Kalau manual, ini pekerjaan 2 hari.

## Yang Ditemukan: 7 Langganan, 3 Tidak Terpakai

Hasil audit: 7 langganan aktif, total Rp 2,34 juta per bulan.

Yang tidak terpakai (tidak ada aktivitas 60+ hari):

- **SaaS project management: Rp 349 ribu/bulan** — tim sudah pindah ke tool lain sejak Februari
- **Cloud storage tambahan 2 TB: Rp 189 ribu/bulan** — terpakai sampai 412 GB saja
- **Aplikasi habit tracker: Rp 69 ribu/bulan** — terakhir dibuka November 2025

Tiga itu total Rp 607 ribu/bulan. Kalikan 6 bulan: Rp 3,64 juta. Plus dua langganan yang pemakaiannya di bawah 20%: total kebocoran **Rp 720 ribu/bulan, atau Rp 4,32 juta selama Januari–Juni.**

Saya cancel tiga langganan hari itu juga. Dua sisanya saya turunkan ke paket lebih kecil. Hemat bulanan: **Rp 720 ribu** — setara gaji satu karyawan paruh waktu di tim support, atau Rp 8,64 juta per tahun.

## Dua Hal yang Tidak Akan Saya Lihat Tanpa Agent

1. **Pola tanggal.** Agent menemukan 60% transaksi "makan di luar" terjadi Jumat–Minggu. Bukan temuan besar, tapi mengubah cara saya mengatur uang mingguan.
2. **Duplikasi pembayaran.** Satu langganan ditagih dua kali di bulan Maret — saya tidak pernah menyadarinya karena dua merchant dengan nama berbeda. Refund Rp 349 ribu.

Keduanya tidak mungkin muncul dari laporan bulanan standar bank. Butuh pembacaan lintas transaksi yang membandingkan konteks — persis yang sulit dilakukan manusia saat data sudah 1.800+ baris.

## Cara Kerja Review Berikutnya

Sekarang review ini jalan otomatis tiap akhir bulan. Hermes Agent punya scheduler cron bawaan, jadi setiap tanggal 1 saya dapat satu halaman: ringkasan, anomali, rekomendasi. Saya tinggal baca dan putuskan.

Yang dulu butuh 2-3 hari terpecah-pecah, sekarang 11 menit tiap bulan. Kuncinya bukan "AI menggantikan keputusan". Kuncinya: data yang dulu butuh 1.847 baris manual untuk dipahami, sekarang bisa dibaca dalam satu pesan.

## Tiga Pelajaran

1. **Langganan adalah kebocoran yang paling jarang diperiksa.** Kalau autodebit jalan, tidak ada friction untuk lupa.
2. **Review keuangan tidak perlu menunggu momen besar.** Bulanan, 11 menit, lebih baik dari "nanti ah" yang berakhir 4 bulan.
3. **Prompt yang bagus butuh iterasi.** Versi pertama saya datar; versi ketiga yang memberi keputusan, bukan data.

Kalau kamu masih mencatat pengeluaran manual di Excel atau aplikasi catatan, mulainya dari sana — karena review sebagus apa pun tidak akan membantu kalau datanya tidak ada. Setup lengkap expense tracking dengan Hermes Agent sudah saya tulis di [artikel sebelumnya](/blog/setup-hermes-agent-expense-tracking/). Dokumentasi resmi Hermes Agent ada di [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs).

**Q: Apakah Hermes Agent bisa dipakai untuk expense tracking tanpa coding?**
A: Bisa. Setup awal butuh CLI dan konfigurasi, tapi setelah jalan, interaksi lewat Telegram biasa. Tutorial setup lengkap ada di artikel sebelumnya.

**Q: Berapa biaya menjalankan Hermes Agent untuk review keuangan pribadi?**
A: Saya menjalankannya di server Ubuntu sendiri dengan RAM 8GB; biaya utamanya listrik dan API key untuk model LLM — jauh di bawah langganan SaaS yang berhasil saya hapus.

**Q: Apa bedanya dengan aplikasi budgeting seperti Money Lover atau Catatan Keuangan?**
A: Aplikasi budgeting bagus untuk input dan laporan standar. Hermes Agent bisa ditarik lebih jauh: membaca konteks, mencocokkan langganan dengan pemakaian, dan memberi rekomendasi — bukan cuma grafik.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*
