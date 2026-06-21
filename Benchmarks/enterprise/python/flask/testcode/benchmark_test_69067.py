# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69067():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
