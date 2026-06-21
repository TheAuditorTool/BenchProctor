# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20577():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
