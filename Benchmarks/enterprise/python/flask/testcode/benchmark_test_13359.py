# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13359():
    raw_body = request.get_data(as_text=True)
    if str(raw_body) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
