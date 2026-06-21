# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest02928():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
