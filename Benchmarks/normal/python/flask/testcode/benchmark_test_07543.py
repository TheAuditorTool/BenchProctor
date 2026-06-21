# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07543():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
