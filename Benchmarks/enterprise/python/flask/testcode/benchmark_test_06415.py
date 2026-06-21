# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest06415():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
