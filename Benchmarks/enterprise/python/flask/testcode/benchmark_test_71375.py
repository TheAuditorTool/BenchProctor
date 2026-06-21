# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71375():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
