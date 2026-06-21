# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00229():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
