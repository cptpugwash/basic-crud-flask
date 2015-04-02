import os

CSRF_ENABLED = True
SECRET_KEY = 'secretkey'

# sqlite db path setup
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'database.db')

# for when using mysql
#SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@localhost/dbname'