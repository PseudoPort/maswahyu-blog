---
title: "Harga Sales Tidak Konsisten? AI Bikin Patokan Harga B2B Otomatis untuk Tim Sales UKM"
description: "Harga grosir UKM tidak konsisten antar sales? AI bisa jadi patokan harga B2B otomatis — solusi praktis tanpa bikin repot tim sales."
pubDate: "2026-07-14"
heroImage: "../../assets/hero-ai-automation-untuk-ukm.jpg"
---

Anda punya 3 sales. Tiap sales punya cara sendiri ngasih harga ke customer grosir. Sales A ngasih diskon 15% langsung tanpa tanya. Sales B selalu pake harga katalog — pelanggan kabur karena mahal. Sales C nego kasih harga beda-beda tiap hari. Customer yang sama — PT Makmur Jaya — minggu lalu ditawari Rp 85.000 per unit sama Sales A, minggu ini Rp 72.000 sama Sales B. Pelanggan telepon komplain: "Kok harga saya beda? Yang benar yang mana?"

Situasi ini bukan cerita langka. Ini kejadian nyata setiap hari di UKM Indonesia yang punya tim sales lebih dari satu orang. Masalahnya: **tidak ada patokan harga yang jelas, konsisten, dan mudah diakses semua sales.**

---

## Kenapa Harga Sales Tidak Konsisten Itu Mahal

Dampak dari pricing yang kacau balau ini lebih besar dari yang kelihatan:

**1. Kredibilitas hancur di depan customer.** Customer B2B biasanya beli dalam jumlah besar dan jangka panjang. Kalau mereka tahu harga Anda tidak konsisten, mereka akan main-main — tawar lebih rendah terus, karena tahu ada sales lain yang bisa kasih harga lebih murah.

**2. Margin terkikis tanpa sadar.** Tanpa patokan, sales yang "baik hati" bisa kasih diskon sampai 30% padahal margin cuma 25%. Artinya? Jual rugi, dan Anda baru tahu pas laporan akhir bulan.

**3. Sales senior bisa seenaknya.** Tanpa sistem, sales yang paling lama biasanya yang paling berkuasa soal harga. Ini bikin budaya tidak sehat — sales baru minder, sales lama semena-mena.

**4. Waktu terbuang untuk approval manual.** Setiap kali sales dapat order, Anda harus cek WA: "Harga ini oke nggak?", balas, bolak-balik. Kalau sehari 10 order approval, itu bisa makan 1-2 jam waktu Anda.

---

## Ide AI Automation: Patokan Harga Otomatis + Approval Workflow

Solusi AI di sini bukan mengganti sales. Tapi kasih mereka patokan yang jelas, konsisten, dan bisa diakses kapan pun — lewat WhatsApp atau dashboard sederhana.

### Cara kerjanya:

1. **Input data master harga.** Anda masukin daftar harga per produk, beserta tier (misal: tier A = 1-50 pcs, tier B = 51-200 pcs, tier C = 200+ pcs), dan diskon maksimal per tier.

2. **AI jadi "price calculator" untuk sales.** Sales kirim chat ke WhatsApp bot atau buka dashboard: "Customer A minta 100 unit produk X." AI langsung hitung harga berdasarkan tier B, plus diskon maksimal yang diizinkan.

3. **Otomatis catat tiap quote.** Semua penawaran yang keluar tersimpan. Nanti Anda tinggal lihat: siapa sales yang sering kasih diskon maksimal, customer mana yang dapat harga khusus, dan tren margin per bulan.

4. **Approval hanya untuk yang di luar batas.** Kalau sales mau kasih diskon di luar patokan — misal 30% padahal maksimal 20% — otomatis minta approval ke Anda lewat notifikasi. Sisanya? Jalan sendiri.

---

## Data & Input yang Dibutuhkan

Supaya sistem ini jalan, Anda perlu nyiapin data ini dulu:

| Data | Contoh | Catatan |
|------|--------|---------|
| Daftar produk + HPP (Harga Pokok) | Produk A: Rp 50.000, Produk B: Rp 120.000 | Wajib update tiap kali supplier naikkan harga |
| Tier harga per jumlah | 1-50 pcs: Rp 75.000, 51-200: Rp 68.000, 200+: Rp 62.000 | Bisa beda per produk |
| Diskon maksimal per tier | Tier A: 10%, Tier B: 15%, Tier C: 20% | Ini penting buat jaga margin |
| Daftar customer dan riwayat pembelian | PT Makmur: tier B, beli tiap bulan | Biar AI bisa kasih rekomendasi yang relevan |
| Aturan khusus (kalau ada) | "Customer X diskon 5% extra karena lama" | Input manual, sekali set |

