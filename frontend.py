from flask import *

import api

app = Flask(__name__)
app.config["DEBUG"] = True

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
    return redirect(url_for('login'), code=301)
#
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username                    = request.form.get('username')
        api.cloud_provider          = request.form.get('cloud')
        api.export_access_key       = "export AWS_ACCESS_KEY_ID=" + request.form.get('access_key')
        api.export_secret_key       = "export AWS_SECRET_ACCESS_KEY=" + request.form.get('secret_key')

        return redirect(url_for('instance'), code=303)
    return render_template('login.html')

#
@app.route('/instance', methods=['GET', 'POST'])
def instance():
    if request.method == 'POST':
        api.aws_region  = request.form.get('aws-region')
        #api.ec2_type   = request.form.get('ec2-type')
        api.public_key  = request.form.get('public-key')

        api.build_iac()

        return redirect(url_for('scanners'), code=303)
    return render_template('instance.html')

#
@app.route('/scanners', methods=['GET', 'POST'])
def scanners():
    if request.method == 'POST':
        application_scan_name   = request.form.get('name')
        url                     = request.form.get('url')
        bool_scanners=["False","False","False"]
        if request.form.get('owasp'):
            bool_scanners[0]=True
        if request.form.get('wapiti'):
            bool_scanners[1]=True
        if request.form.get('nikto'):
            bool_scanners[2]=True

        api.scan_request(application_scan_name, url, bool_scanners)

        return redirect(url_for('waiting'), code=303)
    return render_template('scanners.html')

@app.route('/destroy', methods=['GET'])
def destroy():
    api.destroy_aws_iac()
    print("WAS infrastructure has been destroied")
    return redirect(url_for('login'), code=303)

@app.route('/waiting', methods=['GET'])
def waiting():
    return render_template('waiting.html')

@app.route('/report', methods=['GET'])
def get_report():



    return render_template('report.html')

if __name__ == "__main__":
    app.run()
