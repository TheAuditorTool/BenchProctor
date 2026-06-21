# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest23730():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