Kalau data di atas belum rapi, jangan khawatir. Mulai aja dari produk yang paling laku dan 5-10 customer terbesar. Nanti bisa ditambah bertahap.

---

## Workflow Sederhana (Step by Step)

**Step 1 — Sales dapat permintaan harga dari customer.**
Sales A: "Pak, PT Makmur minta 150 unit Produk A, boleh diskon berapa?"

**Step 2 — Sales buka WhatsApp bot / dashboard, masukkan info.**
Bot balas otomatis: "Produk A — Tier B (51-200 pcs) — Harga satuan Rp 68.000. Diskon maksimal 15%. Harga final: Rp 57.800/unit. Total: Rp 8.670.000."
Sales tinggal screenshot dan kirim ke customer. Selesai dalam 30 detik.

**Step 3 — Kalau sales butuh diskon di luar patokan.**
Sales A: "Customer minta diskon 20%."
Bot: "Diskon 20% melebihi batas 15%. Minta approval ke atasan."
Notifikasi masuk ke WhatsApp/email Anda: "Sales A minta diskon 20% untuk PT Makmur, 150 unit Produk A. Setujui / Tolak?"
Anda tap setuju atau tolak. Selesai.

**Step 4 — Semua tercatat otomatis.**
Di akhir minggu, AI kirim laporan: total penawaran, rata-rata diskon yang dikasih, penawaran yang deal, customer yang paling sering dapat diskon besar.

---

## Kapan Perlu Human Approval

AI otomatis untuk perhitungan harga itu aman-aman saja. Tapi ada beberapa situasi yang tetap perlu campur tangan manusia:

- **Diskon melebihi batas.** Kalau sales minta diskon di luar tier yang sudah ditetapkan, jangan otomatis. Minta approval.
- **Customer baru, belum ada riwayat.** AI bisa kasih harga default, tapi Anda mungkin mau kasih harga khusus untuk menjaring customer besar. Putuskan sendiri.
- **Bundling produk.** Kalau customer minta paket bundling (Produk A + B + C), AI mungkin belum cukup pintar ngitung margin gabungan. Better Anda cek dulu.
- **Pembayaran tempo.** Kalau ada unsur piutang (bayar belakangan), approval manual tetap perlu — risiko gagal bayar harus dipertimbangkan.

**Prinsipnya:** biarkan AI mengurusi 80% kasus yang rutin. Simpan energi Anda untuk 20% keputusan strategis.

---

## Metrik Sukses

Bukan cuma "AI berjalan" — tapi bagaimana dampaknya ke bisnis:

| Metrik | Sebelum AI | Target setelah AI |
|--------|-----------|-------------------|
| Waktu sales bikin quote per customer | 10-20 menit | < 1 menit |
| Waktu approval Anda per hari | 1-2 jam | < 15 menit |
| Variasi harga untuk customer yang sama | Sering beda | 0% — konsisten |
| Margin rata-rata per transaksi | Tergantung sales | Stabil di target |
| Komplain customer soal harga | Sering | Jarang |

---

## Checklist Implementasi 7 Hari

Hari 1: **Kumpulkan data master.** Ambil daftar produk, HPP, dan tier harga. Rapikan di spreadsheet.
Hari 2: **Tetapkan aturan diskon.** Berapa persen maksimal per tier. Catat juga customer spesial.
Hari 3: **Setup WhatsApp bot.** Bisa pakai tools seperti Twilio, WATI, atau bot sederhana. (Atau integrasi dengan Hermes Agent / AI assistant Anda.)
Hari 4: **Input data ke sistem.** Masukin produk, tier, aturan diskon.
Hari 5: **Tes dengan 1 sales.** Coba 5-10 skenario — minta sales kasih quote pake sistem baru. Cek akurasi.
Hari 6: **Training tim sales.** Kasih tahu cara pakai, jelaskan kenapa ini bikin hidup mereka lebih mudah. (Bukan buat ngontrol, tapi buat bantu mereka kerja lebih cepat.)
Hari 7: **Go live.** Pantau 2-3 hari pertama. Perbaiki aturan kalau ada yang janggal.

---

**Intinya:** masalah harga sales tidak konsisten bukan karena sales Anda nakal atau pelanggan Anda sulit. Masalahnya ada di sistem. Dengan AI untuk patokan harga, Anda bisa menghilangkan variabel, menjaga margin, dan bikin sales Anda — baru maupun lama — bekerja dengan standar yang sama. Tim sales jadi lebih percaya diri, customer puas, dan Anda tidak perlu jadi wasit harga tiap hari. Semua beres sebelum jam makan siang.
