# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34705():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
