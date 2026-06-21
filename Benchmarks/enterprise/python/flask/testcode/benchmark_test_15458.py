# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15458():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
