# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46421():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
