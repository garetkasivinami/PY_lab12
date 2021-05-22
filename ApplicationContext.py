from flask import Flask, request

app = Flask(__name__, template_folder='Views')
app.config.update(
    SECRET_KEY='a07e37293bae2004aab330af8e3795be547a0368b408cd476b9947fdf409df8c'
)