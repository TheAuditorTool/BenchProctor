# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05916():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
