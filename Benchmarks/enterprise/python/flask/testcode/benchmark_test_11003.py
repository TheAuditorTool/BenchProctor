# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11003():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500
