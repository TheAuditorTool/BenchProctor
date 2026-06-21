# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20345():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
