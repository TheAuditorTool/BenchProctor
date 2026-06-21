# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18325():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
