# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest69610():
    header_value = request.headers.get('X-Custom-Header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(header_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = header_value
    return render_template_string(processed)
