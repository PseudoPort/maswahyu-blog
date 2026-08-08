---
title: "Proyeksi Arus Kas 3 Bulan dengan Hermes Agent: Agent Bilang Oktober Saya Minus Rp 4,8 Juta"
description: "Agustus 2026, Hermes Agent memproyeksikan arus kas saya minus Rp 4,8 juta di Oktober — dua bulan sebelum terjadi. Ini prompt, output, dan keputusan yang saya ambil."
pubDate: 2026-08-09
heroImage: "../../assets/hero-hermes-agent-proyeksi-arus-kas.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Proyeksi Arus Kas 3 Bulan dengan Hermes Agent: Agent Bilang Oktober Saya Minus Rp 4,8 Juta

Jumat malam, awal Agustus 2026. Saya buka Telegram dan menemukan pesan dari Hermes Agent yang saya minta pagi tadi: proyeksi arus kas tiga bulan ke depan.

Bacaannya pendek. **September: +Rp 2,1 juta. Oktober: −Rp 4,8 juta. November: +Rp 6,2 juta.**

Oktober minus. Dua bulan dari sekarang. Kalau tidak ada pesan ini, saya baru tahu ketika saldo di aplikasi bank mulai menyentuh angka kecil — seperti Agustus tahun lalu, ketika saya membayar gaji tiga karyawan sambil berharap transfer klien masuk duluan.

## Dari 2.131 Transaksi ke Proyeksi

Agent bekerja dari data yang sudah tercatat otomatis sejak Januari: 2.131 transaksi masuk dan keluar, ditambah jadwal piutang dari sistem reminder yang sudah saya pakai untuk menagih klien.

Bedanya dengan laporan bulanan biasa: laporan melihat ke belakang, proyeksi melihat ke depan. Untuk itu agent butuh konteks yang tidak ada di rekening koran:

- **Tagihan tahunan yang jatuh tempo Oktober** — asuransi server Rp 2,4 juta, perpanjangan domain dan infrastruktur Rp 1,6 juta, lisensi software Rp 800 ribu.
- **Pola musiman** — pendapatan dari klien ritel konsisten turun 20–30% di bulan-bulan tertentu.
- **Jadwal piutang** — kapan klien besar seharusnya membayar, berdasarkan riwayat pembayaran mereka, bukan tanggal jatuh tempo kontrak.

Bisa saya hitung manual? Angka sederhananya bisa. Tapi setiap kali satu asumsi berubah — klien telat, tagihan baru muncul, harga naik — semua hitungan harus diulang. Dengan 14 item pengeluaran dan 3 skenario, itu pekerjaan satu jam yang tidak pernah saya selesaikan karena selalu ada email yang lebih mendesak.

Agent menghitung ulang dalam hitungan detik.

## Prompt yang Saya Pakai

Prompt pertama saya jelek: *"proyeksi arus kas 3 bulan"*. Outputnya cuma rata-rata pemasukan dikurangi rata-rata pengeluaran — tidak berguna, tidak ada Oktober minus di situ.

Prompt kedua saya tambah sumber datanya. Prompt ketiga yang akhirnya jalan:

> "Gunakan data transaksi Januari–Juli 2026. Kas akhir = kas awal + pemasukan terjadwal − pengeluaran tetap − pengeluaran variabel (rata-rata 3 bulan). Masukkan: tagihan tahunan dengan tanggal jatuh temponya, jadwal piutang berdasarkan riwayat pembayaran klien, dan pola musiman pendapatan. Output: tabel per bulan untuk Agustus, September, Oktober, dengan asumsi yang kamu pakai."

Outputnya tabel tiga kolom: bulan, perkiraan kas akhir, dan daftar asumsi. Yang membuat saya berhenti sebentar adalah baris Oktober: minus Rp 4,8 juta, dengan penjelasan — tiga tagihan tahunan jatuh tempo berdekatan, sementara klien terbesar baru membayar awal November.

Butuh 20 menit untuk menyusun prompt final. Eksekusinya 4 menit.

