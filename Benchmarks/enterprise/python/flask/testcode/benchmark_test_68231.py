# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68231():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
