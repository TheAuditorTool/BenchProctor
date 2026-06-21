# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74467():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
