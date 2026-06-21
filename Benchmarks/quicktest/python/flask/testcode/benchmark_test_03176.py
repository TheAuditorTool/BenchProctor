# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03176():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
