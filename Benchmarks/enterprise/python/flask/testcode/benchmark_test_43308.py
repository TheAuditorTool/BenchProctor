# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43308():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
