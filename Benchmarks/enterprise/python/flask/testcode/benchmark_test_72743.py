# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest72743():
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
