# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest78401():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return jsonify({"result": "success"})
