# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12302():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
