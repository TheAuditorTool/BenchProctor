# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61089():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
