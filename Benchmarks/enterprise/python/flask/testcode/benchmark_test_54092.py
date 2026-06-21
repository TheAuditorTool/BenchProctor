# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest54092():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
