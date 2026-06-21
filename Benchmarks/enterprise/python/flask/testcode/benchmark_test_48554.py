# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48554():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if str(json_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
