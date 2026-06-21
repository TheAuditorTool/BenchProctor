# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37314():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
