# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest62829():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500
