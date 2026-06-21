# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56307():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    int(str(data))
    return jsonify({"result": "success"})
