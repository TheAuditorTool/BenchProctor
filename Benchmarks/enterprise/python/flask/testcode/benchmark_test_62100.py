# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62100():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
