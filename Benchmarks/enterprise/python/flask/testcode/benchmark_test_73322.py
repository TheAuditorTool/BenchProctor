# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73322():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
