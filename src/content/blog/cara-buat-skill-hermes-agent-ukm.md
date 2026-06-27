---
title: "Cara Buat Skill Hermes Agent untuk Otomatisasi Tugas UKM Tanpa Coding"
description: "Panduan praktis membuat skill Hermes Agent khusus untuk UKM. Otomatiskan tugas berulang tanpa perlu keahlian coding — cukup tulis instruksi dalam Bahasa Indonesia."
pubDate: 2026-06-28
heroImage: "../../assets/hero-cara-buat-skill-hermes-agent-ukm.jpg"
---

# Cara Buat Skill Hermes Agent Sendiri untuk Otomatisasi Tugas UKM

Punya Hermes Agent tapi cuma dipakai buat nanya-nanya doang? Sayang banget. Fitur paling powerful dari Hermes Agent justru **skill system** — kemampuan bikin asisten virtual khusus yang hafal SOP bisnis kamu dan bisa ngerjain tugas berulang secara otomatis.

Mulai dari menulis balasan komplain pelanggan, ngecek stok barang tiap pagi, sampai bikin laporan penjualan — semua bisa kamu jadwalkan sebagai skill. Dan kabar baiknya: **kamu nggak perlu bisa coding.**

## Apa Itu Skill di Hermes Agent?

Skill adalah paket instruksi yang kamu kasih ke Hermes Agent. Mirip kayak ngasih briefing ke staff baru — kamu jelasin:

- **Kapan** skill ini harus jalan (trigger)
- **Apa yang harus dilakukan** (instructions)
- **Hasil seperti apa yang kamu mau** (output format)

Bedanya, staff baru kamu adalah AI yang kerja 24/7, nggak pernah ngeluh, dan inget detail sekecil apapun.

## Kenapa UKM Butuh Custom Skill?

Skill bawaan (built-in) Hermes Agent udah lumayan, tapi kekuatan sesungguhnya ada di **skill yang kamu bikin sendiri**. Kenapa?

1. **SOP bisnis kamu unik** — Cara kamu nanganin komplain beda sama cara toko sebelah
2. **Nggak perlu gaji bulanan** — Sekali bikin, kerja terus tanpa biaya tambahan
3. **Konsisten** — Skill ngikutin format dan standar yang kamu tentukan, 100% setiap saat
4. **Skalabel** — Punya 3 toko atau 30 toko? Skill Hermes Agent jalan sama aja

## Panduan Praktis: Bikin Skill Pertama Kamu

### Langkah 1: Buka File Manager Skill

Hermes Agent punya direktori khusus buat nyimpen skill. Caranya:

```bash
cd ~/.hermes/skills/
mkdir skill-cek-stok-harian
cd skill-cek-stok-harian
```

Buat folder baru dengan nama skill kamu. Urusannya cuma file teks.

### Langkah 2: Tulis File SKILL.md

Ini inti dari skill — file instruksi yang dibaca Hermes Agent. Formatnya simpel. Contoh skill untuk ngecek stok barang:

```markdown
---
name: cek-stok-harian
description: Cek stok produk dari spreadsheet dan kirim notifikasi kalau stok mau habis
---

# Skill: Cek Stok Harian

## Trigger
Setiap hari jam 08:00 pagi.

## Steps
1. Baca file stok terbaru di folder Google Drive "Operasional"
2. Cari produk dengan stok di bawah 10 unit
3. Buat daftar: Nama Produk, Stok Tersisa, Supplier
4. Kirim ringkasan ke WhatsApp owner
5. Kalau ada stok di bawah 3 unit, tandai dengan label "URGEN"
```

### Langkah 3: Daftarkan ke Hermes

Buka file konfigurasi Hermes Agent dan tambahkan baris ini:

```yaml
skills:
  - name: cek-stok-harian
    path: ~/.hermes/skills/cek-stok-harian/SKILL.md
```

Simpan. Selesai. Hermes Agent otomatis tahu ada skill baru.

### Langkah 4: Tes Skill Kamu

Minta Hermes Agent jalankan skillnya:

> "Hermes, jalankan skill cek stok harian"

