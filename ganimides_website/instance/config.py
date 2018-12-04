# myServer/instance/config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
EYECATCH='INSTANCE'
EXECUTION_MODE = 'sandbox'
EXECUTION_ENVIRONMENT = 'pythonanywhere'
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_SERVER = 'smtp.yandex.ru'
DEBUG = True

if MAIL_SERVER=='smtp.yandex.ru':
    # email server yandex
    os.environ["MAIL_SERVER"] = "smtp.yandex.ru"
    os.environ["MAIL_PORT"] = "587"
    os.environ["MAIL_USE_TLS"] = "True"
    os.environ["MAIL_USE_SSL"] = "True"
    os.environ["MAIL_USERNAME"] = "ganimidis" #without the @yandex.ru
    os.environ["MAIL_PASSWORD"] = "****"
else:
    # email server google
    os.environ["MAIL_SERVER"] = "smtp.googlemail.com"
    os.environ["MAIL_PORT"] = "465"
    os.environ["MAIL_USE_TLS"] = "False"
    os.environ["MAIL_USE_SSL"] = "True"
    os.environ["MAIL_USERNAME"] = "ganimidis@gmail.com"
    os.environ["MAIL_PASSWORD"] = "philea13"

if EXECUTION_ENVIRONMENT=='pythonanywhere':
    os.environ["RECAPTCHA_SITE_KEY"] = "6LfEOH4UAAAAAKTQUTNS0CJODZ4DbVFi0cQl1oUn"
    os.environ["RECAPTCHA_SECRET_KEY"] = "6LfEOH4UAAAAAOUudlGYDGRUdR6w8fqj6ACrFVRw"
    os.environ["RECAPTCHA_INVISIBLE_SITE_KEY"] = "...."
    os.environ["RECAPTCHA_INVISIBLE_SECRET_KEY"] = "..."
else:
    os.environ["RECAPTCHA_SITE_KEY"] = "6LcD3XkUAAAAABAoO2p4WOoBGg6uRyCoVCcGNCFV"
    os.environ["RECAPTCHA_SECRET_KEY"] = "6LcD3XkUAAAAAHTNpV8RsDN8CybCNEJ0htRddCMq"
    os.environ["RECAPTCHA_INVISIBLE_SITE_KEY"] = "6LfL2HkUAAAAAF8ot-2aPAHYzHPAAxvLtKI-PyXi"
    os.environ["RECAPTCHA_INVISIBLE_SECRET_KEY"] = "6LfL2HkUAAAAAIdjgyCwgSaV2hvOS6APpoXot1yw"

################################################################
### Secret key for signing cookies
################################################################
SECRET_KEY = 'p9Bv<3Eid9%$i01'
SECRET_KEY = os.environ.get('SECRET_KEY') or 'aeiotheosomegasgeometreip9Bv<3Eid9%$i01'
SECURITY_PASSWORD_SALT = 'aeiotheosomegasgeometreip9Bv<bobbistarr'
################################################################
### database config
################################################################
SQLALCHEMY_POOL_RECYCLE = 299
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_RECORD_QUERIES = True
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimedes:philea13@localhost/ganimides_db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ganimides:philea13@ganimides.mysql.pythonanywhere-services.com/ganimides$ganimides_db'
print('###instance### ###config.py### SQLALCHEMY_DATABASE_URI=',SQLALCHEMY_DATABASE_URI)
username = "ganimides"
password = "philea13"
hostname = "ganimides.mysql.pythonanywhere-services.com"
databasename = "ganimides$ganimides_db"
database_username = "ganimides"
database_password = "spithas13"
SQLALCHEMY_DATABASE_URI2 = "mysql+{mysqlconnector}://{username}:{password}@{hostname}/{databasename}".format(
    mysqlconnector="pymysql",
    username="ganimides",
    password="philea13",
    hostname="ganimides.mysql.pythonanywhere-services.com",
    databasename="ganimides$ganimides_db"
)
print('###instance### ###config.py### SQLALCHEMY_DATABASE_URI2=',SQLALCHEMY_DATABASE_URI)
#db = SQLAlchemy(app, engine = create_engine("mysql+myqldb://ganimides:philea13@ganimides.mysql.pythonanywhere-services.com/ganimides$ganimides_db", pool_recycle=280))
#mysql://InsulT:password@mysql.server/InsulT$default'
#{
#    "host": "localhost",
#    "user": "root",
#    "password": "philea13",
#    "database": "db",
#    "sql_engine": "mysql+pymysql",
#    "charset": "utf8"
#}
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#DATABASE_CONNECT_OPTIONS = {}
#############################################################################################
# mail server
#############################################################################################
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
MAIL_userName = os.environ.get('MAIL_userName', 'ganimidis@gmail.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'philea13')

## mail settings google
#MAIL_SERVER = 'smtp.googlemail.com'
#MAIL_PORT = 465
#MAIL_USE_TLS = False
#MAIL_USE_SSL = True
#MAIL_userName = "ganimidis@gmail.com"
#MAIL_PASSWORD = "philea13"

## mail settings yandex
#MAIL_SERVER = 'smtp.yandex.ru'
#MAIL_PORT = 587
#MAIL_USE_TLS = True
#MAIL_USE_SSL = True
#MAIL_userName = 'ganimides' # only login without @yandex.ru
#MAIL_PASSWORD = '******'
#############################################################################################
### mail accounts
#############################################################################################
MAIL_SUBJECT_PREFIX = '[ganimides]'
MAIL_DEFAULT_SENDER = 'noreply@ganimides.com'
MAIL_ADMIN_SENDER = 'admin@ganimides.com'
MAIL_SUPPORT_SENDER = 'support@ganimides.com'
MAIL_SENDER = 'Admin@ganimides.com>'
WEBSITE_ADMIN = os.environ.get('WEBSITE_ADMIN')
#############################################################################################
#google recapcha
#############################################################################################
RECAPTCHA_SITE_KEY=os.environ["RECAPTCHA_SITE_KEY"]
RECAPTCHA_SECRET_KEY=os.environ["RECAPTCHA_SECRET_KEY"]
RECAPTCHA_INVISIBLE_SITE_KEY=os.environ["RECAPTCHA_INVISIBLE_SITE_KEY"]
RECAPTCHA_INVISIBLE_SECRET_KEY=os.environ["RECAPTCHA_INVISIBLE_SECRET_KEY"]
RECAPTCHA_PUBLIC_KEY=os.environ["RECAPTCHA_SITE_KEY"]
RECAPTCHA_PRIVATE_KEY=os.environ["RECAPTCHA_SECRET_KEY"]
GOOGLE_RECAPTCHA_CHECKBOX_SITE_KEY=os.environ["RECAPTCHA_SITE_KEY"]
GOOGLE_RECAPTCHA_CHECKBOX_SECRET_KEY=os.environ["RECAPTCHA_SECRET_KEY"]
GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY=os.environ["RECAPTCHA_SITE_KEY"]
GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY=os.environ["RECAPTCHA_SECRET_KEY"]
################################################################
### miscellaneous
################################################################
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SSL_REDIRECT = False
# Application threads. A common general assumption is using 2 per available processor cores - to handle incoming requests using one and performing background operations using the other.
THREADS_PER_PAGE = 2
# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True
# Use a secure, unique and absolutely secret key for signing the data.
CSRF_SESSION_KEY = "aeiotheosomegasgeometrei"
################################################################
