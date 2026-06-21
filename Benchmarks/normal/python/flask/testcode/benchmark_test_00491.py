# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify


def BenchmarkTest00491():
    auth_header = request.headers.get('Authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
