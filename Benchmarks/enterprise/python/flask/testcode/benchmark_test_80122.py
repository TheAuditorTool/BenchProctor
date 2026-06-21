# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import base64
from flask import request, jsonify


def BenchmarkTest80122():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
