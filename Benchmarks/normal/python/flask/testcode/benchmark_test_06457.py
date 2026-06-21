# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06457():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
