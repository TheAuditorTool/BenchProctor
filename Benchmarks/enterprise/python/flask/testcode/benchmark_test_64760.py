# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64760():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
