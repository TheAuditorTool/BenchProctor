# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04099():
    upload_name = request.files['upload'].filename
    return jsonify({'error': 'An internal error occurred'}), 500
