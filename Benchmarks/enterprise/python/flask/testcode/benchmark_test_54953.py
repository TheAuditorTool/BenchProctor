# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest54953():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
