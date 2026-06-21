# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest75170():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
