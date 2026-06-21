# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35867():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
