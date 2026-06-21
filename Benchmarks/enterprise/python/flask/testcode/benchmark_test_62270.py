# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest62270():
    multipart_value = request.form.get('multipart_field', '')
    data = to_text(multipart_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
