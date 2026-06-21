# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52339():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
