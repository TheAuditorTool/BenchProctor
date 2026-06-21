# SPDX-License-Identifier: Apache-2.0
import re
import json
from flask import request, jsonify


def BenchmarkTest25085():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
