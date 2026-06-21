# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38206():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
