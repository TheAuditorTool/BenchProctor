# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76777():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
