# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest41152():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
