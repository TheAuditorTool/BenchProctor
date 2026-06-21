# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12121():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
