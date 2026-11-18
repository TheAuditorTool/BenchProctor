# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from urllib.parse import urlparse
from flask import jsonify
import re
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00270", methods=["POST"])
def BenchmarkTest00270():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(db_value).strip()
        case _:
            data = str(db_value)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
