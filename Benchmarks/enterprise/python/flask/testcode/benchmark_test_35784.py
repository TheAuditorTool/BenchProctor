# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35784():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
