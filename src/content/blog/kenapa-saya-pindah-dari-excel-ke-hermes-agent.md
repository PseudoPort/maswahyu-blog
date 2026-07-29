---
title: "Kenapa Saya Pindah dari Excel ke Hermes Agent untuk Tracking Expense Pribadi"
description: "Frustrasi dengan Excel yang error-prone dan tidak konsisten? Saya sudah 6 bulan pakai Hermes Agent untuk automate expense tracking. Ini hasilnya."
pubDate: 2026-07-29
heroImage: "../../assets/hero-expense-tracking-automation.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Kenapa Saya Pindah dari Excel ke Hermes Agent untuk Tracking Expense Pribadi

Januari 2026. Saya buka file Excel "Expense_2025_final_FINAL_v3.xlsx" — dan langsung merasa lelah.

300+ baris transaksi. Setengahnya belum dikategorikan. Ada duplikat yang gak ketahuan sampai laporan bulanan. Rumus SUM yang jebol gara-gara saya insert row sembarangan. Dan yang paling menyebalkan: **saya harus manual input setiap transaksi.**

Beli kopi Rp 25.000 di Starbucks → buka laptop → buka Excel → ketik tanggal → ketik nominal → pilih kategori → save. Kalau lupa input 2-3 hari, chaos. Struk udah ilang, lupa nominalnya, tebak-tebakan kategorinya "Food & Beverage" atau "Meeting Expense".

Saya founder tech company yang ngomong automation ke klien setiap hari. Tapi expense tracking pribadi? Masih pakai Excel kayak tahun 2010.

**Ironi-nya menyakitkan.**

## Problem dengan Excel (dan Kenapa Saya Tahan 3 Tahun)

Excel bukan tools jelek. Tapi untuk expense tracking pribadi yang konsisten, ini bottleneck-nya:

**1. Manual data entry = guaranteed inconsistency**

Setiap transaksi butuh 5-7 langkah manual. Kalau busy, skip. Kalau males, skip. Hasilnya: data expense saya punya gap 2-3 minggu setiap bulannya.

**2. No automation = time sink**

Rata-rata 20-30 transaksi per minggu. 5 menit per transaksi (buka Excel, input, categorize, save). **2.5 jam per minggu hilang cuma untuk data entry.**

Per tahun: **130 jam.** Setara 16 hari kerja full.

**3. Error-prone & no validation**

Typo nominal? Salah kategori? Duplikat entry? Excel tidak akan kasih tahu. Baru ketahuan pas laporan bulanan — dan saat itu udah terlambat untuk fix.

**4. Zero insight**

Excel cuma simpan data. Mau tahu spending pattern? Bikin pivot table manual. Mau alert kalau over budget? Gak ada. Mau forecast spending bulan depan based on trend? Coding sendiri.

Kenapa saya tahan 3 tahun? **Karena gak ada alternatif yang pas.**

Apps expense tracking di Play Store/App Store terlalu general. Butuh internet. Data di server mereka (privacy risk). Dan mayoritas berbayar dengan fitur yang saya gak butuh.

Saya mau:
- **Local-first** — data di laptop saya, bukan cloud
- **Automation-friendly** — bisa integrate sama workflow lain
- **Customizable** — bisa tambah logic sendiri
- **Free & open-source** — no subscription bullshit

Sampai saya ketemu **Hermes Agent.**

## Hermes Agent: AI Assistant yang Bisa Diajarin

Hermes Agent bukan expense tracker. Dia AI assistant open-source dengan persistent memory dan skill system.

Artinya: saya bisa **ajarin** dia untuk jadi expense tracker pribadi saya.

Cara kerjanya simpel:

1. Saya foto struk → kirim ke Telegram bot
2. Bot forward ke Hermes Agent
3. Hermes extract data dari foto (OCR)
4. Auto-categorize based on merchant
5. Save ke database lokal (SQLite)
6. Sync ke Google Sheets (backup)
7. Kirim konfirmasi ke Telegram

**Total waktu: 10 detik. Tanpa buka laptop.**

Setup awal butuh 2-3 jam. Tapi setelah jalan, expense tracking jadi **zero-friction.**

## 6 Bulan Pakai Hermes Agent: Hasilnya

Sekarang Juli 2026. 6 bulan full pakai Hermes Agent untuk expense tracking:

### Time Saved

