# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16307():
    field_value = request.form.get('field', '')
    return jsonify({'error': str(field_value), 'stack': repr(locals())}), 500
