# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75264():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return jsonify({'error': 'An internal error occurred'}), 500
