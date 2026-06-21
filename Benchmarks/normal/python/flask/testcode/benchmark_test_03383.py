# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03383():
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
