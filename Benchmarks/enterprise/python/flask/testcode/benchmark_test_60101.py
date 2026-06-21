# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60101():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
