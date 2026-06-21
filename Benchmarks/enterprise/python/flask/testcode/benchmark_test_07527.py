# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest07527():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    session['user'] = str(data)
    return jsonify({"result": "success"})
