# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23126():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if str(json_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
