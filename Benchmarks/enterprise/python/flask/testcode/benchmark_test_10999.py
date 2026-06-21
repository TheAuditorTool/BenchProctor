# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def BenchmarkTest10999():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
