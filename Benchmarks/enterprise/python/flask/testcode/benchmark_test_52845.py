# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52845():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
