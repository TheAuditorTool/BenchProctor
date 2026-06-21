# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest24273():
    referer_value = request.headers.get('Referer', '')
    data = ensure_str(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
