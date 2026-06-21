# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest40234():
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
