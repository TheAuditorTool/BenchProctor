# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19724():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
