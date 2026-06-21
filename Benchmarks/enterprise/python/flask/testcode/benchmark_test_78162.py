# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78162():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
