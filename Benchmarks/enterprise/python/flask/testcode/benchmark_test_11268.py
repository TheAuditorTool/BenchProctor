# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11268():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
