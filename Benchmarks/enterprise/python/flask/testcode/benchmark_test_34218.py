# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34218():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
