# Setup Guide - Step by Step

Panduan lengkap setup Discord Bot dengan Google Sheets dari awal sampai deploy.

---

## PART 1: Setup Google Sheets & API (15 menit)

### A. Buat Google Sheet

**1. Buka Google Sheets**
   - Buka https://sheets.google.com
   - Login dengan akun Google Anda

**2. Buat Sheet Baru**
   - Klik "+ Blank" untuk sheet kosong
   - Atau klik "Template gallery" lalu "Blank"

**3. Isi Header (Baris 1)**
   Copy paste baris ini ke Row 1:
   ```
   Username Roblox	Nama Panggilan	Jenis Kelamin	Domisili	Tanggal Lahir	Device yang Digunakan	Social Media
   ```

   Atau ketik manual di cell A1-G1:
   - A1: Username Roblox
   - B1: Nama Panggilan
   - C1: Jenis Kelamin
   - D1: Domisili
   - E1: Tanggal Lahir
   - F1: Device yang Digunakan
   - G1: Social Media

**4. Rename Sheet**
   - Klik "Untitled spreadsheet" di pojok kiri atas
   - Ganti nama jadi: **Data Member RTA**
   - Tekan Enter

**5. Copy Spreadsheet ID**
   - Lihat URL di address bar browser
   - Format: `https://docs.google.com/spreadsheets/d/XXXXX/edit`
   - Copy bagian `XXXXX` (antara `/d/` dan `/edit`)
   - Simpan ID ini (akan dipakai nanti)

✅ **Checkpoint**: Sheet sudah punya header di baris 1 dan sudah punya nama

---

### B. Setup Google Cloud Console

**1. Buka Google Cloud Console**
   - Buka https://console.cloud.google.com/
   - Login dengan akun Google yang sama

**2. Buat Project Baru**
   - Klik dropdown di pojok kiri atas (tulisan "Select a project")
   - Klik **"NEW PROJECT"** di pojok kanan atas popup
   - Project name: **Discord Bot** (atau nama lain terserah)
   - Location: No organization (biarkan default)
   - Klik **CREATE**
   - Tunggu 5-10 detik sampai project dibuat

**3. Pastikan Project Sudah Active**
   - Klik dropdown project lagi
   - Pastikan "Discord Bot" (atau nama Anda) sudah terpilih (ada checklist)

---

### C. Aktifkan Google Sheets API

**1. Buka Library**
   - Di sidebar kiri, cari **"APIs & Services"**
   - Klik **"Library"** atau **"Enabled APIs & services"** lalu klik **"+ ENABLE APIS AND SERVICES"**

**2. Enable Google Sheets API**
   - Di search box, ketik: **Google Sheets API**
   - Klik hasil pertama (Google Sheets API)
   - Klik tombol **ENABLE** (warna biru)
   - Tunggu sampai enabled

**3. Enable Google Drive API**
   - Klik **"APIs & Services"** → **"Library"** lagi
   - Di search box, ketik: **Google Drive API**
   - Klik hasil pertama (Google Drive API)
   - Klik tombol **ENABLE**
   - Tunggu sampai enabled

✅ **Checkpoint**: Kedua API sudah enabled (cek di "Enabled APIs & services")

---

### D. Buat Service Account & Download Credentials

**1. Buka Credentials**
   - Di sidebar kiri, klik **"APIs & Services"** → **"Credentials"**

**2. Create Service Account**
   - Klik tombol **"+ CREATE CREDENTIALS"** di atas
   - Pilih **"Service account"**

**3. Isi Detail Service Account**
   - Service account name: **discord-bot-sheets** (atau nama lain)
   - Service account ID: (otomatis terisi)
   - Description: (optional, boleh kosong)
   - Klik **CREATE AND CONTINUE**

**4. Grant Access (Skip)**
   - "Grant this service account access to project" → **Skip** / Klik **CONTINUE**

**5. Grant Users Access (Skip)**
   - "Grant users access to this service account" → **Skip** / Klik **DONE**

**6. Buka Service Account yang Baru Dibuat**
   - Anda akan kembali ke halaman Credentials
   - Scroll ke bawah ke bagian **"Service Accounts"**
   - Klik pada email service account yang baru dibuat
     (formatnya: `discord-bot-sheets@project-xxx.iam.gserviceaccount.com`)

