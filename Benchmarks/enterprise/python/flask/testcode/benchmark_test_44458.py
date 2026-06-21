# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest44458():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    processed = data[:64]
    return jsonify({'error': str(processed), 'stack': repr(locals())}), 500
