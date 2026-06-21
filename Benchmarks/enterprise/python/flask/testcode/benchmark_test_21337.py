# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest21337():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
