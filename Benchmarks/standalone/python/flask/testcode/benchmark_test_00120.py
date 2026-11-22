# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00120/<path_param>", methods=["POST"])
def BenchmarkTest00120(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    Path(checked_path).write_text('data')
    return jsonify({"result": "success"})
