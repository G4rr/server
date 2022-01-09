import os
import functools
import json
from flask import Flask, render_template, redirect, request, url_for

import api

app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def http_404_handler(error):
    return render_template('404.html', the_title="Page Note Found 404", message="We can't find the content that you're looking for."), 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<p>HTTP 500 Error Encountered</p>", 500

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('login', the_title='Log in'), code=301)
#
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('registration'):
            return redirect(url_for('registration', the_title='Registration'), code=303)
        login = api.Login(request.form.get('username'),
                    request.form.get('password'),
                    request.form.get('admin'))
        if login.authentication:
            return redirect(url_for('menu', the_title='Menu'), code=303)
        else:
            return render_template('login.html', the_title='ReLog in',
                                    message="Password or username incorrect!")
    return render_template('login.html', the_title='Log in')

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        regist = api.Login(request.form.get('username'),
                        request.form.get('password'),
                        request.form.get('admin'))
        regist.registration
        return redirect(url_for('login', the_title='Log in'), code=301)
    return render_template('registration.html', the_title='Registration')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        if request.form.get('scan'):
            return redirect(url_for('scanners', the_title='Choose scanners'), code=301)
        if request.form.get('create_sa'):
            return redirect(url_for('iac_builder', the_title='Setup infrastructure'), code=301)
        if request.form.get('destroy_sa'):
            return redirect(url_for('iac_destroyer', the_title='Destroy infrastructure'), code=301)
        if request.form.get('see_reports'):
            return redirect(url_for('get_reports', the_title='Scan Reports'), code=301)
        if request.form.get('exit'):
            return redirect(url_for('login', the_title='Log in'), code=301)
    return render_template('menu.html', the_title='Menu')

#
@app.route('/iac-builder', methods=['GET', 'POST'])
def iac_builder():
    if request.method == 'POST':
        if request.form.get("deploy"):
            infrastructure = api.Infrastructure(
                            sa_name=request.form.get('sa_name'),
                            provider=request.form.get('provider'),
                            access_key=request.form.get('access_key'),
                            secret_key=request.form.get('secret_key'),
                            region=request.form.get('region'),
                            instance_type=request.form.get('instance_type'),
                            vpc=request.form.get('vpc'),
                            sg_name=request.form.get('sg_name')
            )
            if infrastructure.build_iac:
                return redirect(url_for('scanners', the_title='Set scanners'), code=303)
            else:
                return render_template('build_iac.html', the_title='Setup infrastructure',
                                        message="Error during deployment")
        elif request.form.get("cancel"):
            return redirect(url_for('menu', the_title='Menu'), code=301)
    return render_template('build_iac.html', the_title='Setup infrastructure')

@app.route('/iac-destroyer', methods=['GET', 'POST'])
def iac_destroyer():
    if request.method == 'POST':
        if request.form.get("destroy"):
            destroy(request.form.get("scanner_app"))
            return redirect(url_for('menu', the_title='Menu'), code=301)
        elif request.form.get("cancel"):
            return redirect(url_for('menu', the_title='Menu'), code=301)
    return render_template('destroy_iac.html', the_title='Destroy infrastructure')

#
@app.route('/scanners', methods=['GET', 'POST'])
def scanners():
    if request.method == 'POST':
        if request.form.get("scan"):
            scanners_=["False","False","False"]
            if request.form.get('owasp'):
                scanners_[0]='owasp'
            if request.form.get('wapiti'):
                scanners_[1]='wapiti'
            if request.form.get('nikto'):
                scanners_[2]='nikto'
            scan_request = api.Scanners(
                        title=request.form.get('scan_report_title'),
                        level=request.form.get('scan_level'),
                        sa_name=request.form.get('scanner_app'),
                        url=request.form.get('url'),
                        scanners=scanners_
            )
            if scan_request.scans:
                return redirect(url_for('get_report', file_name=scan_request.get_filename()), code=303)
            else:
                return render_template('scanners.html', the_title='Choose scanners',
                                        message="Error during scanning")
        elif request.form.get("cancel"):
            return redirect(url_for('menu', the_title='Menu'), code=301)
    return render_template('scanners.html', the_title='Choose scanners')

@app.route('/reports', methods=['GET','POST'])
def get_reports():
    if request.method == 'POST':
        return redirect(url_for('get_report', file_name=""), code=303)
    return render_template('reports.html', the_title='Scan Reports')

@app.route('/reports/<file_name>', methods=['GET'])
def get_report(file_name):
    with open(file_name) as file:
        data = json.load(file) # Load final report
        alerts = data["Alerts"] # Fetch all vulnerabilities0
        stats = data["Statistic"] # Fetch statistic of vulnerabilities
        return render_template('report.html', data=data, stats=stats, alerts=alerts)

if __name__ == "__main__":
    app.run()