## Skenario: Kalau Klien Telat Bayar

Bagian yang paling sering saya pakai bukan tabelnya, tapi skenario.

Satu klien, nilai kontrak Rp 12 juta per bulan, punya kebiasaan telat membayar 1–2 minggu. Saya minta agent hitung ulang dengan asumsi pembayaran klien itu mundur 30 hari. Hasilnya: Oktober minus Rp 4,8 juta menjadi minus Rp 7,6 juta.

Dua keputusan keluar dari situ:

1. **Saya negosiasi perpanjangan asuransi server** — pembayaran digeser dari Oktober ke November. Pihak vendor setuju; tidak ada biaya tambahan.
2. **Saya tagih klien besar itu seminggu lebih awal** dari biasanya, dengan alasan yang masuk akal: penutupan kuartal.

Hasil akhirnya: Oktober −Rp 1,1 juta, November +Rp 6,4 juta. Masih minus di Oktober, tapi minus yang bisa saya tutup dari dana darurat tanpa menyentuh gaji karyawan. Itu perbedaan antara panik dan terkendali.

## Batasannya

Jujur soal ini: proyeksi sebaik data yang masuk.

Pernah saya lupa mencatat tiga pengeluaran tunai total Rp 900 ribu. Proyeksi meleset 12% — bukan angka yang mengubah keputusan, tapi cukup untuk mengingatkan bahwa agent menghitung asumsi, bukan membaca masa depan. Kalau asumsinya salah, outputnya ikut salah.

Hermes Agent tidak menggantikan akuntan. Fungsi saya pakai: membesarkan anomali lebih awal. Angka literasi keuangan Indonesia memang naik ke 65,43% dalam Survei Nasional Literasi dan Inklusi Keuangan 2024 ([OJK](https://finance.detik.com/moneter/d-7469835/hasil-survei-orang-ri-melek-keuangan-65-43-dan-punya-akses-75-02)), tapi yang rutin memproyeksikan arus kas ke depan masih langka — karena datanya tersebar dan hitungannya membosankan. Di situlah automation bekerja.

## Tiga Pelajaran

1. **Laporan melihat ke belakang, proyeksi melihat ke depan.** Keduanya butuh data yang sama; bedanya konteks yang disuntikkan ke dalamnya.
2. **Prompt yang baik mendefinisikan formula dan skenario**, bukan minta "analisis". Semakin eksplisit asumsinya, semakin bisa dipercaya outputnya.
3. **Delapan bulan data yang konsisten membuat prediksi jadi mungkin.** Proyeksi tidak akan berguna kalau pencatatannya tidak jalan duluan.

Kalau kamu masih mencatat pengeluaran manual, mulailah dari pencatatan — cara setup expense tracking dengan Hermes Agent ada di [artikel setup](/blog/setup-hermes-agent-expense-tracking/), dan cerita audit 6 bulan pertama ada di [mid-year review](/blog/mid-year-financial-review-hermes-agent/). Dokumentasi resmi agent ada di [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs), dan dasar-dasar pengelolaan keuangan pribadi bisa dilihat di [Sikapi Uangmu OJK](https://sikapiuangmu.ojk.go.id).

**Q: Bisakah proyeksi arus kas otomatis dibuat tanpa coding?**
A: Bisa. Setup awal butuh CLI dan konfigurasi, tapi setelah jalan, cukup minta lewat Telegram. Tutorial lengkap ada di artikel setup yang saya tautkan di atas.

**Q: Seberapa akurat proyeksinya?**
A: Dengan 8 bulan data lengkap, proyeksi saya meleset sekitar 12% saat ada pengeluaran yang tidak tercatat. Makin konsisten pencatatan, makin kecil penyimpangannya.

**Q: Apakah ini menggantikan jasa akuntan?**
A: Tidak. Ini alat peringatan dini untuk arus kas. Urusan pajak, kepatuhan, dan laporan resmi tetap butuh akuntan.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*
