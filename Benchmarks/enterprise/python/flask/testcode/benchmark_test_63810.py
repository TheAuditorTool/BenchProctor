# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest63810():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500
