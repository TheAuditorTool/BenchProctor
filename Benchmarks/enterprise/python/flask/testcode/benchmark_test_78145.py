# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest78145():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
