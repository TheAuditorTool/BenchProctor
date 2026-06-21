# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50124():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    return jsonify({'error': 'An internal error occurred'}), 500
