# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14194():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
