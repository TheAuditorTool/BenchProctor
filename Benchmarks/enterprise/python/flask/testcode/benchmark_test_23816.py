# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23816():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
