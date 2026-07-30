---
title: "Hermes Agent Jadi Executive Assistant Saya: Meeting Notes, Action Items, Follow-up Otomatis"
description: "Setelah expense tracking beres, saya extend Hermes Agent jadi asisten rapat. Voice note → transkrip → action items dikirim ke Telegram dalam 2 menit."
pubDate: 2026-07-31
heroImage: "../../assets/hero-hermes-agent-meeting-notes.jpg"
author: Mas Wahyu
authorTitle: Founder & CEO Qawwa Technology Indonesia
---

# Hermes Agent Jadi Executive Assistant Saya: Meeting Notes, Action Items, Follow-up Otomatis

Maret 2026, selesai meeting dengan klien potensial. Saya tutup laptop, ambil napas, dan sadar: **saya lupa 3 poin penting yang dibahas 20 menit lalu.**

Bukan karena gak konsentrasi. Tapi karena dalam 60 menit meeting, saya harus: dengerin klien, mikirin solusi, lihat slide mereka, dan catat poin penting. Multitasking? Gak ada yang namanya multitasking — yang ada adalah task-switching, dan tiap switch ada biaya atensinya.

Saya coba berbagai solusi sebelum bikin sendiri:

- **Otter.ai** — bagus transkripsinya, tapi data di cloud mereka, pricing $16.99/bulan
- **Notion AI** — oke, tapi harus copy-paste hasilnya manual
- **Google Docs voice typing** — akurat, tapi gak ada action item extraction

Semuanya partial solution. Yang saya mau: kirim voice note → dapat transkrip + action items → auto-terkirim ke tim. **Semua lokal, tanpa subscription.**

Solusinya? Hermes Agent yang saya extend.

## Arsitektur: Voice Note ke Action Items dalam 3 Langkah

### Langkah 1: Voice Note via Telegram

Flow-nya sederhana. Abis meeting, saya buka Telegram, kirim voice note:

> *"Meeting dengan klien Toko Buku Online pukul 14.00-15.00. Poin utama: mereka mau integrasi WhatsApp Payment, target launching minggu ketiga Agustus. Tim teknis butuh akses API Midtrans. Harga Paket Pro Rp 4.5 juta/tahun, deal closing 2 minggu. Action: saya kirim draft kontrak Jumat ini. Tim teknis: siapkan environment testing untuk integrasi WhatsApp."*

Total: **47 detik rekaman.**

### Langkah 2: Hermes Agent → Transkrip → Structured Notes

Setelah voice note terkirim, Hermes Agent:

1. Download audio dari Telegram
2. Transkrip via Whisper (local, open-source)
3. Parse transkrip → extract: meeting title, timestamp, peserta, keputusan, action items, deadlines
4. Simpan ke database lokal

**Output dalam 2 menit:**

```
## Meeting Notes — Toko Buku Online
📅 31 Juli 2026, 14:00-15:00
👤 Client: Toko Buku Online

### Keputusan
- Integrasi WhatsApp Payment via Midtrans API
- Target launching: minggu ketiga Agustus
- Harga Paket Pro: Rp 4.500.000/tahun

### Action Items
1. 🔴 [Mas Wahyu] Kirim draft kontrak — deadline: Jumat ini
2. 🟡 [Tim Teknis] Siapkan environment testing WhatsApp API — deadline: 5 Agustus
3. 🟢 [Tim CS] Siapkan dokumentasi fitting untuk klien — deadline: 7 Agustus
```

Warna merah/kuning/hijau saya tambahkan belakangan: **priority tag otomatis** berdasarkan deadline dan dampak.

### Langkah 3: Auto-Distribute ke Tim

Setiap action item langsung dikirim ke Telegram group masing-masing tim:

- **#tim-teknis:** "Environment testing WhatsApp API — deadline 5 Agustus. Detail: [link ke notes]"
- **saya pribadi:** "Draft kontrak Toko Buku Online — deadline Jumat"

