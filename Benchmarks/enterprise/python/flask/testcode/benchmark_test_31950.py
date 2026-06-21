# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31950():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
