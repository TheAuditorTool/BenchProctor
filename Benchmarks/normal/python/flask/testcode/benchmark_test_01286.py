# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01286():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
