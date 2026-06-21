# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43147():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
