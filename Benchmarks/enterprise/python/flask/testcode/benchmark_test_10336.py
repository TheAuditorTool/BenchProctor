# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest10336():
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(cookie_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = cookie_value
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
