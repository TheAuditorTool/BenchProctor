# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest17762(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
