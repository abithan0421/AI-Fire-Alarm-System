import os
from dotenv import load_dotenv

def get_email_config():
    """
    Reads email configuration from the .env file and returns it as a dictionary.
    """
    load_dotenv() 

    email_config = {
        "SMTP_SERVER": os.getenv("SMTP_SERVER"),
        "SMTP_PORT": int(os.getenv("SMTP_PORT")),
        "SENDER_EMAIL": os.getenv("SENDER_EMAIL"),
        "SENDER_PASSWORD": os.getenv("SENDER_PASSWORD"),
        "RECIPIENT_EMAIL": os.getenv("RECIPIENT_EMAIL"),
    }

    return email_config