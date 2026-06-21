# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest55008():
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
