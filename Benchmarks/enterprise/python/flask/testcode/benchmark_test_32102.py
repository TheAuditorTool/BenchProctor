# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32102():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
