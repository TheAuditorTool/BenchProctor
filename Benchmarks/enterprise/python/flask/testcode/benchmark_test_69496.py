# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69496():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500
