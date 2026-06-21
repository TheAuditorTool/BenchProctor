# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest21902():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500
