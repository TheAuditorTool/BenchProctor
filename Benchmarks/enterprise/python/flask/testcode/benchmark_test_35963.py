# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import hashlib
from app_runtime import db


def BenchmarkTest35963():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
