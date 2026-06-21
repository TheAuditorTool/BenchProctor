# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
import base64
from flask import request, jsonify


def BenchmarkTest05205():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
