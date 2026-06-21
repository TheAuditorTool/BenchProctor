# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest17578():
    origin_value = request.headers.get('Origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = origin_value
    return str(processed), 200, {'Content-Type': 'text/html'}
