---
title: "Kas Kecil Kantor: Workflow Hermes Agent yang Akhirnya Bikin Buku Kas Beres"
description: "Kas kecil kantor selisih Rp 237 ribu sebulan. Workflow Hermes Agent ini bikin buku kas beres: catat lewat Telegram, rekap otomatis, laporan bulanan tanpa rekap manual."
pubDate: 2026-08-19
heroImage: "../../assets/hero-hermes-agent-kas-kecil-otomatis.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Kas Kecil Kantor: Workflow Hermes Agent yang Akhirnya Bikin Buku Kas Beres

Mei 2026, saya minta rekap kas kecil ke tim operasional. Jawabannya: "Sebentar ya, Mas, saya hitung dulu." Dua hari kemudian baru datang, dalam bentuk foto buku tulis yang di-scan pakai HP. Selisihnya Rp 237.000. Bukan uang yang bikin perusahaan kolaps, tapi cukup bikin saya bertanya: kenapa uang paling kecil di kantor ini justru paling sulit dilacak?

Bulan itu saya putuskan kas kecil jadi proyek kecil-kecilan: bikin workflow pencatatan yang tidak bergantung pada ingatan siapa pun.

## Kenapa Kas Kecil Selalu Berantakan

Kas kecil di kantor kami waktu itu pegangannya sederhana: Rp 1,5 juta per bulan, dipegang tim operasional, dipakai buat beli pulsa kantor, bensin antar dokumen, kopi tamu, dan perbaikan kecil. Totalnya sekitar 47 transaksi sebulan, melibatkan 6 orang yang kadang belanja pakai uang mereka sendiri dulu baru minta ganti.

Masalahnya bukan di orangnya. Masalahnya di alurnya: nota disimpan di dompet masing-masing, dicatat ke buku tulis "nanti", dan rekap dilakukan kalau uangnya sudah mau habis. Nota hilang, nominal dilupakan, dan yang tercatat hanya yang sempat ditulis. Pada akhir bulan, selisih itu hal normal — bukan pencurian, hanya kebocoran pencatatan.

Ini pola yang umum. [Investopedia](https://www.investopedia.com/terms/p/pettycash.asp) menyebut kas kecil butuh prosedur dan kontrol yang jelas: siapa pemegangnya, berapa plafonnya, dan bagaimana setiap pengeluaran didokumentasikan. Tanpa itu, rekonsiliasi selalu jadi permainan tebak-tebakan.

## Workflow yang Saya Pasang

Saya tidak mengganti kebiasaan orang — saya mengganti media catatannya. Semua transaksi kas kecil sekarang masuk lewat bot Telegram yang saya bangun di atas Hermes Agent. Alurnya:

1. **Catat di tempat.** Siapa pun yang keluar uang kirim pesan ke bot: "bensin 50 ribu" atau "pulsa kantor 100 ribu". Lima detik, selesai. Tidak perlu buka spreadsheet.
2. **Kategori dipilih otomatis.** Agent menebak kategori dari kata kunci — bensin masuk Transport, pulsa masuk Komunikasi. Kalau salah, tinggal balas "kategori: lainnya".
3. **Foto nota opsional.** Untuk transaksi di atas Rp 100 ribu, nota difoto dan dilampirkan. Untuk yang di bawah itu, cukup pesan teks. Ini kompromi yang realistis — kalau semua transaksi wajib foto, workflow-nya mati di minggu pertama.
4. **Saldo dihitung otomatis.** Setiap transaksi masuk, bot menjawab sisa saldo: "Saldo kas kecil: Rp 412.000". Orang jadi tahu kapan harus minta isi ulang, tanpa nanya ke pemegang kas.
5. **Rekap mingguan.** Tiap Senin pagi, agent kirim ringkasan: 12 transaksi, Rp 380 ribu keluar, saldo tersisa. Pemegang kas tinggal mencocokkan dengan uang fisik di dompet.
6. **Tutup buku bulanan.** Tanggal 1, laporan lengkap per kategori dikirim ke email — siap untuk dimasukkan ke pembukuan.

Setup-nya sekitar 3 jam: bikin bot, definisikan kategori, pasang aturan alert. Tidak ada yang perlu dipelajari anggota tim — mereka cuma perlu tahu satu perintah: kirim pesan ke bot.

## Angka Setelah Tiga Bulan

Saya audit di awal Agustus. Dari Juni sampai Juli, 143 transaksi tercatat lewat bot. Rekap yang tadinya butuh 2 hari kerja (dan sering telat) sekarang keluar otomatis tiap Senin pagi; cek fisiknya cukup 15 menit.

Selisih bulanan turun drastis: dari Rp 237.000 di bulan pertama ke Rp 12.000 di bulan kedua, dan nol di bulan ketiga. Sisa Rp 12.000 itu pun bukan hilang — cuma pembulatan di kasir. Semua transaksi punya jejak: siapa, kapan, untuk apa.

Yang menarik: jumlah transaksi yang tercatat justru naik. Sebelumnya sekitar 47 transaksi per bulan yang tercatat, sekarang 55-60. Bukan berarti orang jadi lebih boros — artinya pengeluaran yang dulu lolos dari catatan sekarang kelihatan. Ini sejalan dengan data soal manual data entry: [riset](https://www.lido.app/blog/data-entry-error-rates) menunjukkan error rate pencatatan manual 1-4% per entri, dan itu terjadi persis di pekerjaan paling membosankan. Di kas kecil, "error" itu bentuknya bukan typo, tapi transaksi yang tidak pernah tercatat sama sekali.

## Pelajaran yang Saya Bawa

Kas kecil bukan masalah teknologi. Dia masalah disiplin, dan teknologi hanya bisa membantu kalau alurnya dibuat semudah mungkin untuk diikuti. Orang tidak malas mencatat — mereka malas membuka Excel. Ketika mencatat cukup lewat chat, disiplin datang dengan sendirinya.

Satu hal yang saya pertahankan: ada manusia yang tetap memegang uang fisik dan mencocokkan saldo setiap minggu. Hermes Agent tidak menggantikan pemegang kas — dia menghapus pekerjaan rekap yang selama ini makan waktu dua hari. Orang-orang jadi fokus ke hal yang butuh keputusan manusia: apakah pengeluaran ini wajar, dan kenapa minggu ini bensin lebih boros dari biasanya.

## FAQ

**Q: Berapa plafon kas kecil yang ideal?**
A: Tergantung pola pengeluaran. Saya pakai acuan dua minggu operasional — kalau rata-rata keluar Rp 700 ribu per minggu, plafon Rp 1,5 juta cukup realistis. Plafon terlalu kecil bikin orang sering minta isi ulang, terlalu besar bikin kontrol longgar.

**Q: Apakah perlu aplikasi akuntansi khusus untuk ini?**
A: Tidak. Untuk UKM, bot chat + database sederhana sudah jauh lebih baik daripada buku tulis. Yang penting setiap transaksi tercatat saat terjadi, bukan saat diingat. Aplikasi akuntansi baru relevan kalau volume transaksinya sudah puluhan per hari.

**Q: Gimana kalau ada anggota tim yang tetap lupa catat?**
A: Itu tetap terjadi, tapi dampaknya beda. Dulu satu transaksi tidak tercatat = hilang permanen. Sekarang rekap mingguan langsung menunjukkan selisih, dan orang bisa diingatkan saat itu juga — bukan tiga minggu kemudian saat uangnya sudah tidak ketahuan ke mana.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*
