# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest27786():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
