---
title: "Setup Hermes Agent untuk Expense Tracking Otomatis: Dari Struk Foto ke Laporan Bulanan"
description: "Tutorial step-by-step setup Hermes Agent untuk expense tracking pribadi. Dari installasi Ubuntu, integrasi Telegram Bot, OCR receipt scanning, sampai auto-categorization dan budget alert."
pubDate: 2026-07-30
heroImage: "../../assets/hero-setup-hermes-agent-expense-tracking.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Setup Hermes Agent untuk Expense Tracking Otomatis: Dari Struk Foto ke Laporan Bulanan

Di artikel sebelumnya saya cerita kenapa akhirnya pindah dari Excel ke Hermes Agent setelah 3 tahun bertahan. Artikel ini adalah janji saya waktu itu: **tutorial lengkap setup-nya.**

Januari 2026, malam minggu jam 22.30. Saya duduk di depan laptop, kopi hitam, dan tekad bulat: *besok gak mau lagi manual input expense.*

Waktu itu saya target: **2 jam setup, langsung live.** Realitanya? 3 jam — karena kena error database migration dan harus trial-error beberapa OCR setting. Tapi begitu jalan, expense tracking saya berubah total.

Ini step-by-step-nya.

## Step 1: Install Hermes Agent di Ubuntu

Saya pakai Ubuntu 22.04 LTS di laptop ThinkPad dengan RAM 8GB. Basic. Tidak perlu server khusus.

```bash
# Clone repo
git clone https://github.com/NousResearch/Hermes Agent.git
cd Hermes-Agent

# Setup Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
```

**Yang bikin saya stuck 30 menit:** Hermes butuh PostgreSQL sebagai memory backend. Saya pakai default SQLite dulu buat testing, tapi SQLite punya limitasi kalau session sudah banyak. **Rekomendasi saya: langsung pakai PostgreSQL dari awal.**

```bash
sudo apt install postgresql
sudo -u postgres createuser --interactive  # tambah user 'hermes'
sudo -u postgres createdb hermes_memory
```

Edit `.env`:

```
DATABASE_URL=postgresql://hermes:password@localhost:5432/hermes_memory
TELEGRAM_BOT_TOKEN=...ambil dari @BotFather...
```

Efek SQLite vs PostgreSQL langsung kerasa setelah 2 minggu. Hermes Agent punya persistent memory — setiap transaksi expense saya disimpan sebagai memory. SQLite mulai lambat di 500+ memory entries. PostgreSQL? No issue sampai 10.000+ entries bare metal.

## Step 2: Setup Telegram Bot untuk Input Expense

