from flask import Flask, render_template, jsonify
import subprocess
import sys
import os
import json

app = Flask(__name__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(script):
    subprocess.Popen([sys.executable, script], cwd=BASE)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/normal")
def normal():
    run("client/normal_client.py")
    return index()

@app.route("/flood")
def flood():
    run("client/flood_client.py")
    return index()

@app.route("/scan")
def scan():
    run("client/port_scan_client.py")
    return index()

@app.route("/api/logs")
def api_logs():
    path = os.path.join(BASE, "logs/system.log")
    if not os.path.exists(path):
        return jsonify([])

    data = []
    with open(path) as f:
        for line in f.readlines()[-50:]:
            data.append(json.loads(line))
    return jsonify(data)

if __name__ == "__main__":
    app.run()
