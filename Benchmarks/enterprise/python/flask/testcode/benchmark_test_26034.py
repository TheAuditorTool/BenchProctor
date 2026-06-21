# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26034():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
