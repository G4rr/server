from flask import Flask, render_template, request
'''from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
'''

import blockstf.btf as btf
import blockstf.udtf as udtf
import blockstf.bcdktf as bcdktf

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

access_key=""
secret_key=""

aws_region=""
#ec2_type=""

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
        
        setup()
   
    return render_template('home.html')

#...
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #username = request.form.get('username')
        #password = request.form.get('password')
        access_key = request.form.get('access_key')
        secret_key = request.form.get('secret_key')
        #aws_link = request.form.get('aws_link')
        
        
        export_access_key='export AWS_ACCESS_KEY_ID='+access_key
        export_secret_key='export AWS_SECRET_ACCESS_KEY='+secret_key


        print(access_key)
        print(secret_key)

        '''if key1 == 'root' and key2 == 'pass':
            message = "Correct key1 and password"
        else:
            message = "Wrong key2 or password"
'''

    return render_template('login.html') 
 
 
@app.route('/aws', methods=['GET', 'POST'])
def aws_settings():
    if request.method == 'POST':
        aws_region = request.form.get('aws-region')
        #ec2_type = request.form.get('ec2-type')
        setup()
    return render_template('aws-settings.html')
 
 
if __name__ == "__main__":
    app.run() 

def build_iac_tf(filename="aws-iac/setup.tf"):
    with open(filename, 'w') as aws_tf: 
        aws_tf.write(btf.get_provider(ak=access_key, sk=secret_key))
        aws_tf.write(btf.get_aws_ami())
        aws_tf.write(btf.get_aws_security_group())
        aws_tf.write(btf.get_aws_launch_configuration())
        print("Terraform file has been created")
 
def build_iac_sh(filename="aws-iac/setup.sh"):
    with open(filename, 'w') as aws_sh:
        aws_sh.write(udtf.get_default_introduction())
        print("User data file has been created")

def build_aws_iac():
    export_access_key='export AWS_ACCESS_KEY_ID='+access_key
    export_secret_key='export AWS_SECRET_ACCESS_KEY='+secret_key
    os.system(export_access_key)
    os.system(export_secret_key)
    os.system('cd aws-iac')
    os.system('terraform init')
    os.system('terraform apply -auto-approve')
    
    print("Successful")

def destroy_aws_iac():
    os.system('cd aws-iac')
    os.system('terraform destroy')
    os.system('cd ../')
    os.system('rm -rf aws-iac')


def build_scan_request():
    print("")


def build_report():
    print("")
    

def setup():
    os.system('mkdir aws-iac')
    build_iac_tf()
    build_iac_sh()
    build_aws_iac()

