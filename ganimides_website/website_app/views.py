"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import logging
from . import app
###########################################################################
###########################################################################
###########################################################################

##########################################
#put this after @ decorator
##########################################
#how to get a config variable app.config.get('GOOGLE_RECAPTCHA_CHECKBOX_SITE_KEY'))
#how to get a config variable app.config.get('GOOGLE_RECAPTCHA_CHECKBOX_SECRET_KEY'))

#request.method:              GET
#request.url:                 http://127.0.0.1:5000/alert/dingding/test?x=y
#request.base_url:            http://127.0.0.1:5000/alert/dingding/test
#request.url_charset:         utf-8
#request.url_root:            http://127.0.0.1:5000/
#str(request.url_rule):       /alert/dingding/test
#request.host_url:            http://127.0.0.1:5000/
#request.host:                127.0.0.1:5000
#request.script_root:
#request.path:                /alert/dingding/test
#request.full_path:           /alert/dingding/test?x=y

#request.args:                ImmutableMultiDict([('x', 'y')])
#request.args.get('x'):       y
##########################################


#varPageName = request.args.get('url')
#alert(varPageName)
#print('xxxrequestxxxxxxx',varPageName)
#print('xxxqqqqxxxxxxx',e)
#return render_template('404.html'), 404
#print ('xxxx:',request)
###########################################################################
###########################################################################
###########################################################################
### define the routes, accepted methods (GET/POST) and the service function
###########################################################################
###########################################################################
###########################################################################
#@app.before_first_request
#def logging_init():
#    logging.basicConfig(
#        datefmt = '%Y-%m-%d %H:%M:%S',
#        format = '%(asctime)s%%%(message)s',
#        filename = 'home/ganimides/routing.log',
#        level=logging.CRITICAL)

#@app.after_request
#def store_visted_urls():
#    session['urls'].append(request.url)
#    if(len[session['urls']) > 5:
#        session['urls'].pop(0)
#    session.modified = True

#@app.after_request

@app.route('/')
def landingpage():
    #logging.critical('a request!')
    app.logger.info('%s logged in successfully', 'user.username')
    print('LANDINGPAGE',request.method,request.url)
    #session['username'] = "someuser"
    #session['urls'] = []
    return render_template(
        'page_templates/landing_page.html'
        ,title='landing page'
    )

@app.route('/landingpage')
def homepage():
    print('HOME',request.method,request.url)
    #logging.critical('LANDINGPAGE')
    #session['username'] = "someuser"
    #session['urls'] = []
    return render_template(
        'page_templates/landing_page.html'
        ,title='landing page'
    )

@app.route('/language/<language>')
def set_language(language=None):
    print('LANGUAGE',request.method,request.url)
    session['language'] = language
    return redirect(url_for('homepage'))

@app.route('/contact')
def contact():
    print('CONTACT',request.method,request.url)
    data = []
    if 'urls' in session:
        data = session['urls']

    return render_template(
        'page_templates/contact.html'
        ,title='Ganimides Contact Info'
        ,pages=data
    )

@app.route('/about')
def about():
    print('ABOUT',request.method,request.url)
    return render_template(
        'page_templates/about.html'
        ,title='about Ganimides'
    )


@app.route('/company')
def company():
    print('COMPANY',request.method,request.url)
    return render_template(
        'page_templates/company.html'
        ,title='the company'
    )

@app.route('/services')
def services():
    print('SERVICES',request.method,request.url)
    return render_template(
        'page_templates/services.html'
        ,title='services'
    )

@app.route('/why')
def why():
    print('WHY',request.method,request.url)
    return render_template(
        'page_templates/why.html'
        ,title='why ganimides'
    )

@app.route('/research')
def research():
    print('RESEARCH',request.method,request.url)
    return render_template(
        'page_templates/research.html'
        ,title='research'
    )

@app.route('/academy')
def academy():
    print('ACADEMY',request.method,request.url)
    return render_template(
        'page_templates/academy.html'
        ,title='BUSTEC ACADEMY'
    )

@app.route('/knowledge')
def knowledge():
    print('KNOWLEDGE',request.method,request.url)
    return render_template(
        'page_templates/knowledge.html'
        ,title='KNOWLEDGE CENTER'
    )

@app.route('/prototypes')
def prototypes():
    print('PROTOTYPES',request.method,request.url)
    return render_template(
        'page_templates/prototypes.html'
        ,title='PROTOTYPES'
    )

@app.route('/cookies_policy')
def cookies_policy():
    print('COOKIES',request.method,request.url)
    return render_template(
        'page_templates/cookies_policy.html'
        ,title='cookies policy'
    )

@app.route('/privacy_policy')
def privacy_policy():
    print('PRIVACY_POLICY',request.method,request.url)
    return render_template(
        'page_templates/privacy_policy.html'
        ,title='privacy policy'
    )

@app.route('/terms_and_conditions')
def terms_and_conditions():
    print('TERMS_AND_CONDITIONS',request.method,request.url)
    return render_template(
        'page_templates/terms_and_conditions.html'
        ,title='terms and conditions of use'
    )

@app.route('/myBank')
#@login_required
def myBank():
    print('MYBANK',request.method,request.url)
    """Renders the app(myBank) home page."""
    return render_template(
        'mybank/mybank_index.html'
        ,title='myBank'
        ,message='open banking prototype........'
    )

@app.route('/myGame')
def myGame():
    print('MYGAME',request.method,request.url)
    """Renders the app(myBank) home page."""
    return render_template(
        'myGame/myGame.html'
        ,title='myGame'
        ,message='gaming prototype........'
    )