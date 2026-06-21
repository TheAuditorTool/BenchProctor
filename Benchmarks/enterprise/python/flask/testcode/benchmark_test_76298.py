# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76298():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
