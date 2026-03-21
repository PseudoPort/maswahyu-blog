---
title: 'Cara Install Hermes Agent di Laptop: Panduan Lengkap dari Nol'
description: 'Panduan cara install Hermes Agent di laptop Linux, macOS, dan WSL2. Satu baris perintah sampai siap pakai. Termasuk troubleshooting.'
pubDate: 2026-03-21
heroImage: ../../assets/hero-install-hermes.jpg
---

Pernah dengar soal AI agent yang bisa belajar dari kesalahan sendiri? Itu Hermes Agent. Dan kabar baiknya, install-nya gampang banget.

Artikel ini panduan lengkap dari nol sampai Hermes Agent siap dipakai. Termasuk cara install manual kalau mau kontrol penuh, plus troubleshooting untuk masalah umum.

## Kenapa Harus Hermes Agent?

Sebelum masuk ke cara install, penting tahu kenapa Hermes Agent layak dicoba.

Banyak AI agent framework bertebaran. Ada AutoGen dari Microsoft, CrewAI, LangChain Agents, dan lain-lain. Tapi kebanyakan punya keterbatasan yang bikin frustasi.

AutoGen cuma jalan di Python. CrewAI tidak punya integrasi messaging. LangChain Agents tidak bisa belajar dari interaksi sebelumnya. Hermes Agent menjawab semua masalah itu.

Fitur unggulan yang bikin Hermes Agent menonjol:

- **Self-improving learning loop**: Agent makin cerdas tiap kali berinteraksi. Dia simpan pembelajaran dan terapkan di tugas berikutnya.
- **Cross-platform messaging**: Bisa kirim dan terima perintah lewat Telegram, WhatsApp, Discord, dan Slack. Tidak perlu buka terminal setiap saat.
- **Multi-provider support**: Tidak terikat satu provider. Bisa pakai Nous Portal, OpenRouter dengan 200+ model, OpenAI, Anthropic, atau bahkan model lokal.
- **Open-source MIT**: Gratis untuk proyek pribadi maupun komersial. Tidak ada vendor lock-in.

## Apa Itu Hermes Agent?

Hermes Agent adalah open-source AI agent framework dari Nous Research. Beda sama agent lain yang cuma jalan sekali lalu lupa, Hermes punya mekanisme *self-improving learning loop*. Artinya dia makin pintar seiring pemakaian.

Sekarang sudah 9.500+ bintang di GitHub dan ribuan fork. Lisensinya MIT, jadi aman buat proyek komersial.

Yang bikin beda dari kompetitor:

- **vs AutoGen**: Hermes multi-bahasa, bukan Python-only
- **vs CrewAI**: Ada integrasi messaging (Telegram, WhatsApp, Discord, Slack)
- **vs LangChain Agents**: Punya sistem pembelajaran sendiri yang terus berkembang

## Sebelum Mulai: Cek Dulu Persyaratannya

| Komponen | Keterangan |
|----------|-----------|
| OS | Linux, macOS, atau WSL2 |
| Git | Wajib terinstall |
| Python | Opsional (otomatis ditangani uv) |
| Windows native | Belum didukung, pakai WSL2 |

Kalau kamu pakai Windows, jangan panik. Cukup install WSL2 dulu, lalu ikuti langkah-langkah di bawah dari terminal WSL.

## Cara Install Hermes Agent (Metode Cepat)

Ini cara paling gampang. Cuma satu baris perintah:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Tunggu sampai selesai. Script ini akan otomatis:

1. Meng-clone repositori
2. Menginstall uv (package manager Python yang super cepat)
3. Membuat virtual environment
4. Menginstall semua dependensi

Kalau ada error "command not found: curl", install dulu:

- Ubuntu/Debian: `sudo apt install curl`
- macOS: curl sudah bawaan, tidak perlu install
- Fedora: `sudo dnf install curl`

## Cara Install Manual (Kalau Mau Kontrol Penuh)

Kadang kita butuh kontrol lebih. Misalnya mau custom lokasi instalasi atau pakai Python versi tertentu. Ikuti langkah-langkah berikut.

