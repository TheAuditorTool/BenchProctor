# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest03235():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return jsonify({"result": "success"})