**7. Buat Key untuk Service Account**
   - Klik tab **"KEYS"** di atas
   - Klik **"ADD KEY"** → **"Create new key"**
   - Pilih format **JSON**
   - Klik **CREATE**
   - File `credentials.json` akan otomatis terdownload ke komputer Anda

**8. Copy Email Service Account**
   - Masih di halaman yang sama
   - Copy email service account (yang panjang)
   - Formatnya: `discord-bot-sheets@project-xxxxx.iam.gserviceaccount.com`
   - **SIMPAN EMAIL INI** (akan dipakai di langkah selanjutnya)

✅ **Checkpoint**: File `credentials.json` sudah terdownload & email service account sudah dicopy

---

### E. Share Google Sheet ke Service Account

**1. Buka Google Sheet yang Tadi Dibuat**
   - Kembali ke Google Sheet "Data Member RTA"

**2. Klik Share**
   - Klik tombol **Share** di pojok kanan atas (warna biru/hijau)

**3. Add Service Account Email**
   - Di kolom "Add people and groups", paste email service account tadi
   - Contoh: `discord-bot-sheets@project-xxxxx.iam.gserviceaccount.com`

**4. Set Permission**
   - Pastikan dropdown di sebelah kanan menunjukkan **"Editor"**
   - **UNCHECK** / matikan "Notify people" (karena service account bukan orang)

**5. Share**
   - Klik **Share** atau **Send**
   - Jika muncul warning "This email is outside your organization", klik **Share anyway**

✅ **Checkpoint**: Service account sudah ada di daftar "People with access" dengan role Editor

---

## PART 2: Setup Discord Bot (10 menit)

### A. Buat Discord Application

**1. Buka Discord Developer Portal**
   - Buka https://discord.com/developers/applications
   - Login dengan akun Discord Anda

**2. Create New Application**
   - Klik **"New Application"** di pojok kanan atas
   - Application name: **RTA Bot** (atau nama lain)
   - Centang "I agree to the Discord Developer Terms of Service"
   - Klik **Create**

---

### B. Setup Bot

**1. Buka Tab Bot**
   - Di sidebar kiri, klik **"Bot"**
   - Jika belum ada bot, klik **"Add Bot"** → **"Yes, do it!"**

**2. Customize Bot (Optional)**
   - USERNAME: Ganti nama bot jika mau
   - ICON: Upload gambar profil bot (optional)

**3. Copy Bot Token**
   - Di bagian **TOKEN**, klik **"Reset Token"**
   - Klik **"Yes, do it!"** untuk confirm
   - Klik **"Copy"** untuk copy token
   - **SIMPAN TOKEN INI DENGAN AMAN!** (akan dipakai nanti)
   - ⚠️ **JANGAN SHARE TOKEN KE SIAPAPUN!**

**4. Aktifkan Privileged Gateway Intents**
   - Scroll ke bawah ke bagian **"Privileged Gateway Intents"**
   - Aktifkan (toggle ON):
     - ✅ **MESSAGE CONTENT INTENT**
   - Klik **"Save Changes"** di bawah

✅ **Checkpoint**: Bot token sudah dicopy & Message Content Intent sudah aktif

---

### C. Invite Bot ke Server Discord

**1. Buka OAuth2 URL Generator**
   - Di sidebar kiri, klik **"OAuth2"** → **"URL Generator"**

**2. Select Scopes**
   - Di bagian **SCOPES**, centang:
     - ✅ **bot**

**3. Select Bot Permissions**
   - Di bagian **BOT PERMISSIONS** (muncul setelah centang "bot"), centang:
     - ✅ **Send Messages**
     - ✅ **Read Messages/View Channels**
     - ✅ **Read Message History**

**4. Copy Generated URL**
   - Scroll ke bawah
   - Di bagian **GENERATED URL**, klik **"Copy"**

**5. Open URL & Invite Bot**
   - Paste URL tadi ke browser baru
   - Pilih server yang ingin ditambahkan bot
     (⚠️ Anda harus punya permission "Manage Server" di server tersebut)
   - Klik **"Continue"** → **"Authorize"**
   - Selesaikan CAPTCHA jika ada
   - Bot akan masuk ke server Anda

✅ **Checkpoint**: Bot sudah ada di server Discord Anda (cek member list)

