# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00704():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
