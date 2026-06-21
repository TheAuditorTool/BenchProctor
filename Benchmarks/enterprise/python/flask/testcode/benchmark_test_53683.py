# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53683():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
