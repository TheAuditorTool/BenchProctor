# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest78300():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
