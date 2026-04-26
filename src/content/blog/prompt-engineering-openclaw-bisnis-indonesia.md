---
title: "Prompt Engineering untuk OpenClaw: Template yang Sudah Terbukti Ampuh untuk Bisnis Indonesia"
description: "Tingkatkan performa OpenClaw AI agent dengan prompt engineering yang tepat. Ini template prompt yang sudah teruji di bisnis nyata -- auto-reply, rekomendasi produk, dan eskalasi keluhan pelanggan."
pubDate: 2026-04-27
heroImage: ../../assets/hero-prompt-engineering-openclaw.jpg
tags: ["OpenClaw", "prompt engineering", "AI agent", "otomatisasi bisnis", "UKM Indonesia"]
---

# Prompt Engineering untuk OpenClaw: Template yang Sudah Terbukti Ampuh untuk Bisnis Indonesia

Kalau kamu sudah pakai OpenClaw tapi hasilnya nggak sesuai ekspektasi -- kemungkinan besar bukan tools-nya yang bermasalah, tapi prompt-nya yang kurang pas.

Prompt engineering itu ibarat memberikan instruksi ke karyawan baru. Semakin jelas dan detail instruksinya, semakin bagus juga hasilnya. Ini berlaku juga buat AI agent seperti OpenClaw.

Artikel ini kasih template prompt yang sudah terbukti efektif di bisnis-bisnis kecil dan menengah di Indonesia.

## Kenapa Prompt Penting untuk OpenClaw?

Bedakan dulu antara OpenClaw dan chatbot template tradisional. Chatbot template cuma matching kata kunci lalu kirim jawaban yang sudah disetting sebelumnya. OpenClaw itu berbeda -- dia menggunakan model bahasa besar (LLM) yang bisa memahami konteks dan menghasilkan respons secara dinamis.

Tapi kemampuan itu cuma keluar kalau promt-nya juga dirancang dengan baik. Prompt yang buruk akan menghasilkan respons yang generic, nggak nyambung, atau bahkan salah informasi.

Ini yang sering saya lihat: bisnis baru install OpenClaw, langsung dipakai tanpa optimasi, terus kecewa karena hasilnya "kurang smart". Padahal yang perlu di-tune justru promt-nya, bukan tools-nya.

## Template 1: Customer Service Persona

Ini template paling dasar dan paling penting. Pakai ini sebagai fondasi system prompt kamu.

```
Kamu adalah asisten layanan pelanggan untuk [NAMA TOKO], sebuah toko [jenis produk] online di Indonesia. 

Aturan main:
- Selalu jawab dengan ramah, Gunakan bahasa Indonesia yang santai tapi tetap profesional
- Tanyakan nama pelanggan di awal percakapan untuk personalize respons
- Selalu sertakan harga dan ketersediaan stok saat ditanya produk
- Kalau pelanggan inquire tentang promo atau diskon, sebutkan promo yang sedang berlaku
- Kalau ada perubahan harga atau stok mendadak, kasih tahu pelanggan dan sarankan alternatif

Contoh respons:
Pelanggan: "Baju雷电 S navy ada ga?"
Kamu: "Hai! Baju雷电 S navy ready banget nih. Harga Rp125.000. Mau dipesenin? 」
```

Template ini membuat AI punya personality yang konsisten dan memahami konteks bisnis kamu.

## Template 2: Handling Objections

Setiap bisnis pasti menghadapi pelanggan yang ragu. Gunakan template ini supaya AI bisa handle objections dengan baik.

```
Kamu sedang berbicara dengan pelanggan yang terlihat ragu. 

Strategi penanganan:
1. Akui keraguan mereka dengan empati
2. Berikan bukti sosial atau fakta konkret
3. Tawarkan solusi atau alternatif
4. Jangan terlalu "jual" -- biarkan pelanggan memutuskan sendiri

Contoh handle objection "Harga terlalu mahal":
"Oke banget kalau kamu merasa harganya agak tinggi. Jujur, kami sudah bandingkan dengan produk sejenis dan kualitas bahan yang kami pake memang di atas standar. Kita juga ada cicilan 0% lewat SeaBank kalau mau. Mau aku bantu hitung angsuran per bulannya? "
```

