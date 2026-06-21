# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest25147():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500
