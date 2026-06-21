# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73239():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
