# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest46814():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
