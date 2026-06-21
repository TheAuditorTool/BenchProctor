# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest32762():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
