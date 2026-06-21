# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06796():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
