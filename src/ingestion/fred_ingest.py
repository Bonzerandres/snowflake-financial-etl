import os
from dotenv import load_dotenv

print("🚀 FRED ingestion script started")


load_dotenv()

fred_key = os.getenv("FRED_API_KEY")

if fred_key:
    print("✅ FRED API Key loaded")
else:
    print("❌ FRED API Key not found in environment")


print("⚙️ Placeholder: connect to FRED and pull data")
