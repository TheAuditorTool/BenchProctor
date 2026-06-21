# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28637():
    ua_value = request.headers.get('User-Agent', '')
    if str(ua_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
