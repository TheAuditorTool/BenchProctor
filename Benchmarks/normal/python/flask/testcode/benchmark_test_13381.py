# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest13381():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
