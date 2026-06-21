# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58467():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
