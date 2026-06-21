# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04572():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
