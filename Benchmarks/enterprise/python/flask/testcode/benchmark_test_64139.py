# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64139():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
