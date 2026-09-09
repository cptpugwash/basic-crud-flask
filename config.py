import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

WTF_CSRF_ENABLED = True

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
	raise RuntimeError(
		'SECRET_KEY is not set. Copy .env.example to .env and set SECRET_KEY, '
		'e.g.: python -c "import secrets; print(secrets.token_hex(32))"'
	)

# sqlite db path setup
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# for when using mysql
#SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@localhost/dbname'