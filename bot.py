import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys
import json
import tempfile

# Configuration
DISCORD_TOKEN = os.getenv("TOKEN")
SHEET_NAME = os.getenv("SHEET_NAME", "Database Discord")
CREDENTIALS_FILE = "credentials.json"

# Required fields for registration
REQUIRED_FIELDS = [
    "Username Roblox",
    "Nama Panggilan",
    "Jenis Kelamin",
    "Domisili",
    "Tanggal Lahir",
    "Device yang Digunakan",
    "Social Media"
]

# Initialize Google Sheets connection
def init_sheets():
    """Initialize Google Sheets API connection"""
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        google_creds_env = os.getenv("GOOGLE_CREDENTIALS")
        if google_creds_env:
            # Load credentials from environment variable (for Railway/Heroku)
            creds_dict = json.loads(google_creds_env)
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        elif os.path.exists(CREDENTIALS_FILE):
            # Load credentials from local file
            creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
        else:
            print(f"Error: No credentials found!")
            print("Set GOOGLE_CREDENTIALS env var or add credentials.json file.")
            sys.exit(1)

        client = gspread.authorize(creds)
        sheet = client.open(SHEET_NAME).sheet1
        return sheet
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Error: Spreadsheet '{SHEET_NAME}' not found!")
        print("Please make sure:")
        print("1. The sheet name is correct")
        print("2. The sheet is shared with the service account email")
        sys.exit(1)
    except Exception as e:
        print(f"Error initializing Google Sheets: {e}")
        sys.exit(1)

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Initialize sheet
try:
    sheet = init_sheets()
    print(f"Successfully connected to Google Sheet: {SHEET_NAME}")
except Exception as e:
    print(f"Failed to initialize: {e}")
    sys.exit(1)

@bot.event
async def on_ready():
    """Called when bot successfully connects to Discord"""
    print(f"Bot logged in as {bot.user}")
    print(f"Connected to {len(bot.guilds)} server(s)")
    print("Ready to receive commands!")

@bot.command(name="daftar")
async def daftar(ctx, *, data: str = None):
    """
    Register user data to Google Sheets

    Usage: !daftar
    Username Roblox : YourUsername
    Nama Panggilan : YourNickname
    Jenis Kelamin : Male/Female
    Domisili : YourCity
    Tanggal Lahir : DD Month YYYY
    Device yang Digunakan : PC/Mobile
    Social Media : YourSocial
    """
    if not data:
        await ctx.send(
            "Format tidak lengkap! Gunakan `!helpRTA` untuk melihat contoh penggunaan."
        )
        return

    try:
        # Parse the input data
        lines = data.strip().split("\n")
        parsed_data = {}

        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                parsed_data[key] = value

        # Validate all required fields are present
        missing_fields = []
        for field in REQUIRED_FIELDS:
            if field not in parsed_data or not parsed_data[field]:
                missing_fields.append(field)

        if missing_fields:
            missing_list = "\n- ".join(missing_fields)
            await ctx.send(
                f"Data tidak lengkap! Field yang hilang:\n- {missing_list}\n\n"
                f"Gunakan `!helpRTA` untuk melihat format yang benar."
            )
            return

        # Validate non-empty values
        empty_fields = [field for field in REQUIRED_FIELDS if not parsed_data[field].strip()]
        if empty_fields:
            empty_list = "\n- ".join(empty_fields)
            await ctx.send(
                f"Field berikut tidak boleh kosong:\n- {empty_list}"
            )
            return

        # Prepare values in correct order
        values = [parsed_data[field] for field in REQUIRED_FIELDS]

        # Find first empty row in column A, then write data there
        col_a = sheet.col_values(1)
        next_row = len(col_a) + 1
        sheet.update(f'A{next_row}:G{next_row}', [values])

        await ctx.send(
            f"Data berhasil disimpan, {ctx.author.mention}!\n"
            f"Terima kasih sudah mendaftar."
        )
        print(f"New registration from {ctx.author} ({ctx.author.id})")

    except gspread.exceptions.APIError as e:
        await ctx.send(
            "Terjadi kesalahan saat menyimpan ke Google Sheets. "
            "Silakan coba lagi atau hubungi admin."
        )
        print(f"Google Sheets API Error: {e}")

    except Exception as e:
        await ctx.send(
            "Terjadi kesalahan yang tidak diketahui. "
            "Silakan cek format data Anda dan coba lagi."
        )
        print(f"Error in daftar command: {e}")

@bot.command(name="helpRTA")
async def help_command(ctx):
    """Show command usage and examples"""
    help_text = """
**Discord Bot - Panduan Penggunaan**

**Command: !daftar**
Digunakan untuk mendaftar dan menyimpan data ke database.

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

**Command Lainnya:**
- `!helpRTA` - Menampilkan panduan ini
- `!check` - Mengecek koneksi database

**Catatan:**
- Pastikan semua field diisi
- Gunakan format `Field : Value`
- Setiap field harus di baris baru
    """
    await ctx.send(help_text)

@bot.command(name="check")
async def check(ctx):
    """Verify Google Sheets connection"""
    try:
        # Try to access the sheet
        sheet_title = sheet.title
        row_count = len(sheet.get_all_values())

        await ctx.send(
            f"Koneksi OK!\n"
            f"Sheet: {SHEET_NAME}\n"
            f"Total baris: {row_count}"
        )
        print(f"Connection check by {ctx.author} - OK")

    except gspread.exceptions.APIError as e:
        await ctx.send(
            "Koneksi ke Google Sheets gagal. "
            "Silakan hubungi admin."
        )
        print(f"Google Sheets API Error in check: {e}")

    except Exception as e:
        await ctx.send(
            "Terjadi kesalahan saat mengecek koneksi."
        )
        print(f"Error in check command: {e}")

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "Command tidak ditemukan! Gunakan `!helpRTA` untuk melihat daftar command."
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Format command salah! Gunakan `!helpRTA` untuk melihat cara penggunaan."
        )
    else:
        await ctx.send(
            "Terjadi kesalahan. Silakan coba lagi atau gunakan `!helpRTA`."
        )
        print(f"Command error: {error}")

# Run the bot
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("Error: TOKEN environment variable not set!")
        print("Please set your Discord bot token in the .env file or environment variables.")
        sys.exit(1)

    try:
        bot.run(DISCORD_TOKEN)
    except discord.errors.LoginFailure:
        print("Error: Invalid Discord token!")
        print("Please check your TOKEN in the .env file or environment variables.")
    except Exception as e:
        print(f"Error starting bot: {e}")
