# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest19242():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
