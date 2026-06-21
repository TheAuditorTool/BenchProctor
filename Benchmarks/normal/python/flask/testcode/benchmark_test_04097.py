# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest04097():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    os.unlink(checked_path)
    return jsonify({"result": "success"})
