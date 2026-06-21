# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48954():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
