# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42637():
    referer_value = request.headers.get('Referer', '')
    try:
        int(str(referer_value))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
