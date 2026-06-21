# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25626():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