**Langkah 1: Clone repositori**

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
```

**Langkah 2: Install uv**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

uv itu pengganti pip yang jauh lebih cepat. Kalau sudah ada, skip langkah ini.

**Langkah 3: Buat virtual environment**

```bash
uv venv --python 3.11
source .venv/bin/activate
```

Pakai Python 3.11 karena paling stabil untuk Hermes Agent saat ini.

**Langkah 4: Install dependensi**

```bash
uv pip install -e ".[all]"
```

Flag `-e` artinya *editable mode*. Kalau kamu mau ikut kontribusi kode, ini penting supaya perubahan langsung terasa tanpa install ulang.

## Setup Awal Setelah Install

Install selesai, sekarang konfigurasi. Jalankan wizard interaktif:

```bash
hermes setup
```

Wizard ini akan menanyakan beberapa hal:

- **Provider AI**: Mau pakai Nous Portal, OpenRouter, OpenAI, atau Anthropic?
- **API Key**: Kunci akses ke provider pilihanmu
- **Platform messaging**: Mau terhubung ke Telegram, WhatsApp, Discord, atau Slack?

Saya sarankan mulai dengan Nous Portal atau OpenRouter. Dua-duanya mendukung 200+ model, jadi fleksibel kalau mau ganti-ganti model nanti.

Kalau belum punya API key, tenang. Nous Portal punya free tier untuk percobaan. Cukup daftar di portal.nousresearch.com, buat API key, dan masukkan saat setup.

## Verifikasi Instalasi

Cek apakah semuanya sudah benar:

```bash
hermes --version
```

Kalau muncul versi, selamat. Hermes Agent sudah siap dipakai.

## FAQ

**Bisakah install Hermes Agent di Windows tanpa WSL?**

Belum bisa. Hermes Agent belum mendukung Windows native. Solusinya install WSL2 dulu, lalu ikuti panduan install di atas dari terminal WSL.

**Berapa ukuran instalasi Hermes Agent?**

Sekitar 200-300MB termasuk dependensi Python. Tidak berat untuk ukuran laptop modern.

**Apakah butuh GPU?**

Tidak. Hermes Agent sendiri ringan. Yang butuh GPU adalah model AI yang kamu pakai, tapi kalau pakai API provider (seperti OpenRouter), semua komputasi di server mereka.

**Bisa pakai model AI lokal?**

Bisa. Hermes Agent mendukung koneksi ke endpoint lokal seperti Ollama atau LM Studio. Cukup set URL endpoint saat setup.

**Bagaimana cara update Hermes Agent?**

```bash
cd hermes-agent
git pull
uv pip install -e ".[all]"
```

Atau kalau install pakai script satu baris, jalankan ulang perintah curl yang sama.

**Error "Permission denied" saat install?**

Cek apakah kamu punya izin tulis di direktori. Kalau install di `/usr/local`, mungkin perlu `sudo`. Tapi sebaiknya install di home directory saja supaya tidak perlu sudo.

## Troubleshooting Umum

**"hermes: command not found" setelah install**

Pastikan virtual environment sudah aktif. Coba jalankan:

```bash
source ~/.hermes/.venv/bin/activate
hermes --version
```

Kalau masih error, tambahkan path ke `~/.bashrc` atau `~/.zshrc`:

```bash
export PATH="$HOME/.hermes/.venv/bin:$PATH"
```

**"Module not found" saat menjalankan hermes**

Dependensi mungkin belum terinstall sempurna. Jalankan ulang:

```bash
cd hermes-agent
uv pip install -e ".[all]" --force-reinstall
```

**Build gagal karena versi Python salah**

Hermes Agent butuh Python 3.10 atau 3.11. Cek versi kamu:

```bash
python3 --version
```

Kalau versinya salah, install Python 3.11:

- Ubuntu: `sudo apt install python3.11`
- macOS: `brew install python@3.11`

## Cara Pakai Hermes Agent Setelah Install

Install selesai, konfigurasi beres. Sekarang saatnya coba perintah pertama.

Jalankan agent dari terminal:

```bash
hermes run
```

Atau kalau mau langsung kirim tugas spesifik:

```bash
hermes ask "Ringkas email terbaru saya dan buat daftar tugas"
```

## Langkah Selanjutnya

Hermes Agent sudah terinstall. Sekarang waktunya eksplorasi:

- Coba kirim perintah pertama lewat CLI atau messaging platform
- Eksplorasi learning loop dengan memberikan feedback ke agent
- Hubungkan ke Telegram atau WhatsApp untuk automasi harian
- Baca dokumentasi resmi di GitHub untuk fitur lanjutan

Komunitas Hermes Agent aktif di GitHub Discussions. Kalau ada kendala atau ide fitur baru, langsung post di sana. Developer Nous Research cukup responsif.
