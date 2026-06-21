# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34968():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
