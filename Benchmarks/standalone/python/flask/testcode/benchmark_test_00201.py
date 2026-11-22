# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
import re
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00201", methods=["POST"])
def BenchmarkTest00201():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(processed) + '</div>')
    return resp
