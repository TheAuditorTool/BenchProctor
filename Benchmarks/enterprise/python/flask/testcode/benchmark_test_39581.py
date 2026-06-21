# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest39581():
    host_value = request.headers.get('Host', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(host_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = host_value
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
