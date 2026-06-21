# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest12606():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
