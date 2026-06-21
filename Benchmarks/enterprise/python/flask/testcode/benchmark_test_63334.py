# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest63334():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    session['data'] = str(data)
    return jsonify({"result": "success"})
