# myApp/__init__.py
"""
The flask application package.
"""
import os
from datetime import datetime
# third-party imports
from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from . config import app_config
from logging.config import dictConfig

#print('###dictConfig###',dictConfig)
################################################################################
################################################################################
################################################################################
### Define the WSGI application object
################################################################################
################################################################################
################################################################################
print('#############################################################')
print('###CREATE FLASK-APP###','app = Flask(__name__, instance_relative_config=True)')
app = Flask(__name__, instance_relative_config=True) #--> important: the folders are relative to where the flask app is created
################################################################################
################################################################################
################################################################################
### Configurations
################################################################################
################################################################################
################################################################################
print('')
print('###CONFIGURE FLASK-APP###')
print('   CONFIG-1-FROM-INSTANCE','../instance/config.py')
app.config.from_pyfile('../instance/config.py') #from instance
print('   (1-instance) EYECATCH---',app.config['EYECATCH'])
print('   (1-instance) SQLALCHEMY_DATABASE_URI---',app.config['SQLALCHEMY_DATABASE_URI'])
################################################################################
#########################################################################################
print('   CONFIG-2-FROM-ROOT','../config.py')
app.config.from_pyfile('../config.py') #from the (server) root
print('   (2-root) EYECATCH---',app.config['EYECATCH'])
print('   (2-root) SQLALCHEMY_DATABASE_URI---',app.config['SQLALCHEMY_DATABASE_URI'])
#########################################################################################
config_name = app.config['EXECUTION_ENVIRONMENT']
print('   CONFIG-3-APP-ENVIRONMENT',config_name,'.config.py')
app.config.from_object(app_config[config_name])
print('   3(environment)',config_name,'EYECATCH---',app.config['EYECATCH'])
print('   3(environment)',config_name,'SQLALCHEMY_DATABASE_URI---',app.config['SQLALCHEMY_DATABASE_URI'])
#########################################################################################
config_name = app.config['EXECUTION_MODE']
print('   CONFIG-4-APP-EXEC-MODE',config_name,'.config.py')
app.config.from_object(app_config[config_name])
print('   4(exec-mode)',config_name,'EYECATCH---',app.config['EYECATCH'])
print('   4(exec-mode)',config_name,'SQLALCHEMY_DATABASE_URI---',app.config['SQLALCHEMY_DATABASE_URI'])
#########################################################################################
#########################################################################################
print('   @@@check','RECAPTCHA_SITE_KEY---',app.config['RECAPTCHA_SITE_KEY'])
print('   @@@check','RECAPTCHA_SECRET_KEY---',app.config['RECAPTCHA_SECRET_KEY'])
################################################################################
################################################################################
################################################################################
### ?????????????
################################################################################
################################################################################
################################################################################
print('')
print('###BOOTSTRAP APP###','Bootstrap(app)')
Bootstrap(app)
################################################################################
################################################################################
################################################################################
### Define the database object which is imported by modules and controllers
################################################################################
################################################################################
################################################################################
print('')
print('###DATABASE###','db = SQLAlchemy(app)')
db = SQLAlchemy()
db.init_app(app)
################################################################################
################################################################################
################################################################################
### LoginManager
################################################################################
################################################################################
################################################################################
print('')
print('###LOGIN-MANAGER###','login_manager = LoginManager(application)')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "home.login"
################################################################################
################################################################################
################################################################################
### Migration Manager
################################################################################
################################################################################
################################################################################
print('')
print('###Migration-MANAGER###')
migrate = Migrate(app, db)
################################################################################
################################################################################
################################################################################
### Home page
################################################################################
################################################################################
################################################################################
#print('')
#print('###HOME_PAGE###',"render_template('page_templates/landing_page.html',title='landing page')")
#@app.route('/')
#def landingpage():
#    print('LANDINGPAGE',request.method,request.url)
#    #session['username'] = "someuser"
#    #session['urls'] = []
#    return render_template('page_templates/landing_page.html',title='landing page'
#    )
################################################################################
################################################################################
################################################################################
### HTTP Error Handlers
################################################################################
################################################################################
################################################################################
print('')
print('###ERROR_HANDLERS###')
print('   @app.errorhandler(403)','render_template(errors/403.html, title=Forbidden)')
@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403

print('   @app.errorhandler(404)','render_template(errors/404.html, title=Page Not Found)')
@app.errorhandler(404)
def page_not_found(error):
    varPageName = str(request._get_current_object())
    return render_template('errors/404.html', title='Page Not Found',PageNotFound=varPageName), 404

print('   @app.errorhandler(500)','render_template(errors/500.html, title=Server Error)')
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500

