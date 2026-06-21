# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28370():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