Lihat outputnya. Kalau ada yang kurang pas, tinggal edit file SKILL.md lagi. Nggak perlu install ulang atau restart apapun.

## Contoh Skill UKM Lain yang Langsung Berguna

Ini beberapa skill yang udah saya bikin dan terbukti jalan di lapangan:

### 1. Skill Balas Komplain Otomatis

Trigger komplain masuk, AI nulis draft balasan sesuai tone brand kamu. Kamu tinggal review dan kirim. Hemat 10-15 menit per komplain.

### 2. Skill Jadwal Konten Medsos

Setiap Senin jam 09:00, Hermes buatin draft postingan Instagram, TikTok, dan Facebook untuk seminggu ke depan. Tinggal tambahin foto atau video.

### 3. Skill Rekap Penjualan Harian

Tiap malam jam 21:00, skill ini ambil data dari marketplace, rangkum: total penjualan, produk terlaris, komplain masuk. Langsung dikirim ke grup WhatsApp owner.

### 4. Skill Monitoring Kompetitor

Mingguan, skill ini cek harga kompetitor buat 5 produk sejenis. Hasilnya: tabel perbandingan harga + rekomendasi. Nggak perlu stalking manual.

## Hal yang Perlu Diperhatikan

1. **Mulai dari yang kecil.** Skill sederhana dulu — 3-4 langkah. Jangan langsung bikin skill kompleks yang 20 langkah. Bikin frustrasi.

2. **Instruksi harus konkret.** Jangan "analisa pasar". Tapi "bandingkan harga produk A, B, C di Tokopedia dan Shopee, lalu buat tabel perbandingan".

3. **Tes di jam sepi.** Waktu tes awal, pilih jam sibuk yang low impact. Biar nggak ganggu operasional kalau hasilnya kacau.

4. **Iterasi.** Skill pertama kamu mungkin nggak sempurna. Edit, tes, edit lagi. Semakin detail instruksinya, semakin presisi hasilnya.

## Kapan Waktu yang Tepat untuk Upgrade?

Kalau bisnis kamu udah punya 3-4 skill dan mulai kerasa dampaknya — stok nggak pernah telat di-restock, komplain nggak ada yang kelewat, laporan harian datang otomatis — saatnya naik level.

Pertimbangkan untuk:
- Integrasi skill dengan API marketplace (Tokopedia, Shopee)
- Bikin skill multi-langkah yang saling trigger
- Gabungin skill jadi workflow otomatis penuh

## Kesimpulan

Kekuatan Hermes Agent bukan cuma soal teknologi canggih — tapi soal **kemampuan adaptasi** ke kebutuhan spesifik bisnis kamu. Skill system bikin AI yang tadinya alat tanya-jawab berubah jadi **asisten operasional** yang kerja 24/7.

Kalau kamu bisa ngejelasin SOP ke staff baru, kamu bisa bikin skill Hermes Agent. Mulai hari ini dari satu skill sederhana dan lihat bedanya dalam seminggu.

**Pertanyaan: Apakah skill Hermes Agent bisa dipakai tanpa koneksi internet?**
**Jawaban:** Hermes Agent perlu koneksi internet untuk mengakses model AI. Tapi setelah skill terdaftar, instruksinya tersimpan lokal di folder skill kamu.

**Pertanyaan: Berapa biaya tambahan untuk bikin skill sendiri?**
**Jawaban:** Nol rupiah. Bikin skill itu cuma nulis file teks. Biaya cuma untuk akses API model AI yang mungkin kamu pakai — itu pun biasanya di bawah 100 ribu per bulan untuk pemakaian UKM kecil.

**Pertanyaan: Apa aman menyimpan data bisnis di skill Hermes Agent?**
**Jawaban:** File skill disimpan di komputer/server lokal kamu sendiri. Kalau pake cloud, pastikan pilih provider yang trusted. Hindari menuliskan password atau API key langsung di file skill — gunakan environment variable.

**Pertanyaan: Berapa banyak skill yang bisa dibuat?**
**Jawaban:** Sebanyak yang kamu mau. Setiap skill file kecil (biasanya 1-5 KB), jadi ribuan skill pun nggak masalah.
