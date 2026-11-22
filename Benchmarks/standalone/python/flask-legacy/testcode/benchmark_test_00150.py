# SPDX-License-Identifier: Apache-2.0
import re
from flask import Flask, jsonify
from flask import render_template_string
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00150", methods=["POST"])
def BenchmarkTest00150():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string('<div>{{ value|safe }}</div>', value=str(processed))
