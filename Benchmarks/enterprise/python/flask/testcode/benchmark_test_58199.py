# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58199():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