################################################################################
################################################################################
################################################################################
# import home pages
################################################################################
################################################################################
################################################################################
print('\n###HOME PAGES###')
from . import views
################################################################################
################################################################################
################################################################################
# Register blueprint(s) for pages
################################################################################
################################################################################
################################################################################
print('')
print('###BLUEPRINTS (SUB-APPCOMPONENTS)###')
# Import modules/components using their blueprint handler variable i.e module_authoroization

### authorization module
from . module_home.controllers import home as authorization_module
app.register_blueprint(authorization_module,url_prefix='/home')
print('   autorization_module---','app.register_blueprint(authorization_module,url_prefix=''/authorization'')')

### protototypes page
#from . module_prototypes.controllers import prototypes as prototypes_module
#app.register_blueprint(prototypes_module,url_prefix='/prototypes')
print('   prototypes_module---','app.register_blueprint(prototypes_module,url_prefix=''/prototypes'')')

#from app import models
#from .admin import admin as admin_blueprint
#app.register_blueprint(admin_blueprint, url_prefix='/admin')


################################################################################
################################################################################
################################################################################
################################################################################
### functions and variables
################################################################################
################################################################################
################################################################################
print('')
print('###FUNCTIONS & VARIABLES###')
def get_time():
    now = datetime.now()
    time=now.strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, surname, email):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('DateStamp={}, Name={}, Surname={}, Email={} \n'.format(timestamp, name, surname, email))
    data.close()
################################################################################
################################################################################
################################################################################
################################################################################
### context processor
################################################################################
################################################################################
################################################################################
@app.context_processor
def inject_configuration_parameters_as_variables():
    print('   ###SERVER_RUNNING###','inject_configuration_parameters_as_variables:')
    return dict(
         GOOGLE_RECAPTCHA_CHECKBOX_SITE_KEY=app.config['GOOGLE_RECAPTCHA_CHECKBOX_SITE_KEY']
        ,GOOGLE_RECAPTCHA_CHECKBOX_SECRET_KEY=app.config['GOOGLE_RECAPTCHA_CHECKBOX_SECRET_KEY']
        ,GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY=app.config['GOOGLE_RECAPTCHA_INVISIBLE_SITE_KEY']
        ,GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY=app.config['GOOGLE_RECAPTCHA_INVISIBLE_SECRET_KEY']
        ,RECAPTCHA_SITE_KEY=app.config['RECAPTCHA_SITE_KEY']
        ,RECAPTCHA_SECRET_KEY=app.config['RECAPTCHA_SECRET_KEY']
        ,RECAPTCHA_PUBLIC_KEY=app.config['RECAPTCHA_PUBLIC_KEY']
        ,RECAPTCHA_PRIVATE_KEY=app.config['RECAPTCHA_PRIVATE_KEY']
        ,LAYOUTS_FOLDER=app.config['LAYOUTS_FOLDER']
        ,TEMPLATES_FOLDER=app.config['TEMPLATES_FOLDER']
        ,FORMS_FOLDER=app.config['FORMS_FOLDER']
        ,PAGES_FOLDER=app.config['PAGES_FOLDER']
        ,COMPONENTS_FOLDER=app.config['COMPONENTS_FOLDER']
        ,IMAGES_FOLDER=app.config['IMAGES_FOLDER']
        ,PICTURES_FOLDER=app.config['PICTURES_FOLDER']
        ,UPLOAD_FOLDER=app.config['UPLOAD_FOLDER']
        ,ALLOWED_EXTENSIONS=app.config['ALLOWED_EXTENSIONS']
        ,AVAILABLE_LANGUAGES=app.config['LANGUAGES']
        ,CURRENT_LANGUAGE=session.get('language',request.accept_languages.best_match(app.config['LANGUAGES'].keys()))
        ,DEFAULT_LANGUAGE=app.config['DEFAULT_LANGUAGE']
        ,FLAGS=app.config['FLAGS']
        ,COPYWRITE_YEAR=app.config['COPYWRITE_YEAR']
        ,WEBSITE_TITLE=app.config['DOMAIN_TITLE']
        ,COMPANY_NAME = app.config['COMPANY_NAME']
        ,DOMAIN_NAME=app.config['DOMAIN_NAME']
        ,DOMAIN_TITLE =app.config['DOMAIN_TITLE']
        ,COMPANY_COLOR=app.config['COMPANY_COLOR']
        ,DOMAIN_COLOR=app.config['DOMAIN_COLOR']
        ,COMPANY_ADDRESS=app.config['COMPANY_ADDRESS']
        ,COMPANY_PHONES=app.config['COMPANY_PHONES']
        ,COMPANY_CONTACT_EMAIL=app.config['COMPANY_CONTACT_EMAIL']
        ,COMPANY_SUPPORT_EMAIL=app.config['COMPANY_SUPPORT_EMAIL']
        ,CONTACT_EMAIL=app.config['CONTACT_EMAIL']
        ,SUPPORT_EMAIL=app.config['SUPPORT_EMAIL']
        ,INQUIRY_EMAIL=app.config['INQUIRY_EMAIL']
        ,WEBSITE_ADMIN_EMAIL=app.config['WEBSITE_ADMIN_EMAIL']
        #,recaptcha = recaptcha
)