- **Sebelum (Excel):** 2.5 jam/minggu = 130 jam/tahun
- **Sesudah (Hermes):** 15 menit/minggu = 13 jam/tahun (cuma buat review laporan bulanan)
- **Net saved:** 117 jam/tahun

117 jam = **14.6 hari kerja.** Itu 3 minggu produktif yang balik.

### Data Accuracy

- **Sebelum (Excel):** ~70% transaksi tercatat (sisanya lupa input)
- **Sesudah (Hermes):** 95%+ transaksi tercatat (yang 5% lupa foto struk)
- **Improvement:** 25% lebih complete

### Budget Compliance

Januari-Juni 2026, saya set budget Rp 15 juta/bulan untuk personal expense.

- **Januari-Maret (pakai Excel):** Over budget 2 dari 3 bulan. Average overspend Rp 2.1 juta.
- **April-Juni (pakai Hermes):** On budget 3 dari 3 bulan. Average underspend Rp 800k.

**Kenapa?** Karena Hermes kirim alert real-time kalau spending mendekati budget. Behaviour change.

### Spending Insights

Hermes Agent auto-generate spending report setiap akhir bulan. Beberapa insight:

- **40% expense saya di "Food & Beverage"** — mostly kopi dan makan siang meeting. Saya gak sadar sampai lihat chart.
- **Transport expense naik 60% setiap awal bulan** — karena jadwal meeting klien lebih padat week pertama.
- **Subscription digital (SaaS tools) menggerogoti Rp 1.2 juta/bulan** — banyak yang gak kepake tapi lupa cancel.

Data ini **tidak akan pernah muncul di Excel** kecuali saya manual bikin analisis. Dengan Hermes, otomatis.

## Biaya Real Setup Hermes Agent

**Hardware:** Laptop/PC yang udah ada (Ubuntu 22.04, 8GB RAM cukup)

**Software:**
- Hermes Agent: Free (open-source MIT)
- PostgreSQL: Free
- Telegram Bot API: Free
- Google Sheets API: Free
- OCR engine (Tesseract): Free

**Total biaya bulanan: Rp 0.**

Compare dengan expense tracker app berbayar:
- Money Lover Pro: Rp 59k/bulan
- Wallet by BudgetBakers: $4.99/bulan (~Rp 80k)
- YNAB: $14.99/bulan (~Rp 240k)

**ROI in 0 months.** Langsung untung.

## Lesson Learned

**1. Automation bukan tentang tools — tentang behaviour change**

Excel gagal bukan karena fiturnya kurang. Gagal karena **saya harus ingat untuk buka dan input manual.** Hermes berhasil karena workflow-nya frictionless: foto struk → done.

**2. Local-first > Cloud-first untuk data sensitif**

Expense data itu super personal. Knowing spending pattern = knowing lifestyle. Saya lebih nyaman data disimpan lokal di laptop saya, bukan di server startup Silicon Valley yang bisa jual data ke advertiser.

**3. Open-source = future-proof**

Kalau Money Lover shutdown besok, data saya stuck di app mereka. Kalau Hermes development berhenti, source code tetap ada — saya bisa maintain sendiri atau hire developer.

**4. Small automation compounds**

10 detik saved per transaksi terdengar kecil. Tapi × 20 transaksi/minggu × 52 minggu = 173 menit/tahun saved. Dan itu baru satu workflow. Kalau 10 workflow di-automate? **28 jam/tahun saved.**

## Next Step: Setup Hermes Agent untuk Expense Tracking

Artikel ini cuma cerita kenapa saya pindah. **Tutorial step-by-step setup-nya ada di artikel berikutnya:**

1. Install Hermes Agent di Ubuntu
2. Setup Telegram Bot untuk input expense
3. Integrasi OCR untuk receipt scanning
4. Auto-categorization dengan machine learning
5. Sync ke Google Sheets untuk backup
6. Dashboard analytics dengan Plotly

Kalau kamu stuck dengan Excel dan pengen pindah ke automation — tunggu artikel selanjutnya.

**Update 30 Juli 2026:** Tutorial lengkap setup sudah publish. [Link akan ditambahkan setelah artikel kedua live]

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 29 Juli 2026.*

## Referensi

- [Hermes Agent Official Documentation](https://hermes-agent.nousresearch.com/docs/) — Source code, installation guide, dan API reference
- [Indonesia Expense Management Software Market Analysis 2026-2035](https://www.nextmsc.com/report/indonesia-expense-management-software-market-ic4868) — Market trends expense tracking Indonesia
