# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest35448():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if json_value not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + json_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
