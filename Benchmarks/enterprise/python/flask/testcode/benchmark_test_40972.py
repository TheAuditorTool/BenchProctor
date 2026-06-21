# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import hashlib
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40972():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
