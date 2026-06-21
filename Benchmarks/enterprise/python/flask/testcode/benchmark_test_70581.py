# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest70581():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ensure_str(json_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
