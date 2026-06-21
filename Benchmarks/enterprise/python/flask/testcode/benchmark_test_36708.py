# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36708():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
