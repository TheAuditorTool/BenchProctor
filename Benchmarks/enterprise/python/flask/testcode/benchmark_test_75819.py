# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75819():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
