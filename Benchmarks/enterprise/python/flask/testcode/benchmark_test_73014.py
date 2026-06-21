# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73014():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
