# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest62061():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
