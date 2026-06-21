# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest01785():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
