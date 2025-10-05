import os
from dotenv import load_dotenv

print("🚀 FRED ingestion script started")

# Load environment variables
load_dotenv()

# Just to confirm it's loading FRED credentials:
fred_key = os.getenv("FRED_API_KEY")

if fred_key:
    print("✅ FRED API Key loaded")
else:
    print("❌ FRED API Key not found in environment")

# Placeholder for actual ingestion logic
print("⚙️ Placeholder: connect to FRED and pull data")
