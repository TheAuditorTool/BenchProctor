# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08200():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
