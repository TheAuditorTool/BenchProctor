# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest07656():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500
