# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17829():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
