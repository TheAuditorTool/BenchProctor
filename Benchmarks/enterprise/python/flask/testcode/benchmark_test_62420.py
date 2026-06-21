# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62420():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        int(str(json_value))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
