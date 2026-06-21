# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest24721():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
