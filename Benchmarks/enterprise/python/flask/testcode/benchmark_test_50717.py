# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50717():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
