# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42012():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