@app.context_processor
def inject_utility_functions():
    print('   ###SERVER_RUNNING###','inject_utility_functions:')
    #print('###inject_utility_functions:format_price()')
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)

    #print('###inject_utility_functions:language_file()')
    def language_file(file='',language='en'):
        nfile=file
        if (language not in app.config['LANGUAGES']):
            language=app.config['DEFAULT_LANGUAGE']
        if (language!=app.config['DEFAULT_LANGUAGE']):
            nfile=file.replace('.html', '_'+language+'.html')
        return nfile

    #print('###inject_utility_functions:version_file()')
    def version_file(file='',environment='',design='',version=''):
        nfile=file
        if (environment!=''):
            nfile=environment+'/'+nfile
        if (design!=''):
            nfile=nfile.replace('.', '_'+design+'.')
        if (version!=''):
            nfile=nfile.replace('.', '_v'+version+'.')
        return nfile

    #print('###inject_utility_functions:fullpathfile()')
    def fullpathfile(file='',type='TEMPLATE'):
        folder=app.config['TEMPLATES_ROOT_FOLDER']
        if (type.upper()=='LAYOUT'):
            folder=app.config['LAYOUT_FOLDER']
        if (type.upper()=='TEMPLATE'):
            folder=app.config['TEMPLATES_FOLDER']
        if (type.upper()=='PAGE'):
            folder=app.config['PAGES_FOLDER']
        if (type.upper()=='COMPONENT'):
            folder=app.config['COMPONENTS_FOLDER']
        if (type.upper()=='IMAGE'):
            folder=app.config['IMAGES_FOLDER']
        if (type.upper()=='PICTURE'):
            folder=app.config['PICTURES_FOLDER']
        if (type.upper()=='FORM'):
            folder=app.config['FORMS_FOLDER']
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = folder+file1
        return file2

    #print('###inject_utility_functions:image_file()')
    def image_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['IMAGES_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:picture_file()')
    def picture_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['PICTURES_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:flag_file()')
    def flag_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['FLAGS_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:page_file()')
    def page_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['PAGES_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:form_file()')
    def form_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['FORMS_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:component_file()')
    def component_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['COMPONENTS_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:language_page_file()')
    def language_page_file(file='',language='en'):
        nfile=page_file(file)
        if (language not in app.config['LANGUAGES']):
            language=app.config['DEFAULT_LANGUAGE']
        if (language!=app.config['DEFAULT_LANGUAGE']):
            nfile=nfile.replace('.html', '_'+language+'.html')
        return nfile

    #print('###inject_utility_functions:template_file()')
    def template_file(file=''):
        file1=file
        file2=file1
        if (file1.find('/')<0):
            file2 = app.config['TEMPLATES_FOLDER']+file1
        return file2

    #print('###inject_utility_functions:language_fullpathfile()')
    def language_fullpathfile(file='',language='en',type='PAGE'):
        nfile=fullpathfile(file,type)
        if (language not in app.config['LANGUAGES']):
            language=app.config['DEFAULT_LANGUAGE']
        if (language!=app.config['DEFAULT_LANGUAGE']):
            nfile=nfile.replace('.html', '_'+language+'.html')
        return nfile

    return dict(
        format_price=format_price
        ,fullpathfile=fullpathfile
        ,language_file=language_file
        ,version_file=version_file
        ,image_file=image_file
        ,picture_file=picture_file
        ,flag_file=flag_file
        ,page_file=page_file
        ,form_file=form_file
        ,language_page_file=language_page_file
        ,language_fullpathfile=language_fullpathfile
        ,template_file=template_file
        ,component_file=component_file
)
################################################################################
################################################################################
################################################################################
# Build the database:This will create the database file using SQLAlchemy
################################################################################
################################################################################
################################################################################
print('')
print('###CREATE DATABASE###','db.create_all()')
#db.create_all()
################################################################################
################################################################################
################################################################################
print('')
print('###FINISHED: FLASK-APP-created&ready###','db.create_all()')
print('')
print('#############################################################')