---

## PART 3: Setup Project Locally (5 menit)

**1. Download File credentials.json**
   - File `credentials.json` yang tadi didownload dari Google Cloud
   - Pindahkan file ini ke folder project: `/Users/vanmeyer/Sites/discord-bot-sheets/`

**2. Buat File .env**
   - Masuk ke folder `/Users/vanmeyer/Sites/discord-bot-sheets/`
   - Copy file `.env.example` jadi `.env`:
     ```bash
     cd /Users/vanmeyer/Sites/discord-bot-sheets
     cp .env.example .env
     ```

**3. Edit File .env**
   - Buka file `.env` dengan text editor
   - Ganti isi dengan:
     ```env
     TOKEN=paste_discord_bot_token_disini
     SHEET_NAME=Data Member RTA
     ```
   - Ganti `paste_discord_bot_token_disini` dengan token Discord yang tadi dicopy
   - **CONTOH (JANGAN COPY INI)**:
     ```env
     TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
     SHEET_NAME=Data Member RTA
     ```

✅ **Checkpoint**: Ada 2 file di folder project:
   - ✅ `credentials.json` (dari Google Cloud)
   - ✅ `.env` (berisi TOKEN dan SHEET_NAME)

---

## PART 4: Test Bot Locally (Optional)

Jika ingin test dulu sebelum deploy ke Railway:

**1. Install Python Dependencies**
   ```bash
   cd /Users/vanmeyer/Sites/discord-bot-sheets
   pip install -r requirements.txt
   ```

**2. Run Bot**
   ```bash
   python bot.py
   ```

**3. Cek Output**
   Jika berhasil, akan muncul:
   ```
   Successfully connected to Google Sheet: Data Member RTA
   Bot logged in as RTA Bot#1234
   Connected to 1 server(s)
   Ready to receive commands!
   ```

**4. Test di Discord**
   - Buka server Discord
   - Ketik: `!help`
   - Bot harus reply dengan panduan penggunaan

**5. Test Command Daftar**
   ```
   !daftar
   Username Roblox : TestUser
   Nama Panggilan : Test
   Jenis Kelamin : Laki-laki
   Domisili : Jakarta
   Tanggal Lahir : 1 Januari 2000
   Device yang Digunakan : PC
   Social Media : @testuser
   ```

**6. Cek Google Sheet**
   - Buka Google Sheet "Data Member RTA"
   - Data harus muncul di baris 2

**7. Stop Bot (untuk deploy ke Railway)**
   - Tekan `Ctrl + C` di terminal

✅ **Checkpoint**: Bot jalan di local dan bisa menyimpan data ke Google Sheets

---

## PART 5: Deploy ke Railway (10 menit)

### A. Upload ke GitHub

**1. Buat Repository Baru di GitHub**
   - Buka https://github.com/new
   - Repository name: **discord-bot-sheets**
   - Visibility: **Private** (recommended) atau Public
   - **JANGAN** centang "Add a README file"
   - Klik **Create repository**

**2. Initialize Git di Project**
   ```bash
   cd /Users/vanmeyer/Sites/discord-bot-sheets
   git init
   git add .
   git commit -m "Initial commit - Discord bot with Google Sheets"
   ```

