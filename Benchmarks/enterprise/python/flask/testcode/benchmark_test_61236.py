# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61236():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
