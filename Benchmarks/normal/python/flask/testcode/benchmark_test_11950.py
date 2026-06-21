# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest11950():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