**Yang penting:** ini bukan cuma notifikasi satu arah. Tim bisa reply ke Telegram bot untuk update status: `done`, `blocked`, `revised deadline`. Status auto-update di database.

## Hasil Setelah 4 Bulan

Saya mulai pakai sistem ini April 2026. Sekarang Juli. Beberapa data:

### Meeting Coverage

| Metrik | Sebelum (Q1 2026) | Sesudah (Q2 2026) |
|--------|-------------------|-------------------|
| Meeting dengan notes terdokumentasi | ~40% | 95% |
| Action items yang ditindaklanjuti | ~55% | 88% |
| Follow-up manual per minggu | 2-3 jam | 15 menit |
| Missed deadline akibar lupa | 4-5/bulan | 0-1/bulan |

**Sumber data:** Saya audit semua meeting notes dan action items dari Q1 vs Q2 untuk laporan internal Qawwa. Perbedaannya signifikan — terutama di follow-up rate yang naik 33%.

### Daya Ingat yang Gak Perlu Diandalkan

Sebelumnya, saya andalkan otak untuk ingat action items meeting. Hasilnya? **Ada jeda 12-48 jam** antara meeting dan action benar-benar dikerjakan — karena harus nunggu saya ingat, buka notes, trus delegasi.

Sekarang, tim udah terima action items dalam 5 menit setelah meeting selesai. **Eksekusi mulai lebih cepat.**

### Biaya

- **Whisper (local):** Gratis, open-source
- **Telegram Bot:** Gratis
- **Hermes Agent:** Udah terinstall dari project expense tracking sebelumnya

**Tambahan modal:** Rp 0

## Yang Saya Pelajari

**Pertama, voice note itu format paling efficient.** Ngetik 150 kata butuh 1-2 menit. Ngomong 150 kata butuh 30 detik. Voice note juga capture tone dan konteks yang hilang di teks. Saya bisa bilang "deadline Jumat ini **penting banget**" — tekanan di suara saya jadi sinyal buat prioritas.

**Kedua, struktur data yang rigid justru bikin orang males.** Awalnya saya bikin form template buat meeting notes: kolom peserta, agenda, durasi, budget, dll. Hasilnya? Gak dipake. Terlalu ribet. Solusi: voice note bebas → Hermes yang structur-in. **Zero friction di input, maximum structure di output.**

**Ketiga, auto-distribusi action items mengubah budaya tim.** Sebelumnya, saya adalah single point of failure untuk delegasi. Kalau saya lupa, tim gak gerak. Sekarang, action items langsung sampe ke mereka tanpa lewat saya. **Tim jadi lebih proaktif — mereka mulai nanya "status action item A gimana?" duluan sebelum saya tanya.**

## Next Steps

Sekarang saya lagi develop fitur **daily standup briefing** — setiap jam 08.00, Hermes Agent kirim ringkasan ke Telegram group: action items yang pending, deadline hari ini, dan agenda meeting. Tujuannya: pagi hari tim gak perlu nunggu saya untuk tahu apa yang harus dikerjakan.

**Update:** sistem ini sudah capture 340+ action items dari 87 meeting sejak April. Dari jumlah itu, 300 selesai tepat waktu — **88% completion rate.** Sebelumnya? Saya gak punya data karena gak tercatat.

---

*Ditulis oleh **Mas Wahyu** — Founder & CEO Qawwa Technology Indonesia. 16+ tahun di industri teknologi, kini fokus membantu UKM Indonesia bertransformasi digital dengan AI & automation.*

*Artikel ini pertama kali dipublikasikan: 31 Juli 2026.*

## Referensi

- [Hermes Agent Documentation — Skill System](https://hermes-agent.nousresearch.com/docs/core-concepts/skills) — Cara membuat dan mengintegrasikan skill kustom untuk workflow automation
- [OpenAI Whisper](https://github.com/openai/whisper) — Open-source speech recognition engine yang digunakan untuk transkripsi voice note
