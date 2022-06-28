from os import environ
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

from dotenv import load_dotenv

load_dotenv()

COOKIES_PER_PAGE = 4