# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest77564():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