Hal yang perlu dihindari: jangan langsung bilang "tapi kualitas kami bagus kok" tanpa ada bukti. Berikan angka, fakta, atau testimoni konkret.

## Template 3: Eskalasi ke Admin Manusia

Bagian ini sering dilupakan padahal krusial. AI nggak selalu bisa handle semua situasi. Template ini memastikan pelanggan tidak "hilang" ketika situasinya rumit.

```
Kondisi yang WAJIB kamu eskalasikan ke admin manusia:
- Komplain atau keluhan serius (barang rusak, pengiriman salah, refund)
- Permintaan khusus yang di luar SOP (custom order, harga khusus untuk pembelian besar)
- Masalah pembayaran yang perlu diverifikasi
- Keluhan yang mengandung emosi tinggi atau tidak nyaman

Cara eskalasi:
1. Minta maaf atas ketidaknyamanan yang dialami
2. Jelaskan bahwa kamu akan meneruskan ke tim yang lebih tepat
3. Berikan estimasi waktu respons (maksimum 1 jam di jam kerja)
4. Kirim pesan ke webhook dengan format: {phone, name, message, priority: "high"}

Contoh:
"Mohon maaf ya kak, untuk kasus ini saya rasa lebih tepat kalau ditanganin langsung sama tim kami yang bisa cek orderan secara langsung. Nanti dalam 30 menit ada tim CS kami yang akan hubungi kakak. Terima kasih atas pengertiannya! "
```

Tanpa template eskalasi yang jelas, pelanggan bisa kecewa karena masalah mereka nggak terselesaikan. Eskalasi yang cepat dan sopan justru meningkatkan trust pelanggan.

## Template 4: Product Recommendation Engine

Template ini berguna untuk bisnis e-commerce yang ingin AI membantu rekomendasi produk berdasarkan preferensi pelanggan.

```
Kamu adalah konsultan produk untuk [NAMA TOKO]. 

Proses rekomendasi:
1. Tanyakan preferensi pelanggan (budget, ukuran, warna, kebutuhan spesifik)
2. Cek ketersediaan produk yang match
3. Berikan maksimal 3 rekomendasi dengan alasan singkat
4. Tutup dengan tanya apakah mau langsung pesan

Format rekomendasi:
[Nama Produk] - Rp[Harga]
Alasan: [kenapa produk ini cocok untuk kebutuhan pelanggan tadi]
Stok: [tersedia / terbatas / pre-order]

Contoh:
"Nah untuk budget 200rb, aku rekomendasi:
1. Baju雷电 Flanel Premium -- Rp175.000. Bahannya adem, cocok buat daily use. Stok ready.
2. Jaket Windbreaker Urban -- Rp195.000. Tahan angin, cocok buat yang sering luar kota. Stok 3 pcs terakhir.

Kangen lanjut atau ada preferensi lain? "
```

Template ini mengubah cara AI dari sekadar menjawab pertanyaan jadi benar-benar membantu keputusan pembelian.

## Template 5: After-Sales & Follow-Up

Ini template yang sering dilupakan tapi punya dampak besar untuk repeat order. Pakai setelah transaksi selesai.

```
Kamu adalah tim follow-up pelanggan [NAMA TOKO].

Tujuan: memastikan pelanggan puas dengan pembeliannya dan membuka kesempatan repeat order.

Pesan follow-up (kirim 3 hari setelah pengiriman):
"Hai [Nama]! Ini dari [NAMA TOKO]. Pesanan kakak sudah dikonfirmasi sampai ya. 

Boleh banget aku tanya:
1. Produknya sesuai ekspektasi ga?
2. Ada yang perlu kami bantu atau ada keluhan?
3. Kalau puas, kami lagi ada promo [PROMO NAME] buat pembelian berikutnya -- [DETAIL PROMO]

Senang bisa bantu kakak! "

Pesan follow-up (kirim 7 hari setelah pengiriman):
"Hai [Nama]! Gimana kabarnya? Semoga produknya cocok dan dipakai dengan bahagia ya. 

BTW, kita baru masukin koleksi [NEW CATEGORY] nih. Kadang pelanggan kita yang juga suka [produk yang dibeli pelanggan] langsung suka ini juga. Sekadar info aja, ga maks kok! "
```

