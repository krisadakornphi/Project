from flask import Flask, render_temp, jsonify
import psutil

app Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def moniter():
    #ดึงรายงานการเชื่มต่อ Network
    connection = []
    for connin psutil.net_connections(kind='inet'):
        