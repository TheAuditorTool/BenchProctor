# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest36515():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(forwarded_ip)):
        return jsonify({'error': 'invalid input'}), 400
    processed = forwarded_ip
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
