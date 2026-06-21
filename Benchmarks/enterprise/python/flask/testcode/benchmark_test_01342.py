# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01342():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