Ini yang bikin workflow jadi **frictionless.** Saya buat Telegram Bot via [@BotFather](https://t.me/BotFather) — gratis, 5 menit jadi.

Token dari BotFather langsung paste ke `.env`.

**Logika sederhananya:**

1. Saya kirim foto struk ke Telegram Bot
2. Hermes Agent detect attachment → download image
3. OCR pipeline jalan
4. Hasil parsing dikembalikan ke saya untuk konfirmasi
5. Saya reply "OK" → data masuk ke database
6. Kalau ada yang salah parsing, saya koreksi manual — **ini feedback loop penting buat improve accuracy.**

Di minggu pertama, OCR salah baca nominal struk sekitar 30% — terutama struk yang kusut, terkena air, atau font kecil. Saya kasih feedback manual, dan akurasinya naik ke 85%+ setelah 2 minggu.

**Praktis: total waktu dari foto struk sampai data tercatat = 8-12 detik.**

## Step 3: OCR Pipeline untuk Receipt Scanning

Hermes Agent bisa integrasi dengan beberapa OCR engine. Saya pake **Tesseract OCR** — gratis, open-source, akurasi decent.

```bash
sudo apt install tesseract-ocr tesseract-ocr-ind
```

Tambahkan preferensi language Indonesia supaya lebih akurat baca struk Indonesia yang campur Bahasa Inggris dan Indonesia.

**Catatan penting dari pengalaman:** Struk dari merchant besar (Indomaret, Alfamart, Starbucks, McD) hampir 95% akurat. Struk dari warung kecil atau parkir? **Turun ke 60%.** Font thermal yang luntur adalah musuh utama OCR.

Solusi saya: tambah preprocessing pipeline — konversi ke grayscale, thresholding, deskew. Sederhana tapi nambah akurasi 15%.

```python
# Preprocessing snippet yang saya tambahkan
import cv2
import numpy as np

def preprocess_receipt(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh
```

Angka 15% ini saya ukur dari 50 struk sample minggu pertama — dari baseline 70% naik ke 85% setelah preprocessing.

## Step 4: Auto-Categorization

Ini yang paling powerful. Setiap transaksi harus masuk kategori: Food & Beverage, Transport, Utility, Entertainment, Health, dll.

Saya buat simple ruleset based on merchant name:

```yaml
rules:
  - pattern: "starbucks|kopi|coffee"
    category: Food & Beverage
  - pattern: "grab|gojek|pertamina|bensin"
    category: Transport
  - pattern: "alfamart|indomaret"
    category: Groceries
  - pattern: "netflix|spotify|aws|digitalocean"
    category: Subscription Digital
```

**Dulu di Excel, kategorisasi manual makan 30 detik per transaksi.** Dengan ruleset, 0 detik. Tinggal review seminggu sekali — biasanya cuma perlu koreksi 3-4 transaksi dari 50.

**Kesalahan saya:** waktu awal saya bikin rules terlalu luas. "Beli beras di Alfamart" masuk kategori "Groceries" — padahal sebenernya "Household Supplies." Butuh 2 minggu dan 12 transaksi salah kategori sebelum saya refine jadi 2 tier: Groceries (makanan/minuman) dan Household (sabun, deterjen, dll).

## Step 5: Budget Alert & Reporting

Ini fitur yang bikin automation **berdampak ke behaviour.**

Hermes Agent bisa setup scheduled job — setiap akhir hari, dia hitung total spending hari ini dan bandingkan dengan pro-rata budget.

Kalau sudah 80% dari budget, dapat alert:

> "*Alert: Spending hari ini Rp 235,000. Sisa budget mingguan: Rp 1.2 juta (15 hari tersisa).*"

**Dampak real:** Di April 2026 (bulan pertama pakai sistem ini), saya over budget cuma sekali — karena alert muncul. Bandingkan dengan Januari-Maret pakai Excel yang over budget 2-3 kali per bulan.

Laporan bulanan auto-generated dalam format Markdown:

```
## Laporan Bulanan Juli 2026
- Total Spending: Rp 14.2 juta
- Budget: Rp 15 juta
- Sisa: Rp 800k ✅
- Top 3 Kategori: Food & Beverage (38%), Transport (22%), Subscription (18%)
- Insight: Subscription naik 15% karena langganan tools baru
```

Waktu pembuatan laporan: **5 detik** (eksekusi query + formatting). Bandingkan dengan Excel yang butuh 30 menit manual filter dan pivot table.

## Biaya dan Waktu Setup

| Item | Biaya | Waktu |
|------|-------|-------|
| VPS/Tempat hosting | Rp 0 (laptop sendiri) | — |
| Hermes Agent | Gratis (MIT License) | 30 menit install |
| PostgreSQL | Gratis | 15 menit setup |
| Telegram Bot | Gratis | 5 menit |
| Tesseract OCR | Gratis | 10 menit install |
| Ruleset & tuning | — | 1 jam (trial-error) |
| **Total** | **Rp 0** | **~2-3 jam** |

ROI? Langsung setelah setup selesai — setiap transaksi yang dulu butuh 5 menit sekarang 10 detik.

## Yang Pengen Saya Tahu dari Awal

Setelah 6 bulan pakai sistem ini, beberapa hal yang bakal saya lakukan beda kalau mulai dari awal:

1. **Gunakan PostgreSQL dari hari pertama.** SQLite oke buat testing, tapi migrasi data itu menyebalkan.
2. **Kumpulkan 50 struk sample dulu sebelum bikin rules kategori.** Saya bikin rules dari 10 struk pertama, ternyata gak representatif — 40% transaksi gak cocok sama kategori yang saya bikin.
3. **Jangan perfeksionis soal akurasi OCR.** 85% akurat itu cukup. 15% yang salah bisa dikoreksi pas review mingguan dalam 5 menit. Lebih baik data 85% akurat konsisten daripada 0% karena gak jadi jalan.

---

Sekarang Juli 2026, sistem ini sudah capture lebih dari 1.200 transaksi tanpa masalah. Expense tracking jadi *set and forget* — saya cuma review 15 menit seminggu.

**Artikel selanjutnya:** bagaimana saya extend Hermes Agent untuk workflow lain — termasuk receipt scanning untuk klien UKM dan automasi laporan keuangan bulanan tim.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 30 Juli 2026.*

## Referensi

- [Hermes Agent Official Documentation](https://hermes-agent.nousresearch.com/docs/) — Dokumentasi resmi Hermes Agent untuk setup dan konfigurasi
- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/tessdoc/) — Dokumentasi engine OCR open-source yang digunakan
- [BotFather — Telegram Bot API](https://core.telegram.org/bots/tutorial) — Tutorial resmi Telegram Bot untuk integrasi
