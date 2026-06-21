# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01814():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
