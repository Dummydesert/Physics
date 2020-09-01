# -*- coding: utf-8 -*-
import json
from flask_bootstrap import Bootstrap
from flask import render_template, session, redirect, url_for, request, flash, jsonify, Flask
from datetime import datetime
from MruCalculator import calculadora
from TorricelliCalculator import calculadora


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A5LaOMqaJjhBkHC0xqWBd0xiKfr0801C'
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mru')
def mru():
    return render_template('mru.html')

@app.route('/toricelli')
def torricelli():
    return render_template('torriceli.html')

@app.route('/calc', methods=['POST'])
def calc():
    if request.method == 'POST':
        data = request.get_json()
        if len(data):
            resp = calculadora(data[0]["meu_campo1"], data[0]["meu_campo2"], data[0]["meu_campo3"])
            return jsonify({"calculo": resp})
    return redirect(url_for("index"))

@app.route('/calc2', methods=['POST'])
def calc2():
    if request.method == 'POST':
        data = request.get_json()
        if len(data):
            resp = calculadora(data[0]["meu_campo1"], data[0]["meu_campo2"], data[0]["meu_campo3"])
            return jsonify({"calculo": resp})
    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # app.run(host='0.0.0.0', use_reloader=False)
    app.run(host='0.0.0.0', debug=True, use_reloader=False)



