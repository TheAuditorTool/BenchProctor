# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest61313():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
