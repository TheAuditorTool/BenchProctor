# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06380():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
