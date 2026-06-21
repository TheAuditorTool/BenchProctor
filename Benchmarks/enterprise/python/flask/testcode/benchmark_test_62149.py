# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62149():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    return jsonify({'error': 'An internal error occurred'}), 500
