# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20043():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