Follow-up yang personal meningkatkan kemungkinan repeat order secara signifikan. Data dari Shopify menyebutkan bahwa pelanggan yang menerima follow-up message punya 65% kemungkinan lebih tinggi untuk repeat order dibanding yang tidak.

## Cara Testing Prompt

Setelah menulis prompt, jangan langsung déploy ke production. Lakukan testing sistematis:

**Round 1: Basic conversation test**
Kirim berbagai tipe pesan umum -- pertanyaan produk, tanya harga, minta rekomendasi. Cek apakah respons sesuai ekspektasi.

**Round 2: Edge case test**
Kirim pesan yang provokatif, typo, bahasa gaul, atau campur Inggris-Indonesia. Lihat apakah AI tetap handle dengan baik.

**Round 3: Escalation test**
Kirim pesan yang seharusnya trigger eskalasi. Cek apakah sistem benar-benar eskalasi ke admin.

Dari testing ini, kamu akan menemukan bagian prompt yang perlu diperbaiki. Prompt engineering itu proses iteratif -- terus refine sampai benar-benar smooth.

## Checklist Sebelum Publishing

Pastikan sebelum launch, semua ini sudah dicek:

- [ ] System prompt mencakup nama brand, tone, dan SOP yang jelas
- [ ] Aturan eskalasi sudah terdefinisi dan fungsional
- [ ] AI bisa handle "no match" situations dengan graceful fallback
- [ ] Minimum 20 sample conversations sudah di-test
- [ ] Log percakapan aktif untuk review mingguan
- [ ] Admin tahu prosedur handle eskalasi dari OpenClaw

## FAQ

**Apakah prompt harus dalam Bahasa Indonesia?**
Tidak harus. Model LLM modern seperti GPT-4o atau Claude Haiku sudah cukup baik dalam Bahasa Indonesia casual. Tapi untuk istilah bisnis khusus (nama produk, brand voice), pakai Bahasa Indonesia lebih konsisten.

**Berapa kali harus update prompt?**
Minimal review setiap minggu di bulan pertama. Kalau sudah stabil, monthly review sudah cukup. Update juga saat ada perubahan produk, promo, atau SOP bisnis.

**Apakah bisa pakai beberapa template sekaligus?**
Bisa. Combine template yang relevant untuk use case kamu. Contoh: customer service persona + objection handling + eskalasi. Semakin kompleks promt-nya, semakin penting juga testing yang thorough.

**Bagaimana kalau respons AI masih terlalu formal atau kaku?**
Tambahkan instruksi tentang "tone" di prompt. Contoh: "Selalu pakai bahasa yang santai, kayak ngobrol sama temen. Gunakan emoji yang tepat tapi jangan berlebihan. Jangan pernah memulai kalimat dengan 'Perlu saya informasikan...'"

## Penutup

Prompt engineering adalah competitive advantage nyata buat bisnis yang pakai AI agent. Tools yang sama, dipakai oleh dua bisnis berbeda, akan menghasilkan output yang sangat berbeda kalau prompt-nya berbeda.

Jadi sebelum bilang "AI ini kurang smart", coba cek dulu: apakah promt-nya sudah dioptimalkan?

Kirim percakapan sample kamu di kolom komentar -- siapa tahu bisa kasih input untuk improve promt-nya. Atau kalau butuh bantuan setup dan optimize OpenClaw dari awal, reach out aja lewat DM Instagram @maswahyuu.

---

*Artikel oleh Mas Wahyu, founder Qawwa Technology Indonesia. Fokus di digital marketing dan AI automation untuk UKM Indonesia.*
