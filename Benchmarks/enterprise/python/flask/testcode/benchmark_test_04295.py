# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04295():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
