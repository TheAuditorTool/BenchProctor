# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest04386(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
