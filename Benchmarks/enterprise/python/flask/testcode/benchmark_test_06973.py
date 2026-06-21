# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06973():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
