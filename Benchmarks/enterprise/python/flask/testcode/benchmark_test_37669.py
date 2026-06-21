# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37669():
    multipart_value = request.form.get('multipart_field', '')
    return jsonify({'error': str(multipart_value), 'stack': repr(locals())}), 500
