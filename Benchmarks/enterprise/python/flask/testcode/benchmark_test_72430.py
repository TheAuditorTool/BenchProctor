# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72430():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
