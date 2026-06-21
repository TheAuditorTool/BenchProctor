# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05914():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
