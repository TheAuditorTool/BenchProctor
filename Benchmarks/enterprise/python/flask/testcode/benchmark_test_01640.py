# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01640():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
