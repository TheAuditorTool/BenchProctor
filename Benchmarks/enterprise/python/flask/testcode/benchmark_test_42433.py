# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42433():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
