import os
import snowflake.connector
from dotenv import load_dotenv

print("FILE EXECUTED")  # Confirm script runs

load_dotenv()  # Load .env

def get_snowflake_connection():
    print("Loading credentials...")
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE")
    )
    return conn

if __name__ == "__main__":
    print("Attempting Snowflake connection...")
    try:
        conn = get_snowflake_connection()
        print("Snowflake connection successful!")
        conn.close()
    except Exception as e:
        print("Connection failed:", str(e))
