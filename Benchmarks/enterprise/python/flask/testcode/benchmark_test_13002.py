# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13002():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
