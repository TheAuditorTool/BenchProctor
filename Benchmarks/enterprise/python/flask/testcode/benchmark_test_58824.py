# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest58824():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