**3. Push ke GitHub**
   Ganti `YOUR_USERNAME` dengan username GitHub Anda:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/discord-bot-sheets.git
   git branch -M main
   git push -u origin main
   ```

   Jika diminta login:
   - Username: username GitHub Anda
   - Password: Personal Access Token (bukan password biasa)

✅ **Checkpoint**: Code sudah ada di GitHub (cek di browser)

⚠️ **PENTING**: Pastikan file `.env` dan `credentials.json` TIDAK terupload (cek di GitHub, kedua file ini tidak boleh ada)

---

### B. Deploy di Railway

**1. Login Railway**
   - Buka https://railway.app/
   - Klik **"Login"**
   - Login with GitHub
   - Authorize Railway

**2. Create New Project**
   - Klik **"New Project"**
   - Pilih **"Deploy from GitHub repo"**
   - Jika diminta "Configure GitHub App", klik **"Configure GitHub App"**
     - Pilih repository **discord-bot-sheets**
     - Klik **"Install & Authorize"**
   - Pilih repository **discord-bot-sheets**

**3. Tunggu Initial Deploy**
   - Railway akan otomatis deploy pertama kali
   - **Deploy ini akan GAGAL** (karena belum ada environment variables)
   - Itu normal, lanjut ke langkah selanjutnya

**4. Add Environment Variables**
   - Klik project yang baru dibuat
   - Klik service/deployment Anda
   - Klik tab **"Variables"**
   - Klik **"New Variable"** dan tambahkan:

   **Variable 1:**
   - Variable: `TOKEN`
   - Value: (paste Discord bot token Anda)

   **Variable 2:**
   - Variable: `SHEET_NAME`
   - Value: `Data Member RTA`

**5. Upload credentials.json**

   Ada 2 cara, pilih salah satu:

   **Cara 1: Commit ke Private Repo (Mudah)** ✅ Recommended
   - Pastikan repository GitHub Anda **PRIVATE**
   - Edit file `.gitignore`:
     ```bash
     cd /Users/vanmeyer/Sites/discord-bot-sheets
     nano .gitignore
     ```
   - Hapus atau comment baris `credentials.json`:
     ```
     .env
     # credentials.json
     ```
   - Save dan commit:
     ```bash
     git add .gitignore credentials.json
     git commit -m "Add credentials for Railway"
     git push
     ```
   - Railway akan auto-redeploy

   **Cara 2: Environment Variable (Lebih Aman)**
   - Buka file `credentials.json`
   - Copy SEMUA isinya (dari { sampai })
   - Di Railway Variables, tambahkan:
     - Variable: `GOOGLE_CREDENTIALS`
     - Value: (paste semua isi credentials.json)
   - Perlu update code `bot.py` untuk membaca dari env variable (kompleks)

**6. Redeploy**
   - Jika pakai Cara 1, Railway auto-deploy setelah push
   - Jika pakai Cara 2:
     - Klik tab **"Deployments"**
     - Klik **"Redeploy"** pada deployment terakhir

**7. Check Logs**
   - Klik tab **"Logs"**
   - Tunggu sampai muncul:
     ```
     Successfully connected to Google Sheet: Data Member RTA
     Bot logged in as RTA Bot#1234
     ```
   - Jika ada error, cek bagian Troubleshooting di bawah

✅ **Checkpoint**: Bot online 24/7 dan bisa menerima command di Discord!

---

## PART 6: Test Bot Production

**1. Test Command !help**
   - Buka server Discord
   - Ketik: `!help`
   - Bot harus reply

**2. Test Command !check**
   - Ketik: `!check`
   - Bot harus reply dengan info koneksi

**3. Test Command !daftar**
   ```
   !daftar
   Username Roblox : ProductionTest
   Nama Panggilan : Prod
   Jenis Kelamin : Laki-laki
   Domisili : Surabaya
   Tanggal Lahir : 15 Mei 2005
   Device yang Digunakan : Mobile
   Social Media : @prodtest
   ```

**4. Verify di Google Sheets**
   - Buka Google Sheet "Data Member RTA"
   - Data harus muncul sebagai baris baru

✅ **SELESAI!** Bot sudah online dan siap digunakan!

---

## Troubleshooting

### Bot tidak online di Discord
- Cek Railway logs → ada error?
- Cek environment variable TOKEN → sudah benar?
- Cek Message Content Intent → sudah aktif?

### Error: "credentials.json not found"
- **Jika pakai Cara 1**: Pastikan credentials.json sudah di-push ke GitHub
- **Jika pakai Cara 2**: Pastikan GOOGLE_CREDENTIALS sudah diset di Railway variables

### Error: "Spreadsheet not found"
- Cek SHEET_NAME di Railway → harus sama persis dengan nama sheet
- Cek Google Sheet → sudah di-share ke service account email?

### Bot reply tapi data tidak masuk sheet
- Test dengan `!check` → koneksi OK?
- Cek format command → harus ada 7 field
- Cek Google Sheet → service account role = Editor?

### Railway deployment failed
- Cek Logs di Railway
- Pastikan requirements.txt ada
- Pastikan Procfile ada

---

## Support

Jika masih ada masalah, screenshot:
1. Railway logs (tab Logs)
2. Environment variables (tab Variables) - **sensor TOKEN!**
3. Error message di Discord

Lalu tanyakan ke developer atau buat issue di GitHub repository.
