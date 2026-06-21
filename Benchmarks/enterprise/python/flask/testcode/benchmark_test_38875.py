# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest38875():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
