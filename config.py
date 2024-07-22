import os
from urllib.parse import quote_plus

class Settings:
    PROJECT_NAME: str = "ChatGPT Automation"
    PROJECT_VERSION: str = "1.0.0"
    
    MYSQL_USER: str = os.getenv("MYSQL_USER", "sohel")
    MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD", "Sohel@123"))
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", 3306)
    MYSQL_DB: str = os.getenv("MYSQL_DB", "chatgpt_db")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    CHROME_PATH: str = "/usr/bin/google-chrome"
    CHROME_DRIVER_PATH: str = "/usr/local/bin/chromedriver"
    
settings = Settings()