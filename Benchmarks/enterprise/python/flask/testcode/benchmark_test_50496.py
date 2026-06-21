# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50496():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
