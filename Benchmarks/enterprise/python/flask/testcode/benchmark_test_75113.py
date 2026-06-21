# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75113():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
