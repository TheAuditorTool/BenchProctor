# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01085():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
