# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74409():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
