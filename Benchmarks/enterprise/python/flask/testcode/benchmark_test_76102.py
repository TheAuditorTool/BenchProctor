# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76102():
    header_value = request.headers.get('X-Custom-Header', '')
    if str(header_value).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
