# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76683():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
