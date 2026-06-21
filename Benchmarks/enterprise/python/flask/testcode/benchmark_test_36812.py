# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify
import hashlib
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest36812():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
