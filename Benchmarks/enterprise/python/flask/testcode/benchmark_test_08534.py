# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest08534():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
