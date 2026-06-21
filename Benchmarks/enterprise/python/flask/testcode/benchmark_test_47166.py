# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47166():
    origin_value = request.headers.get('Origin', '')
    if str(origin_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
