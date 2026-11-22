# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00011", methods=["POST"])
def BenchmarkTest00011():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % (config_value,)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return jsonify({"result": "success"})
