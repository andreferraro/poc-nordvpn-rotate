"""
POC Sidecar
"""
import urllib.request
from flask import Flask, jsonify, request
from vpn_handle import NordVPN

nordvpn = NordVPN()

app = Flask(__name__)


@app.route("/ip", methods=["GET"])
def my_ip():
    external_ip = urllib.request.urlopen(
        "https://ident.me").read().decode("utf8")
    if request.method == "GET":
        data = {"ip": external_ip}
        return jsonify(data)


@app.route("/connect", methods=["GET"])
def connect():
    if request.method == "GET":
        nordvpn.connect()
        data = {"status": True}
        return jsonify(data)


@app.route("/rotate", methods=["GET"])
def rotate():
    if request.method == "GET":
        nordvpn.rotate()
        data = {"status": True}
        return jsonify(data)


@app.route("/disconnect", methods=["GET"])
def disconnect():
    if request.method == "GET":
        nordvpn.disconnect()
        data = {"status": True}
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
