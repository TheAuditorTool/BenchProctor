# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest22768():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
