---
title: "Menghadapi SPT Tahunan dengan Hermes Agent: 322 Transaksi Berantakan Jadi Laporan Siap Hitung"
description: "Maret 2026, deadline SPT. Data 2025 masih Excel campur aduk. Hermes Agent ubah 322 transaksi jadi laporan siap hitung dalam 90 menit."
pubDate: 2026-08-17
heroImage: "../../assets/hero-hermes-agent-data-spt-tahunan.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Menghadapi SPT Tahunan dengan Hermes Agent: 322 Transaksi Berantakan Jadi Laporan Siap Hitung

Minggu ketiga Maret 2026. Saya buka file `Expense_2025_final_FINAL_v3.xlsx` untuk persiapan SPT Tahunan — file yang sama yang membuat saya pindah ke Hermes Agent dua bulan sebelumnya. Deadline 31 Maret tinggal 11 hari, dan di dalam Excel itu ada 322 baris transaksi dengan kategori yang campur aduk: "makan", "makanan", "makan siang klien", "nasi padang", "belanja", "belanja bulanan", "toko". Enam nama untuk satu hal yang sama.

Dua tahun sebelumnya, ritual saya sama: buka Excel, filter kategori satu per satu, pindahkan ke sheet baru, lalu bandingkan dengan tumpukan struk di dalam amplop cokelat. Butuh tiga sampai empat hari kerja. Maret 2026, saya tidak punya waktu itu — dan saya juga tidak ingin melakukannya.

## Yang Saya Minta ke Hermes Agent

Saya tidak menyuruh agent membuatkan laporan dari nol. Saya kasih file Excel-nya, lalu minta tiga hal spesifik:

1. Normalisasi nama kategori — semua varian "makan", "makan siang klien", "nasi padang" jadi satu kategori: "F&B".
2. Pisahkan transaksi yang jelas pengeluaran pribadi (belanja rumah, sekolah anak, pulsa pribadi) dari biaya usaha.
3. Kelompokkan ulang per kategori biaya yang relevan untuk SPT: bahan baku, operasional, transportasi, sewa, marketing, gaji.

Saya sengaja tidak minta "analisis pajak" atau "saran penghematan pajak". Itu bukan tempatnya agent, dan bukan tugas yang saya percayakan ke sistem otomatis. Yang saya butuhkan adalah data yang rapi dan konsisten, supaya keputusan pajaknya tetap di tangan konsultan.

## Angkanya, Setelah 90 Menit

Agent butuh sekitar satu jam untuk menyusun skrip pembersihan data, dan setengah jam lagi untuk menjalankannya. Output pertama:

- 322 transaksi dikategorikan ulang ke 14 kategori, dari sebelumnya 27 kategori yang saling tumpang tindih.
- 41 transaksi pengeluaran pribadi terpisah — total Rp 7,2 juta yang sebelumnya tercampur dengan biaya usaha.
- 12 baris duplikat ditemukan dan ditandai, bukan dihapus otomatis. Saya hapus manual setelah cek.
- 19 transaksi masuk kategori "Lain-lain" dengan total Rp 3,4 juta — agent menandainya karena terlalu besar untuk dibiarkan tanpa penjelasan.

Kategori yang paling banyak berubah adalah transportasi. Di Excel lama, biaya tol, bensin, parkir, dan ojek online tercatat di empat kategori berbeda. Setelah dinormalisasi, total biaya transportasi 2025 keluar angka tunggal: Rp 14,8 juta. Angka itu langsung bisa dibandingkan dengan mutasi bank dan riwayat aplikasi ojek online — dan cocok.

## Yang Tidak Bisa Diotomasi

Bagian paling berharga justru terjadi setelah laporan jadi. Konsultan pajak saya minta file yang sama, dan dalam 20 menit menemukan tiga hal yang tidak akan pernah ditemukan agent:

1. Satu pembayaran vendor Rp 4,2 juta di kategori "Operasional" ternyata untuk proyek pribadi — butuh koreksi.
2. Dua struk belanja alat Rp 1,1 juta tidak punya bukti lengkap, jadi tidak bisa diklaim.
3. Kategori "Lain-lain" Rp 3,4 juta itu harus dipecah, karena sebagian termasuk biaya yang tidak boleh dikurangkan.

Saya belajar sesuatu di sini: agent sangat bagus untuk merapikan dan mengelompokkan data, tapi dia tidak tahu konteks — mana transaksi yang beneran biaya usaha, mana yang bukan. [pajak.go.id](https://www.pajak.go.id/en/node/35019) mencatat batas waktu lapor SPT Tahunan orang pribadi adalah 31 Maret, dan kesalahan klasifikasi biaya adalah salah satu hal yang paling sering memicu pemeriksaan. [KlikPajak](https://klikpajak.id/blog/pengertian-biaya-variabel-dan-biaya-tetap/) juga menegaskan bahwa biaya yang boleh dikurangkan dari penghasilan bruto diatur ketat di UU PPh — tidak semua pengeluaran otomatis bisa diklaim. Konteks itu tetap pekerjaan manusia.

## Ritual SPT yang Sekarang

Maret 2026 saya lapor lebih cepat dari biasanya: data rapi Jumat sore, konsultan cek Senin, SPT terkirim Selasa. Total waktu saya: sekitar 2 jam untuk prompt dan verifikasi, bukan 3 hari menyortir struk.

Tahun depan pekerjaannya akan lebih ringan. Seluruh 2026 sudah tercatat di Hermes Agent sejak Januari, dengan kategori yang konsisten sejak awal — tidak ada lagi 27 kategori untuk 322 transaksi. Yang saya perlukan nanti tinggal satu prompt, lalu review hasilnya bersama konsultan.

Kalau Anda masih menyimpan data pengeluaran dalam Excel dengan kategori yang tumbuh liar, saran saya bukan langsung beli software pajak. Mulai dari yang sederhana: rapikan kategorinya dulu. Karena sebaik apa pun tools-nya, laporan pajak yang baik dimulai dari data yang konsisten.

## FAQ

**Q: Apakah Hermes Agent bisa mengisi SPT Tahunan secara otomatis?**
A: Tidak — dan saya tidak menyarankan itu. Agent saya pakai untuk membersihkan, menormalkan, dan mengelompokkan data transaksi. Perhitungan pajak dan keputusan klaim biaya tetap dilakukan konsultan pajak, karena butuh konteks dan bukti yang tidak dimiliki sistem otomatis.

**Q: Kategori expense apa yang penting untuk SPT orang pribadi dengan usaha?**
A: Secara umum: biaya usaha yang berkaitan dengan penghasilan (bahan baku, operasional, transportasi, sewa, marketing, gaji) dan pisahkan tegas dari pengeluaran pribadi. Detail aturannya ada di UU PPh dan dijelaskan di [pajak.go.id](https://www.pajak.go.id/index.php/en/node/86805) — konsisten sejak awal lebih mudah daripada merapikan di akhir.

**Q: Berapa lama waktu menyiapkan data SPT dengan Hermes Agent?**
A: Untuk kasus saya: 322 transaksi, sekitar 90 menit untuk pembersihan data, plus satu jam review bersama konsultan. Jauh lebih cepat dari 3–4 hari manual, tapi tetap butuh verifikasi manusia di akhir.

---

Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.
