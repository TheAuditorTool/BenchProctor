# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02807():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
