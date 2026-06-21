# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def BenchmarkTest64120():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
