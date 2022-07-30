from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)

COOKIES_PER_PAGE = 4

SECRET_KEY = 'npjMblrkyRBpiQrjbrc5fax6IVLvnfA024rhu924h'



