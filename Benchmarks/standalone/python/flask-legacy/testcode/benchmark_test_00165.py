# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
import re
import json
from flask import jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00165", methods=["POST"])
def BenchmarkTest00165():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(processed) + '</div>')
    return resp
