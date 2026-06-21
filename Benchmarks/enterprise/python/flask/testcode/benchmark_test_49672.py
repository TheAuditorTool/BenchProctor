# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49672():
    origin_value = request.headers.get('Origin', '')
    try:
        int(str(origin_value))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
