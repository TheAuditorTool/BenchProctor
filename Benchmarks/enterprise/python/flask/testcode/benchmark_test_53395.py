# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest53395():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
