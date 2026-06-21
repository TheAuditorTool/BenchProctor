# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest48322():
    ua_value = request.headers.get('User-Agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
