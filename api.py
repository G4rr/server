from flask import Flask, render_template, request
'''from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
'''

import os

app = Flask(__name__)
app.config["DEBUG"] = True

'''class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')
'''

application_scan_name=""
url=""

export_access_key=""
export_secret_key=""

@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return "<p>HTTP 404 Error Encountered</p>", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<p>HTTP 500 Error Encountered</p>", 500

@app.route('/', methods=['GET'])
def index():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
  
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        application_scan_name = request.form.get('name')
        url = request.form.get('url')
        
        
        
        print(application_scan_name)
        print(url)
        
        
   
    return render_template('home.html')

#...
@app.route('/login/', methods=['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST':
        #username = request.form.get('username')
        #password = request.form.get('password')
        access_key = request.form.get('access_key')
        secret_key = request.form.get('secret_key')
        #aws_link = request.form.get('aws_link')
        
        
        export_access_key='export AWS_ACCESS_KEY_ID='+access_key
        export_secret_key='export AWS_SECRET_ACCESS_KEY='+secret_key

        '''if key1 == 'root' and key2 == 'pass':
            message = "Correct key1 and password"
        else:
            message = "Wrong key2 or password"
'''

    return render_template('login.html', message=message) 
 
 
 #@app.route('/aws', methods=['GET', 'POST'])
 #   if request.method == 'POST':
 #       region = request.form.get('region')
 #   return render_template('aws_settings.html')
 
 
if __name__ == "__main__":
    app.run() 

def build_aws_infrastructure_file():
    #with open('', 'w') as aws_file: 
    print("")

def build_aws_infrastructure():
    os.system(export_access_key)
    os.system(export_secret_key)

    print("")


def build_scan_request():
    print("")


def build_report():
    print("")

