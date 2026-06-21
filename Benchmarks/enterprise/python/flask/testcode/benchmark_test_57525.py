# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57525():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
