# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00194():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
