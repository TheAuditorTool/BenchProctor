# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13451():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
