# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import hashlib
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest43494(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
