# Discord Bot Google Sheets - Railway Free Hosting

Bot Discord yang menyimpan data registrasi ke Google Sheets dengan hosting gratis di Railway.app

## Fitur

- **Command !daftar**: Menyimpan data registrasi user ke Google Sheets
- **Command !help**: Menampilkan panduan penggunaan
- **Command !check**: Mengecek koneksi ke database Google Sheets
- **Validasi Input**: Memastikan semua field terisi lengkap
- **Error Handling**: Pesan error yang jelas dan membantu

## Requirements

- Akun Discord
- Akun Google
- Akun GitHub
- Akun Railway.app (gratis)

## Setup Guide

### Step 1: Buat Google Sheet

1. Buka [Google Sheets](https://sheets.google.com)
2. Buat Sheet baru
3. Isi baris pertama (header) dengan kolom berikut:

```
Username Roblox | Nama Panggilan | Jenis Kelamin | Domisili | Tanggal Lahir | Device yang Digunakan | Social Media
```

4. Rename file menjadi: **Database Discord** (atau nama lain sesuai keinginan)
5. Copy **Spreadsheet ID** dari URL (bagian antara `/d/` dan `/edit`)

   Contoh URL: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit`

### Step 2: Enable Google Sheets API

1. Masuk ke [Google Cloud Console](https://console.cloud.google.com/)
2. Klik **"Select a project"** → **"New Project"**
3. Beri nama project (contoh: "Discord Bot") → **Create**
4. Pastikan project yang baru dibuat sudah terpilih

#### Aktifkan API:

5. Di menu kiri, pilih **"APIs & Services"** → **"Library"**
6. Cari dan aktifkan:
   - **Google Sheets API** (klik Enable)
   - **Google Drive API** (klik Enable)

#### Buat Service Account:

7. Di menu kiri, pilih **"APIs & Services"** → **"Credentials"**
8. Klik **"Create Credentials"** → **"Service Account"**
9. Isi Service Account name (contoh: "discord-bot") → **Create and Continue**
10. Skip optional steps → **Done**

#### Download Credentials:

11. Klik pada Service Account yang baru dibuat
12. Pergi ke tab **"Keys"**
13. Klik **"Add Key"** → **"Create new key"**
14. Pilih **JSON** → **Create**
15. File `credentials.json` akan terdownload

#### Share Google Sheet:

16. Buka file `credentials.json` yang baru didownload
17. Cari dan copy nilai `client_email` (format: `name@project.iam.gserviceaccount.com`)
18. Buka Google Sheet yang dibuat di Step 1
19. Klik tombol **Share** (pojok kanan atas)
20. Paste email service account tadi
21. Pastikan permission-nya **"Editor"**
22. **Uncheck** "Notify people" → **Share**

### Step 3: Buat Discord Bot

1. Masuk ke [Discord Developer Portal](https://discord.com/developers/applications)
2. Klik **"New Application"**
3. Beri nama aplikasi → **Create**
4. Masuk ke menu **"Bot"** (sidebar kiri)
5. Klik **"Add Bot"** → **"Yes, do it!"**
6. **COPY TOKEN** (klik "Reset Token" jika perlu, lalu copy)

   ⚠️ **PENTING**: Simpan token ini dengan aman! Jangan share ke siapapun!

#### Aktifkan Intents:

7. Scroll ke bawah ke bagian **"Privileged Gateway Intents"**
8. Aktifkan **"Message Content Intent"**
9. Klik **Save Changes**

#### Invite Bot ke Server:

10. Masuk ke menu **"OAuth2"** → **"URL Generator"**
11. Pilih scope: **bot**
12. Pilih bot permissions:
    - Send Messages
    - Read Messages/View Channels
    - Read Message History
13. Copy **Generated URL** di bagian bawah
14. Paste URL tersebut di browser
15. Pilih server yang ingin ditambahkan bot
16. **Authorize**

### Step 4: Setup Project Locally (Testing)

#### Clone atau Download Repository

```bash
# Clone repository (jika sudah di GitHub)
git clone <your-repo-url>
cd discord-bot-sheets

# Atau download dan extract ZIP
```

#### Install Dependencies

```bash
# Pastikan Python 3.8+ sudah terinstall
python --version

# Install dependencies
pip install -r requirements.txt
```

#### Setup Credentials

1. Copy file `credentials.json` yang didownload dari Google Cloud ke folder project
2. Buat file `.env` di folder project:

```env
TOKEN=paste_discord_bot_token_disini
SHEET_NAME=Database Discord
```

⚠️ Ganti `paste_discord_bot_token_disini` dengan token Discord bot Anda!

#### Test Bot Locally

```bash
python bot.py
```

Jika berhasil, akan muncul:
```
Successfully connected to Google Sheet: Database Discord
Bot logged in as YourBotName#1234
Connected to 1 server(s)
Ready to receive commands!
```

Test di Discord dengan command `!help`

### Step 5: Upload ke GitHub

#### Buat Repository

1. Masuk ke [GitHub](https://github.com)
2. Klik **"New repository"**
3. Beri nama repository (contoh: "discord-bot-sheets")
4. Pilih **Public** atau **Private**
5. **JANGAN** centang "Initialize with README"
6. **Create repository**

#### Push Code

```bash
# Initialize git (jika belum)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Add remote
git remote add origin https://github.com/username/discord-bot-sheets.git

# Push
git branch -M main
git push -u origin main
```

⚠️ **PENTING**: Pastikan `.gitignore` sudah ada sebelum commit agar credentials tidak terupload!

### Step 6: Deploy ke Railway

1. Masuk ke [Railway.app](https://railway.app/)
2. Login dengan GitHub
3. Klik **"New Project"**
4. Pilih **"Deploy from GitHub repo"**
5. Pilih repository **discord-bot-sheets** Anda
6. Railway akan mulai deploy otomatis

#### Set Environment Variables:

7. Setelah deploy selesai, klik project Anda
8. Pilih service yang baru dibuat
9. Klik tab **"Variables"**
10. Tambahkan variabel berikut:

```
TOKEN = your_discord_bot_token_here
SHEET_NAME = Database Discord
```

⚠️ Ganti `your_discord_bot_token_here` dengan token Discord bot Anda!

#### Upload credentials.json:

11. Karena Railway tidak bisa baca file lokal, ada 2 cara:
    - **Cara 1 (Recommended)**: Convert `credentials.json` ke environment variable
    - **Cara 2**: Commit `credentials.json` ke **private repository** (⚠️ hanya jika repo private!)

**Untuk Cara 1 (Convert ke ENV):**
Buka `credentials.json`, copy semua isinya, dan buat variable baru di Railway:
```
GOOGLE_CREDENTIALS = {paste semua isi credentials.json}
```

Lalu update `bot.py` untuk membaca dari environment variable (lihat catatan di bagian bawah).

#### Redeploy:

12. Klik **"Deploy"** atau push perubahan baru ke GitHub
13. Railway akan otomatis redeploy

#### Check Logs:

14. Klik tab **"Logs"** untuk melihat apakah bot berhasil running
15. Pastikan muncul pesan: "Bot logged in as..."

## Penggunaan

### Command: !daftar

Digunakan untuk mendaftar dan menyimpan data ke Google Sheets.

**Format:**
```
!daftar
Username Roblox : NacthXen
Nama Panggilan : xeno
Jenis Kelamin : cowo
Domisili : batam
Tanggal Lahir : 20 Agustus 2006
Device yang Digunakan : Hp
Social Media : ig : takt
```

**Field yang Wajib Diisi:**
1. Username Roblox
2. Nama Panggilan
3. Jenis Kelamin
4. Domisili
5. Tanggal Lahir
6. Device yang Digunakan
7. Social Media

### Command: !help

Menampilkan panduan penggunaan bot.

```
!help
```

### Command: !check

Mengecek koneksi bot ke Google Sheets.

```
!check
```

## Troubleshooting

### Bot Offline di Railway

**Cek:**
1. Logs di Railway → apakah ada error?
2. Environment variables → sudah benar semua?
3. Credits Railway → masih ada saldo?

### Error: "Spreadsheet not found"

**Solusi:**
1. Cek nama sheet di environment variable `SHEET_NAME`
2. Pastikan Google Sheet sudah di-share ke service account email
3. Pastikan service account punya akses **Editor**

### Error: "credentials.json not found"

**Solusi:**
1. Pastikan file `credentials.json` ada di folder project
2. Atau convert ke environment variable (lihat Step 6)

### Bot tidak merespon command

**Cek:**
1. Apakah bot sudah join server?
2. Apakah **Message Content Intent** sudah diaktifkan?
3. Apakah bot punya permission **Send Messages**?

### Data tidak masuk ke Google Sheets

**Cek:**
1. Format command → apakah sesuai contoh?
2. Semua 7 field sudah diisi?
3. Koneksi Google Sheets → test dengan `!check`

## Catatan Penting

- **credentials.json** dan **.env** TIDAK boleh diupload ke GitHub public!
- Simpan Discord token dengan aman
- Railway free tier punya batasan:
  - $5 credit/bulan
  - Sleeping mode jika tidak ada aktivitas
  - Bisa di-upgrade jika perlu 24/7 uptime

## Alternative: Credentials as Environment Variable

Jika Anda tidak ingin commit `credentials.json`, ubah kode di `bot.py`:

```python
import json

# Add after imports
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS")

# In init_sheets function, replace:
# creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)

# With:
if GOOGLE_CREDENTIALS_JSON:
    creds_dict = json.loads(GOOGLE_CREDENTIALS_JSON)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
else:
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
```

Lalu tambahkan variable `GOOGLE_CREDENTIALS` di Railway dengan isi dari `credentials.json`.

## Support

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

## License

MIT License - Free to use and modify.
# discord-bot-sheets
# discord-bot-sheets
